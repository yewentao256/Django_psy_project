import json

from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# 花园心情与评论列表
from psygarden.models import Message, Comment
from user.models import User


# 获取心情和评论列表
def psygardenList(request):
    if request.method == "POST":
        current_page = request.POST.get("current_page", None)
        type = request.POST.get("type", None)
        token = request.POST.get("token", None)
        # 判断空值
        if None in [current_page, type]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    if eval(type) == 0:
        try:
            user = User.objects.get(token=token)
        except Exception as e:
            return JsonResponse({"code": 0, "msg": "无效的用户token！"})
        messages = user.message.all().reverse()
    else:
        messages = Message.objects.filter(type=1).reverse()

    # 分页
    per_page = 15
    lst = []  # 消息列表
    comment_lst = []  # 评论列表
    paginator = Paginator(messages, per_page)

    for obj in paginator.get_page(current_page).object_list:
        # 判断匿名
        if eval(obj.anonymity) == 1:
            dic = {"id": obj.id, "mood": obj.mood, "avatar": "files/avatar/default.jpg", "user_nickname": "匿名用户",
                   "time": int(obj.create_time.timestamp()), "content": obj.content, "comment_list": []}
        else:
            dic = {"id": obj.id, "mood": obj.mood, "avatar": obj.user.avatar, "user_nickname": obj.user.user_nickname,
                   "time": int(obj.create_time.timestamp()), "content": obj.content, "comment_list": []}

        # 如果为公共花园追加评论
        if eval(type) == 1:
            for comment in obj.comment.all().reverse():
                if eval(comment.anonymity)==1:
                    dic2 = {"id": comment.id, "avatar": "files/avatar/default.jpg", "user_nickname": "匿名用户",
                            "time": int(comment.create_time.timestamp()), "content": comment.content}
                else:
                    dic2 = {"id": comment.id, "avatar": comment.user.avatar, "user_nickname": comment.user.user_nickname,
                            "time": int(comment.create_time.timestamp()), "content": comment.content}
                dic["comment_list"].append(dic2)
        lst.append(dic)

    data = {"total": paginator.count, "per_page": per_page, "current_page": current_page,
            "total_page": paginator.num_pages,
            "list": lst}
    return JsonResponse({"code": 1, "msg": "查询成功！", "data": json.dumps(data)})


# 发表心情
def mood_message(request):
    if request.method == "POST":
        token = request.POST.get("token", None)
        mood = request.POST.get("mood", None)
        content = request.POST.get("content", None)
        type = request.POST.get("type", None)
        anonymity = request.POST.get("anonymity", None)
        # 判断空值
        if None in [token, mood, content, type, anonymity]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
        if type == 0 and anonymity == 1:
            return JsonResponse({"code": 0, "msg": "私人花园不允许匿名"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    try:
        user = User.objects.get(token=token)
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "无效的用户token！"})

    new_message = Message(user=user, mood=mood, type=type, content=content, anonymity=anonymity)
    new_message.save()
    return JsonResponse({"code": 1, "msg": "发表成功！"})


# 发表的评论
def comment(request):
    if request.method == "POST":
        token = request.POST.get("token", None)
        id = request.POST.get("id", None)
        content = request.POST.get("content", None)
        anonymity = request.POST.get("anonymity", None)
        # 判断空值
        if None in [token, content, anonymity, id]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    try:
        user = User.objects.get(token=token)
        message = Message.objects.get(id=id)
        if eval(message.type) == 0:  # 在内部的存储方式是char
            return JsonResponse({"code": 0, "msg": "只能对公共花园发表评论！"})
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "无效的用户token或心情id！"})

    new_comment = Comment(user=user, message=message, content=content, anonymity=anonymity)
    new_comment.save()
    return JsonResponse({"code": 1, "msg": "评论成功！"})

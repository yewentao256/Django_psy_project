import json
import random
import re
import string
import os

from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from psy.settings import BASE_DIR, BASE_URL
from .models import User, Consultant


# 用户登录
def login(request):
    # 获取数据
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 判断空值
        if None in [username, password]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    # 检验用户是否存在
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "错误的用户名或密码！", "data": ""})
    if user.password == password:
        # 随机生成字符串token
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(88)]
        user.token = "".join(str_list)
        user.save()
        return JsonResponse({"code": 1, "msg": "登录成功！", "data": user.token})
    else:
        return JsonResponse({"code": 0, "msg": "错误的用户名或密码！", "data": ""})


# 用于注册的views
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        repassword = request.POST.get("repassword", None)
        # 判断空值
        if None in [username, password, repassword]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    if password == repassword:
        if User.objects.filter(username=username):
            return JsonResponse({"code": 0, "msg": "用户名已注册！"})
        else:
            new_user = User(username=username, password=password)
            new_user.save(())
            return JsonResponse({"code": 1, "msg": "注册成功！"})
    else:
        return JsonResponse({"code": 0, "msg": "输入的密码不一致！"})


# 用于修改密码的views
def updatePass(request):
    if request.method == "POST":
        password = request.POST.get("password", None)
        newpassword = request.POST.get("newpassword", None)
        repassword = request.POST.get("repassword", None)
        token = request.POST.get("token", None)
        # 判断空值
        if None in [newpassword, password, repassword, token]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    if newpassword == repassword:
        try:
            user = User.objects.get(password=password, token=token)
        except Exception as e:
            return JsonResponse({"code": 0, "msg": "用户校验失败"})
        user.password = newpassword
        user.save(())
        return JsonResponse({"code": 1, "msg": "修改密码成功！"})
    else:
        return JsonResponse({"code": 0, "msg": "输入的密码不一致！"})


# 获取用户资料
def getUserInfo(request):
    if request.method == "POST":
        token = request.POST.get("token", None)
        # 判断空值
        if None in [token]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    try:
        user = User.objects.get(token=token)
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "用户校验失败"})
    data = {"id": user.id, "sex": user.sex, "birthday": user.birthday,
            "create_time": user.create_time,
            "user_nickname": user.user_nickname,
            "user_email": user.user_email, "avatar": user.avatar, "signature": user.signature,
            "mobile": user.mobile, "address": user.address, "user_status": user.user_status}
    return JsonResponse({"code": 1, "msg": "查询成功！", "data": data})


# 编辑用户资料
def editUserInfo(request):
    if request.method == "POST":
        token = request.POST.get("token", None)
        sex = request.POST.get("sex", None)
        birthday = request.POST.get("birthday", None)
        user_nickname = request.POST.get("user_nickname", None)
        user_email = request.POST.get("user_email", None)
        avatar = request.POST.get("avatar", None)
        signature = request.POST.get("signature", None)
        mobile = request.POST.get("mobile", None)
        address = request.POST.get("address", None)
        # 判断空值
        if None in [token, sex, birthday, user_nickname, user_email, avatar, signature, mobile, address]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
        if not re.match(r"^1[35678]\d{9}$", mobile):
            return JsonResponse({"code": 0, "msg": "手机号格式错误！", "传入的手机号": mobile})
        if not re.match(r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$", user_email):
            return JsonResponse({"code": 0, "msg": "邮箱格式错误！", "传入的邮箱": mobile})

    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    try:
        user = User.objects.get(token=token)
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "用户校验失败"})
    user.sex = sex
    try:
        user.birthday = birthday
        user.user_nickname = user_nickname
        user.user_email = user_email
        user.avatar = avatar
        user.signature = signature
        user.mobile = mobile
        user.address = address
        user.save()
    except Exception as e:
        return JsonResponse({"code": 0, "msg": str(e)})
    return JsonResponse({"code": 1, "msg": "修改成功！"})


# 用户验证
def verifyUser(request):
    if request.method == "POST":
        token = request.POST.get("token", None)
        name = request.POST.get("name", None)
        sex = request.POST.get("sex", None)
        mobile = request.POST.get("mobile", None)
        idcard = request.POST.get("idcard", None)
        # 判断空值
        if None in [token, sex, name, idcard, mobile]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
        if not re.match(r"^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$",
                        idcard):
            return JsonResponse({"code": 0, "msg": "身份证格式错误！", "传入的身份证": idcard})
        if not re.match(r"^1[35678]\d{9}$", mobile):
            return JsonResponse({"code": 0, "msg": "手机号格式错误！", "传入的手机号": mobile})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    try:
        user = User.objects.get(token=token)
    except Exception as e:
        return JsonResponse({"code": 0, "msg": "用户校验失败"})

    user.sex = sex
    user.name = name
    user.mobile = mobile
    user.idcard = idcard
    user.user_status = 1
    user.save()
    return JsonResponse({"code": 1, "msg": "用户校验成功！"})


# 咨询师列表
def consultantList(request):
    if request.method == "GET":
        current_page = request.GET.get("current_page", None)
        # 判断空值
        if None in [current_page]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为GET！"})

    per_page = 3
    consultantlst = []
    consultants = Consultant.objects.all()
    paginator = Paginator(consultants, per_page)


    # 对当前页咨询师序列化
    lst = paginator.get_page(current_page).object_list
    for consultant in lst:
        dic = model_to_dict(consultant)
        del dic['user']
        del dic['create_time']
        dic['name'] = consultant.user.name
        dic['address'] = consultant.user.address
        dic['mobile'] = consultant.user.mobile
        dic['avatar'] = consultant.user.avatar
        consultantlst.append(dic)
    data = {"total": paginator.count, "per_page": per_page, "current_page": current_page,
            "total_page": paginator.num_pages,
            "list": consultantlst}
    return JsonResponse({"code": 1, "msg": "查询成功！", "data": json.dumps(data)})


"""# 上传用户相关的文件
def upload_file(request):
    if request.method == "POST":  # 获取对象
        file = request.FILES.get("file", None)
        type = request.POST.get("type", None)
        token = request.POST.get("token", None)
        if None in [file, type, token] or type not in ["avatar"]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值或类型错误"})
        try:
            user = User.objects.get(token=token)
        except Exception as e:
            return JsonResponse({"code": 0, "msg": "无效token！"})

        write_position = os.path.join(BASE_DIR, "files", "user", str(user.id), file.name)  # 写文件的路径
        url = BASE_URL + "/files/user" + str(user.id) + file.name  # url访问的路径

        f = open(write_position, "wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        if type == "avatar":
            user.avatar = url
            user.save()
        return JsonResponse({"code": 1, "msg": "操作成功！", "data": user.avatar})
    else:
        return JsonResponse({"code": 0, "msg": "需要以POST形式访问"})"""

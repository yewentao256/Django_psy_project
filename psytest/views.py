import random

from django.http import JsonResponse
from django.shortcuts import render
from .models import Questions


# Create your views here.
# 获取测试题目
def getTestQuestions(request):
    if request.method == "POST":
        number = int(request.POST.get("number", None))
        # 判断空值
        if None in [number]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})
        # 获取指定数量的题目

    questions = list(Questions.objects.all())
    if number> len(questions):
        return JsonResponse({"code": 0, "msg": "请求的题目数量过多"})
    question_rawlist = random.sample(questions, number)

    # 序列化操作
    question_list = []
    for i in range(len(question_rawlist)):
        question = question_rawlist[i]
        question_list.append({"topic_id": question.id,
                              "topic":question.topic,
                              "tend": question.tend,
                              "options": [{"option_id": 1, "content": question.choose1},
                                          {"option_id": 2, "content": question.choose2}]})

    return JsonResponse({"code": 1, "msg": "查询成功！", "data": question_list})


# 上传测试答案并返回测试结果
def uploadTest(request):
    if request.method == "POST":
        data = eval(request.POST.get("data", None))
        # 判断空值
        if None in [data]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值"})
    else:
        return JsonResponse({"code": 0, "msg": "请求模式需要为POST！"})

    # "内向/外向":0, "实感/直觉":1, "思考/情感":2, "判断/知觉":3
    dic = {"0": 0, "1": 0, "2": 0, "3": 0}
    for i in range(len(data)):
        choice = data[i]
        if choice["option_id"] == 0:
            dic[str(choice["tend"])] -= 1
        else:
            dic[str(choice["tend"])] += 1
    result = {"内向/外向": dic["0"], "实感/直觉": dic["1"], "思考/情感": dic["2"], "判断/知觉": dic["3"]}
    return JsonResponse({"code": 1, "msg": "操作成功！", "result": result})

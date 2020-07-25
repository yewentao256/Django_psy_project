from django.http import JsonResponse
import os
from psy.settings import BASE_DIR, BASE_URL


# 上传文件
def upload_file(request):
    if request.method == "POST":  # 获取对象
        file = request.FILES.get("file", None)
        type = request.POST.get("type", None)
        if None in [file, type] or type not in ["avatar"]:
            return JsonResponse({"code": 0, "msg": "传入的信息存在空值或类型错误"})

        write_position = os.path.join(BASE_DIR, "files", type, file.name)  # 写文件的路径
        url = "files/" + type + "/" + file.name  # url访问的路径

        f = open(write_position, "wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return JsonResponse({"code": 1, "msg": "操作成功！", "data": url})
    else:
        return JsonResponse({"code": 0, "msg": "需要以POST形式访问"})

#python 3.7 的 Linux 环境
FROM python:3.7

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 添加 Debian 清华镜像源
RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
    > /etc/apt/sources.list


# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code

# 添加 pip 清华镜像源
RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple

# 将 requirements.txt 复制到容器的 code 目录
ADD requirements.txt /code/
# 安装库, 添加 pip 清华镜像源
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 将当前目录复制到容器的 code 目录
ADD . /code/

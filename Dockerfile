FROM python:3.7

WORKDIR ./

ADD . .

RUN sed -i "s@http://deb.debian.org@http://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
RUN cat /etc/apt/sources.list
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y libgl1

RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip3 install -r requirements.txt

# RUN pip3 uninstall opencv-python -y

# RUN pip3 install opencv-python-headless

CMD ["python3", "./main.py"]

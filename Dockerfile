FROM python:3.6
WORKDIR /root/docker_project/zaowu

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "main:app", "-c", "./gunicorn.conf.py"]
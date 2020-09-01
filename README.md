# zaowu
zaowu app UI design

# Server运行方式：

1.非py36环境下需要切换 | source py36venv/bin/activate

2.静默启动 | nohup python3.6 -u server.py > res.log 2>&1 &

3.gunicorn启动方式 | gunicorn main:app -c gunicorn.conf.py

# Docker运行方式：

1.生产环境运行 | sudo docker run -itd -p 5001:5001 zhangpeng0v0/zaowu

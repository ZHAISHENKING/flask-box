# flask-box
🚀可复用工厂模式框架

## 使用的库
- [x] flask
- [x] flask-admin
- [x] mongoengine
- [x] flask-migrate
- [x] Flask-Script
- [x] flask-API
- [x] flask-WTF

## 配置

1. 使用mongo创建一个初始数据库`demo`或把`config.py`中的`db`改成自己的数据库    
2. 服务器上使用需创建`production.py`，写入自己的数据库信息，默认git提交会过滤掉`production.py`,保证生产配置只存在服务器    
```
ENV = 'prd'
PORT = 27017
NAME = ""
PWD = ""
```
本地配置在`local_settings.py`，用于区分生产和开发环境    
```
ENV = 'dev'
PORT = 27017
NAME = ""
PWD = ""
```
3. 环境依赖安装   
```bash
pip install -r requirements.txt
```

## 启动

```python
python manage.py runserver
```

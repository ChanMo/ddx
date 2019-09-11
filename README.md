# MDX

Django + React + Docker 基础模板

## 包含

* django2.2
* postgres
* gunicorn
* redis
* node10
* react

## 目录结构

* docker-compose.yml
* deploy.yml.example # 正式版docker-compose文件
* Dockerfile # 用于创建django-docker
* Service # 使用systemctl实例
* nginx.conf.example # 正式版nginx配置文件示例
* web-docker # api-docker 文件
* requirements.txt # api-docker 文件
* local-example.py # 扩展api settings文件

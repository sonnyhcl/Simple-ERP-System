# Simple Web Project
Midterm Project for Course  `Database System` `COMP130010.03` in Fudan. 

>   **DDL: 5.2**  **PRE: 5.9**



>   课程要求
>
>   -   数据库关系设计 30%
>   -   操作正确性 30%
>   -   基本功能完善性（增删改查、权限管理）30%
>   -   应用场景、功能的创新性 10%  [我们的代加工系统说明文档](https://github.com/sonnyhcl/SimpleWebProject/blob/master/doc/%E4%BB%A3%E5%8A%A0%E5%B7%A5%E4%BF%A1%E6%81%AF%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AF%B4%E6%98%8E.md)

## Run Configuration

>   make sure you have install `python2.7 64bit` `virtualenv` `git`

###### 1. git

```bash
~$ git clone https://github.com/sonnyhcl/SimpleWebProject.git
# other git command
~/SimpleWebProject$ git pull
~/SimpleWebProject$ git add .
~/SimpleWebProject$ git commit -m "your comment"
~/SimpleWebProject$ git push
```

###### 2. Virtualenv Configuration

```bash
~/SimpleWebProject$ virtualenv venv
~/SimpleWebProject$ source venv\Scripts\activate # windows
~/SimpleWebProject$ source venv/bin/activate 	 # unix
(venv) ~/SimpleWebProject$ pip install -r requirements.txt 
```

> Python Requirement
> [requirement.txt](https://github.com/sonnyhcl/SimpleWebProject/blob/master/requirements.txt)

###### 3. Pycharm

>    **File->Settings->Projects->Projects Struct** 里选择`webapp`为`source folder`

![Pycharm设置](https://github.com/sonnyhcl/SimpleWebProject/blob/master/devops/pycharm_config.jpg)

###### 4. 运行

```bash
(venv) ~/SimpleWebProject$ python run.py
```

###### 4. Database Configuration

```python
host='localhost'
port=3306
user='root'
passwd='root'
database='web'
```

## Repo Organization

```bash
.
├── devops # 运维
│   ├── cron_wxrobot.sh
│   └── wxrobot.py
├── doc	# 文档
│   ├── raw_data
│   ├── 代加工信息管理系统说明.md
│   ├── 代加工流程图.jpg
│   ├── 前后端url接口设计.xlsx
│   ├── 数据库接口设计.xlsx
│   └── 网页前端设计.xlsx
├── logs # 日志
│   └── webapp.log
├── README.md
├── requirements.txt # python依赖包
├── run.py	# 运行入口
├── tree.txt
└── webapp # 网站工程
    ├── auth
    ├── config.py
    ├── db
    ├── __init__.py
    ├── static
    ├── templates
    └── views
```

## Reference Link

-   Git教程   [Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)
-   Flask中文教程  [http://docs.jinkan.org/docs/flask](http://docs.jinkan.org/docs/flask)
-   BootStrap中文网  [http://www.bootcss.com/](http://www.bootcss.com/)
-   Flask Project Demo  [https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr](https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr)
-   ORM编写指南   [http://www.liaoxuefeng.com](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001402228705570c9506d546a3349c6b7d64135127672fe000)
-   `n`NF规范   [http://www.open-open.com/lib/view/open1404791721950.html](http://www.open-open.com/lib/view/open1404791721950.html)  
-   flask-sqlite [http://docs.pythontab.com/flask/flask0.10/patterns/sqlite3.html](http://docs.pythontab.com/flask/flask0.10/patterns/sqlite3.html)
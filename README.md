# Simple Web Project
Midterm Project for Course  `Database System` `COMP130010.03` in Fudan.

>   课程要求
>
>   -   数据库关系设计 30%
>   -   操作正确性 30%
>   -   基本功能完善性（增删改查、权限管理）30%
>   -   应用场景、功能的创新性 10%

>   [需求文档](https://github.com/sonnyhcl/SimpleWebProject/blob/master/doc/%E4%BB%A3%E5%8A%A0%E5%B7%A5%E4%BF%A1%E6%81%AF%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E8%AF%B4%E6%98%8E.md)

>   **DDL: 5.2**
>
>   **PRE: 5.9

## Assignment

-   [HCl](https://github.com/sonnyhcl) 和[ZBY](https://github.com/zjjzby)负责搭建Flask本地运行环境和服务器运行环境，完成登录与权限管理部分。
-   [tinylic](https://github.com/tinylic)负责数据表字段的设计，并将对数据表的增删改SQL操作封装成python API。
-   [Cjj](Michael0134)负责前端页面设计和前后端交互设计。


## Run Configuration

>   `python 2.7` `64bit`
>
>   `mysql` `64bit`
>
>   `virtualenv`
>
>   `pycharm`

#### Git Command

```bash
git pull
git add .
git commit -m "your comment"
git push
```

#### Virtualenv Configuration

```bash
~/SimpleWebProject$ virtualenv venv
~/SimpleWebProject$ source venv/Scripts/activate
(venv) ~/SimpleWebProject$ pip install -r requirements.txt 
```

#### Python Requirement

```python
appdirs==1.4.3
click==6.7
dominate==2.3.1
Flask==0.12.1
Flask-Bootstrap==3.3.7.1
Flask-Login==0.4.0
Flask-Migrate==2.0.3
Flask-MySQL==1.4.0
Flask-Script==2.0.5
Flask-SQLAlchemy==2.2
Flask-WTF==0.14.2
itsdangerous==0.24
Jinja2==2.9.6
Mako==1.0.6
MarkupSafe==1.0
packaging==16.8
PyMySQL==0.7.11
pyparsing==2.2.0
python-editor==1.0.3
six==1.10.0
SQLAlchemy==1.1.9
visitor==0.1.3
Werkzeug==0.12.1
WTForms==2.1
```

#### MySQL Configuration

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
├── devops 	# 运维
│   ├── cron_wxrobot.sh
│   └── wxrobot.py
├── doc		# 需求文档
│   ├── url命名示例.xlsx
│   ├── 代加工信息管理系统说明.md
│   ├── 代加工流程图.jpg
│   ├── 代工品制作时间清单.xlsx
│   ├── 数据库基本表设计.xlsx
│   └── 运行环境配置.md
├── logs	# 日志文件
│   └── webapp.log
├── README.md
├── requirements.txt # 依赖文件
├── venv			# virtual-env
└── webapp			# web工程
    ├── config.py
    ├── __init__.py
    ├── run.py
    ├── static		# 静态文件夹
    ├── templates	# 模版文件夹
    ├── views.py
```

## Reference Link

-   Git教程   [Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)
-   Flask中文教程  [http://docs.jinkan.org/docs/flask](http://docs.jinkan.org/docs/flask)
-   BootStrap中文网  [http://www.bootcss.com/](http://www.bootcss.com/)
-   Flask Project Demo  [https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr](https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr)
-   ORM编写指南   [http://www.liaoxuefeng.com](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001402228705570c9506d546a3349c6b7d64135127672fe000)
-   `n`NF规范   [http://www.open-open.com/lib/view/open1404791721950.html](http://www.open-open.com/lib/view/open1404791721950.html)  
# Simple Web Project
Midterm Project for Course  `Database System` `COMP130010.03` in Fudan.

>   **DDL: 5.2**
>
>   **PRE: 5.9**


### Assignment Organization

-   [HCl](https://github.com/sonnyhcl) 和[ZBY](https://github.com/zjjzby)负责搭建Flask本地运行环境和服务器运行环境，完成登录与权限管理部分。
-   [tinylic](https://github.com/tinylic)负责数据表字段的设计，并将对数据表的增删改SQL操作封装成python API。
-   [Cjj](Michael0134)负责前端页面设计和前后端交互设计。


### Reference Link

-   Flask中文教程	[http://docs.jinkan.org/docs/flask](http://docs.jinkan.org/docs/flask)
-   BootStrap中文网  [http://www.bootcss.com/](http://www.bootcss.com/)
-   Flask Project Demo  [https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr](https://github.com/pallets/flask/tree/master/examples/flaskr/flaskr)
-   ORM编写指南   [http://www.liaoxuefeng.com](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001402228705570c9506d546a3349c6b7d64135127672fe000)
-   `n`NF规范   [http://www.open-open.com/lib/view/open1404791721950.html](http://www.open-open.com/lib/view/open1404791721950.html)  


### Repo Organization

```bash
.                                                         
├── doc                   # 需求文档                                
│   └── 需求文档.docx                                         
├── logs                  # 日志目录                                
│   └── log.txt                                           
├── README.md                                             
├── requirements.txt      # 依赖库                                
└── webapp                # web工程文件夹                                
    ├── app                                               
    │   ├── auth          # 权限管理                                
    │   │   └── __init__.py                               
    │   ├── db            # 数据库连接                                
    │   │   └── __init__.py                               
    │   ├── __init__.py                                   
    │   ├── main          # 业务逻辑                                
    │   │   └── __init__.py                               
    │   ├── static        # 静态文件                                
    │   │   ├── bootstrap-3.3.7-dist                      
    │   │   │   ├── css                                   
    │   │   │   │   ├── bootstrap.css                     
    │   │   │   │   ├── bootstrap.css.map                 
    │   │   │   │   ├── bootstrap.min.css                 
    │   │   │   │   ├── bootstrap.min.css.map             
    │   │   │   │   ├── bootstrap-theme.css               
    │   │   │   │   ├── bootstrap-theme.css.map           
    │   │   │   │   ├── bootstrap-theme.min.css           
    │   │   │   │   └── bootstrap-theme.min.css.map       
    │   │   │   ├── fonts                                 
    │   │   │   │   ├── glyphicons-halflings-regular.eot  
    │   │   │   │   ├── glyphicons-halflings-regular.svg  
    │   │   │   │   ├── glyphicons-halflings-regular.ttf  
    │   │   │   │   ├── glyphicons-halflings-regular.woff 
    │   │   │   │   └── glyphicons-halflings-regular.woff2
    │   │   │   └── js                                    
    │   │   │       ├── bootstrap.js                      
    │   │   │       ├── bootstrap.min.js                  
    │   │   │       └── npm.js                            
    │   │   └── images                                    
    │   │       └── gold.png                              
    │   └── templates    # 页面模版                                 
    │       ├── 404.html                                  
    │       ├── error.html                                
    │       └── index.html                                
    ├── __init__.py                                       
    ├── run.wsgi                                          
    └── webapp.py        # app入口   
```


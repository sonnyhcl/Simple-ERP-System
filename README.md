# Simple Web Project
Midterm Project for Course  `Database System` `COMP130010.03` in Fudan.

>   **DDL: 5.2**


#### Assignment Organization

-   [HCl](https://github.com/sonnyhcl) 和[ZBY](https://github.com/zjjzby)负责搭建Flask本地运行环境和服务器运行环境，完成登录与权限管理部分。
-   [tinylic](https://github.com/tinylic)负责数据表字段的设计，并将对数据表的增删改SQL操作封装成python API。
-   [Cjj](Michael0134)负责前端页面设计和前后端交互设计。



#### Repo Organization

```c
.                          
├── doc                    
├── logs                   
│   └── webapp.log         
├── README.md              
├── requirements.txt       
└── webapp                 
    ├── app                
    │   ├── app.py         
    │   ├── auth # 权限管理           
    │   │   └── __init__.py
    │   ├── db   # 数据库API           
    │   │   └── __init__.py
    │   ├── __init__.py    
    │   ├── main # 业务逻辑          
    │   │   └── __init__.py
    │   ├── static          
    │   └── templates # 界面模版     
    │       └── index.html 
    └── __init__.py        
```


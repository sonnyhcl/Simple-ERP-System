# Simple Web Project
Midterm Project for Course  `Database System` in Fudan.



#### Repo organization

```c
├─.gitignore                
├─README.md                 
├─requirements.txt 				    # python依赖包         
│                            
├─docs                       		# 需求文档
├─logs                       		# 日志文件
└─webapp                     		# Flask app
    │  __init__.py           
    │                        
    └─app                    
        │  app.py            
        │  __init__.py       
        │                    
        ├─db               			# 数据库API
        │      __init__.py   
  	    ├─auth               		# 权限管理
        │      __init__.py   
        │                    
        ├─main               		# 业务逻辑
        │      __init__.py   
        │                    
        ├─static             
        └─templates          		# 界面模版
                index.html   
```


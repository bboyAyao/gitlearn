新闻类门户网站
===

![首页](https://github.com/bboyAyao/gitlearn/blob/master/newsSite/minicms/%E9%A1%B5%E9%9D%A2%E5%B1%95%E7%A4%BA.png)

## 介绍

后端 python django 1.8 版本  
数据库 mysql  
前端 bootstrap3    

该网页分为首页和详情页，有浏览记录功能和搜索功能，浏览功能由后端设置cookie拼接字符实现。  
大部分假数据由create_demo_records.py自动生成并存入数据库，一些真实数据由django自带管理后台功能导入。  
搜索用whoosh引擎加上python jieba分词库实现。  
通过model.py设置栏目分类和文章（内容，所属栏目）对应字段表迁移至数据库生成对应表。 

其他django笔记  https://www.jianshu.com/nb/26746209

# 根据Jira号自动统计bug
## 需求说明
当前jira系统不能根据某个需求统计其下的bug情况，使用传统的手工统计，效率低下并且容易出错，本方法通过nodejs访问页面，遍历元素实现自动统计，从而提高效率 
## 前置条件
1.安装nodeJs环境，官网：https://nodejs.org/en/  
## 使用方法 
1.首先手工登录jira环境，浏览器控制台中得到JSESSIONID，记录此id并在界面输入，否则会登录失败导致无数据 
![Image text](http://git.300.cn/yangqin/TEST-DOCUMENT/raw/master/09.%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B0%8F%E5%B7%A5%E5%85%B7/bugSummaryForJira/output/jsessionid.png)  
2.初次使用需要切换到对应目录并执行命令：npm install，生成node_modules文件夹    
3.执行命令开启服务程序：node server.js  
4.浏览器中打开地址：http://localhost:8888/sumary 输入相关统计信息    
JSESSIONID：输入步骤1中记录的jsessionId   
需求编号：如2611       
统计模式：all（默认），include，exclude  
包含模式（include）和排除模式（include）需要输入对应的过滤条件，多个过滤条件使用英文分号分割，并且是逻辑或的关系      

## 输出结果
![Image text](http://git.300.cn/yangqin/TEST-DOCUMENT/raw/master/09.%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B0%8F%E5%B7%A5%E5%85%B7/bugSummaryForJira/output/output.png)

## 待优化问题
手工记录JSESSIONID不太方便，可以考虑从登陆界面，输入jira账号获取JSESSIONID，但是目前通过发送jira登陆请求时，总是登陆失败，暂未找到解决办法    

## 版本历史
v1.0.0：仅实现统计某需求全部bug功能，输入信息（JSESSIONID和需求编号）需要手工编辑脚本对应位置    
v2.0.0：增加交互式命令，输入信息通过终端命令行输入，增加过滤功能（排除和包含模式）    
v3.0.0：增加界面UI，通过B/S形式实现统计功能   
v3.0.1：增加bug级别：危险，增加bug状态：创建需求,并且为0时不展示该统计信息          
v3.0.2：增加bug提交时间，责任人字段并且增加根据状态过滤方法       
v3.0.3：修复包含/排除模式下的promise调用问题           
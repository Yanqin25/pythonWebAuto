# Python web自动化

## 目录结构说明
base:底层基础功能，通过选择器获取元素  
config：存放配置文件，如界面定位使用的选择器信息，格式：user_email=id:register_email   
sourceData:存放excel用例数据   
util：存放常用工具，如读取配置文件，excel工具  
page：获取界面操作元素  
business：封装业务主要逻辑  
case：存放用例  
screenShot:存放失败截图  
report:存放结果报告  
log:存放日志模块  
## 备注  
#### 1.打开浏览器报错，需要下载对应版本的chromedriver并放到python路径中，下载地址：https://npm.taobao.org/mirrors/chromedriver/  
#### 2.验证码图片解析第三方接口：https://www.showapi.com/api/lookPoint/184  

## 辅助功能（前提安装好了python环境）
### 一、excel用例名称前面的序号自动和用例ID的序号保持一致:  
修改util/read_excel.py下的文件路径，直接执行命令 python util/read_excel.py即可  

### 二、将excel用例转为testLink要求的xml，并导入  

### 使用方法:   
1.在util/excel_to_xml.py中，修改用例路径,（index代表用例在excel的第几个页签，从0开始）
![Image text](http://git.300.cn/yangqin/TEST-DOCUMENT/raw/master/09.%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B0%8F%E5%B7%A5%E5%85%B7/UIFunctionAuto/report/excel2xml.png)  
2.在UIFunctionAuto路径下执行 python util/excel_to_xml.py,__main__方法中可以传入结果路径，默认路径见步骤3  
3.得到结果文件UIFunctionAuto/report/testcase_result.xml  
4.将步骤3中的xml文件导入testLink即可(以图片库为例，手工建了目录:内容&页面;选中此节点导入，用例格式必须为指定格式，参考：04.测试用例/后台Vue改造/测试用例-企业图册-待评审-杨勤.xlsx)
![Image text](http://git.300.cn/yangqin/TEST-DOCUMENT/raw/master/09.%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B0%8F%E5%B7%A5%E5%85%B7/UIFunctionAuto/report/importxml.png)  
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
image=Image.open("./screenshot/code1.png")
text=pytesseract.image_to_string(image)
print(text)

# 调用第三方api精确得到验证码
# r = ShowapiRequest("http://route.showapi.com/184-4","89459","eaa40d8760814950b8f216c9f0a4c5c2" )
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "1")
# r.addBodyPara("needMorePrecise", "1")
# r.addFilePara("image", r"./screenshot/code1.png") #文件上传时设置
# res = r.post()
# print(res.json()['showapi_res_body']['Result']) # 返回信息
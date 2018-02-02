'''
from PIL import Image,ImageFilter
#d打开jpg图片
im=Image.open('123.jpg')
#获得图像尺寸
w,h=im.size
print('Original image size:%s*%s'%(w,h))
#缩小50%
im.thumbnail((w//2,h//2))
print('thumbnail image size:%s*%s'%(w//2,h//2))
#把缩小的图片更改格式
im.save('thumbnail.jpg','png')

#模糊效果
im=Image.open('123.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
'''

#生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
# 创建 Font 对象
font=ImageFont.truetype('arial.ttf',36)
#font=ImageFont.load_default().font
#创建 Draw 对象:
draw=ImageDraw.Draw(image)
#填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code3.jpg','jpeg')
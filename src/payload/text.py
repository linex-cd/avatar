
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from util import codec
from util import resp
from util import files

import config
	
def make(filename, text, size):
		
	hash = codec.md5(text.encode())

	bgcolor = (int(hash[0:2],16),  int(hash[2:4], 16),  int(hash[4:6], 16))
	
	img = Image.new('RGB', (size, size), bgcolor) 

	draw = ImageDraw.Draw(img)

	#苹方黑体.ttf 请注意版权
	fontfile = config.assetsdir + "/font/pingfang.ttf"
	
	scale = size / 128
	
	#计算字体
	fontsize = 96 * scale
	if len(text) == 0:
		fontsize = int(96 * scale)
		text = '〇'
	
	elif len(text) == 1:
		fontsize = int(96 * scale)
		
	elif len(text) == 2:
		fontsize = int(64 * scale)
		
	elif len(text) == 3:
		fontsize = int(36 * scale)
		
	else:
		fontsize = int(24 * scale)
		text = text[:4]
	
	font = ImageFont.truetype(fontfile, fontsize, encoding="utf-8")
	
	#尺寸
	text_width, text_height = draw.textsize(text, font)
	
	#颜色
	color = (255, 255, 255)
	
	draw.text((int((size - text_width) / 2), int((size - text_height) / 3) ), text, color, font=font)

	img.save(filename)


#enddef

from fastapi import APIRouter

router = APIRouter()

@router.get(path='/{text}/{size}', summary='文本生成头像', description='文本,0-4长度，尺寸,最大512, 最小128')
def generate(
		   text: str = '',
		   size: int = 128
	):
	
	
	if size>512:size = 512
	if size<128:size = 128
	
	if len(text) > 4: text = text[:4]
	
	hash = codec.md5((text + str(size)).encode())
	
	filename = config.avatardir + '/' + hash[0:2]+ '/' + hash[2:4]+ '/' + hash[4:6]+ '/' + hash + '.jpg'
	
	ret = files.exist_file(filename)
	
	if ret == False:
		files.make_dirs_for_file(filename)
		make(filename, text, size)
	#endif
	
	return resp.resp_png(filename)
	
	
#enddef


if __name__ == '__main__':
	

	make('text.png','郑君', 128)

	cv2.waitKey(0)
#end

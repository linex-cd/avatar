
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from util import codec
from util import resp
from util import files

import config
	



def create_shape(w, h):
	
	
	bgcolor = (0, 0, 0, 0)
	img_shape = Image.new('RGBA', (w, h), bgcolor) 

	draw_shape = ImageDraw.Draw(img_shape)
	
	#形状类型
	type = codec.randomnumber(0, 5)
	#是否填充
	fill = codec.randomnumber(0, 1)
	
	border_width = 2
	
	color_alpha = (codec.randomnumber(0, 255), codec.randomnumber(0, 255), codec.randomnumber(0, 255), codec.randomnumber(32, 64))
	
	x1 = codec.randomnumber(0, w - 1)
	x2 = codec.randomnumber(x1, w + 1)
	y1 = codec.randomnumber(0, h - 1)
	y2 = codec.randomnumber(y1, h + 1)
	


	#线条
	if type == 0 :
		
		y1 = codec.randomnumber(0, w + 1)
		y2 = codec.randomnumber(0, h + 1)
		
		draw_shape.line(((x1, y1), (x2, y2)), fill=color_alpha, width=border_width)
		
		
		
	#endif
	
	#矩形
	if  type == 1 :
		
		if  fill == 1 :
			draw_shape.rectangle(((x1,y1),(x2,y2)),fill=color_alpha,outline=None,width=0)

		else:
			draw_shape.rectangle(((x1,y1),(x2,y2)),fill=None,outline=color_alpha,width=border_width)
		#endif
	#endif
	
	#圆
	if  type == 2 :
		
		if  fill == 1 :
			draw_shape.ellipse(((x1, y1), (x2, y2)), fill=color_alpha, outline=None, width=0)

		else:
			draw_shape.ellipse(((x1, y1), (x2, y2)), fill=None, outline=color_alpha, width=border_width)
	
		#endif
	#endif
	
	
	#椭圆
	if  type == 3 :
		
		if  fill == 1 :
			draw_shape.ellipse((x1, y1, x2, y2), fill=color_alpha, outline=None, width=0)

		else:
			draw_shape.ellipse((x1, y1, x2, y2), fill=None, outline=color_alpha, width=border_width)

		#endif
	#endif
	
	#圆弧
	if  type == 4 :

		start = codec.randomnumber(0, 360-1)
		end = codec.randomnumber(start, 360)
		

		i = codec.randomnumber(0, 3)

		if  fill == 1 :
			 draw_shape.pieslice((x1, y1, x2, y2), start=start, end=end, fill=color_alpha, outline=None, width=0)

		else:
			draw_shape.arc((x1, y1, x2, y2), start=start, end=end, fill=color_alpha, width=border_width)

		#endif
		
		
	#endif
	
	#多边形
	if  type == 5 :
		
		max_size = 7
		polygon_size = codec.randomnumber(3, max_size)
		polygons = []
		
		for i in range(polygon_size):
			x = codec.randomnumber(0, w)
			y = codec.randomnumber(0, h)

			polygons.append((x, y))

		#endfor
		
		if  fill == 1 :
			draw_shape.polygon(polygons, fill=color_alpha, outline=None, width=0)
	
		else:
			draw_shape.polygon(polygons, fill=None, outline=color_alpha, width=border_width)
		#endif
		
		
	#endif
	
	return img_shape
		

#enddef

def add_text(draw, w, h):
		
	text = codec.randomtext(10)

	x1 = codec.randomnumber(0, w - 1)
	x2 = codec.randomnumber(x1, w + 1)
	y1 = codec.randomnumber(0, h - 1)
	y2 = codec.randomnumber(y1, h + 1)

	
	#颜色
	color = (codec.randomnumber(0, 255), codec.randomnumber(0, 255), codec.randomnumber(0, 255), codec.randomnumber(0, 32))

	fontsize = codec.randomnumber(64, 128)
	
	#请注意版权
	fontfile = config.assetsdir + "/font/"+str(codec.randomnumber(0, 5))+".ttf"

	font = ImageFont.truetype(fontfile, fontsize, encoding="utf-8")

	draw.text((x1,y1), text, color, font=font)

	

def make(filename, text, size):
		
	hash = codec.md5(text.encode())

	bgcolor = (int(hash[0:2],16),  int(hash[2:4], 16),  int(hash[4:6], 16))
	
	img = Image.new('RGBA', (size, size), bgcolor) 

	draw = ImageDraw.Draw(img)
	

	#添加形状
	shape = create_shape(size, size)

	#添加文字
	add_text(draw, size, size)
	
	#shape.save(filename+'shape.png')
	#img.save(filename+'img.png')


	layer = Image.alpha_composite(img, shape)
	
	img.paste(layer, (size, size), layer)
	
	
	layer.save(filename)


#enddef

from fastapi import APIRouter

router = APIRouter()

@router.get(path='/{text}/{size}', summary='给种子生成头像', description='文本,0-128长度，尺寸,最大512, 最小128')
def generate(
		   text: str = '',
		   size: int = 128
	):
	
	
	if size>512:size = 512
	if size<128:size = 128
	
	text = codec.md5((text).encode())
	
	hash = codec.md5((text + str(size)).encode())
	
	filename = config.avatardir + '/' + hash[0:2]+ '/' + hash[2:4]+ '/' + hash[4:6]+ '/' + hash + '.png'
	
	ret = files.exist_file(filename)
	
	if ret == False:
		files.make_dirs_for_file(filename)
		make(filename, text, size)
	#endif
	
	return resp.resp_jpg(filename)
	
	
#enddef


if __name__ == '__main__':
	

	make('seed.png','郑君', 512)

	cv2.waitKey(0)
#end

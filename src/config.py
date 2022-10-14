import os
import rpyc
import platform
import contextvars

#静态资源
assetsdir = "./assets"

#静态页面
pagesdir = "./pages"

#文件上传
avatardir = "/data/avatar"


system_disk_dir = '/'
data_disk_dir = '/data'


if platform.system() == 'Darwin' or platform.system() == 'Windows':
	avatardir = "./avatar"
	
	system_disk_dir = './'
	data_disk_dir = './files'

if __name__ == '__main__':
	pass;
# end

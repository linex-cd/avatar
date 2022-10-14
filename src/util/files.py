import os
import shutil

def readraw(filename):
	f = open(filename, "rb")
	if not f:
		return None
	# endif

	data = f.read()

	f.close()

	return data


# enddef

def writeraw(filename, text, mode="w"):
	f = None
	encoding = "UTF-8"
	if mode.find("b") >= 0:
		encoding = None
	# endif

	f = open(file=filename, mode=mode, encoding=encoding);

	f.write(text)
	f.close()
	pass


# enddef

def exist_file(filename):
	if os.path.exists(filename) and os.path.isfile(filename) and os.access(filename, os.W_OK):
		return True
	# endif
	return False


# enddef

def remove_file(filename):
	if exist_file(filename):
		os.remove(filename)


# enddef

def clean_dirs(dirpath):
	if os.path.exists(dirpath) and os.access(dirpath, os.W_OK):
		shutil.rmtree(dirpath)


	# endif
# enddef

def make_dirs_for_file(filename):
	dirname = filename[:filename.rfind('/')]
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	# endif
# enddef


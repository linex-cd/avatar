import random
import string
import hashlib

def randomnumber(start, to):

	number = random.randint(start, to)
	
	return number

def randomtext(length):
    text = ''.join(random.sample(string.ascii_letters + string.digits, length))

    return text


def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    dest = m2.hexdigest()
    return dest




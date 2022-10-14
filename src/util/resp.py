

from fastapi.responses import Response

from util import files


def resp_jpg(filename) -> Response:

	stream = files.readraw(filename)
	print(filename)
	print(len(stream))
	response = Response(status_code=200, content = stream, media_type = 'image/jpg')
	
	return response
	
def resp_png(filename) -> Response:

	stream = files.readraw(filename)
	print(filename)
	print(len(stream))
	response = Response(status_code=200, content = stream, media_type = 'image/png')
	
	return response

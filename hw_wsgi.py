def application(environ, start_response):
	post_env = environ.copy()
	data = "\nWSGI hello world!!\n GET data:\n" + post_env['QUERY_STRING'] + "\nand POST data:";
	post_env['QUERY_STRING'] = ''
	post = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', '0')))
	data += post
	data += '\n'
	start_response("200 OK", [
	("Content-Type", "text/plain"),
	("Content-Length", str(len(data))),])
	return iter([data])

from bottle import get, run, static_file
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

static_files_folder = 'visualization/web/'

@get('/websocket', apply=[websocket])
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else:
            break

@get('/')
def server_static():
        return static_file("index.html", root=static_files_folder)


@get('/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root=static_files_folder)

def start(static_folder):
	global static_files_folder
	static_files_folder = static_folder	
	run(host='127.0.0.1', port=8000, server=GeventWebSocketServer)

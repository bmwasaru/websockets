from flask import Flask, render_template
from tornado.websocket import WebSocketHandler
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop

app = Flask('flaskapp')


@app.route('/')
def messaging():
    return render_template('messaging.html')


class WebSocket(WebSocketHandler):
    def open(self):
        print("Socket opened...")

    def on_close(self):
        print("socket closed...")

    def on_message(self, message):
        self.write_message("Received message: " + message)
        print("Received message: " + message)


if __name__ == '__main__':
    flask_app = WSGIContainer(app)
    server = Application([
        (r'/websocket/', WebSocket),
        (r'.*', FallbackHandler, dict(fallback=flask_app))
    ])
    server.listen(8888)
    IOLoop.instance().start()

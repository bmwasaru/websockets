# Websockets -Tornado and Flask sitting under a tree :blush:

Using Tornado Framework to implement Web Sockets on a Flask web application.

- Wrap the Flask instance in the Tornado WSGIContainer in tornado.wsgi
- Use tornado.web.FallbackHandler to fall back to Flask app instance

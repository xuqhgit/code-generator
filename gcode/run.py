from web import app

if __name__ == '__main__':
    host = ('0.0.0.0', 8086)
    app.run(host=host[0], port=host[1],debug=True)

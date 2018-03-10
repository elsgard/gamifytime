from flask import Flask, request, send_from_directory
app = Flask(__name__, static_folder='', static_url_path='/static')

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)
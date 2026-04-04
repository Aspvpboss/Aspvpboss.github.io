from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

# Serve index.html at /
@app.route("/")
@app.route("/index.html")
def home():
    return send_from_directory('', 'index.html')

# Serve about.html at /about.html
@app.route("/about.html")
def about():
    return send_from_directory('', 'about.html')

# Serve static files automatically
@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)
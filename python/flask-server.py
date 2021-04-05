from flask import Flask, render_template
from core import TorClient


app = Flask(__name__)
client = TorClient()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-container-ip')
def get_container_ip_view():
    ip = client.get_tor_container_ip()
    return f"Container's ip : {ip}"

@app.route('/get-public-ip')
def get_public_ip_view():
    ip = client.get_public_ip()
    return f"Public ip : {ip}"

@app.route('/rotate-ip')
def rotate_ip_view():
    old_ip = client.get_public_ip()
    client.rotate()
    new_ip = client.get_public_ip()
    return f"Old ip : {old_ip}, new ip : {new_ip}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

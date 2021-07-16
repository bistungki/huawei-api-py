from flask.templating import render_template
import huaweisms.api.user as user
import huaweisms.api.wlan as wlan
import huaweisms.api.sms as sms
import huaweisms.api.device as device
from flask import Flask

app = Flask(__name__)

ctx = user.quick_login("admin", "redkocin", "192.168.8.1")

def getsms():
    return sms.get_sms(ctx,1)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/getsms")
def hello():
    return getsms()

@app.route("/reboot")
def reboot():
    device.reboot(ctx)
    return "<p>Device rebooted!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask.templating import render_template
import huaweisms.api.user as user
import huaweisms.api.wlan as wlan
import huaweisms.api.sms as sms
import huaweisms.api.device as device
import huaweisms.api.dialup as dialup
import huaweisms.api.monitoring as mon
 
import sys, os, time
import json




from flask import Flask

app = Flask(__name__)
def ctx():
    con =  user.quick_login("admin", "redkocin", "192.168.8.1")
    print(con)
    return con
def sendsms():
      sms.send_sms(ctx(),"082393031869", "Modem reboot")

def getsms():
    smss = sms.get_sms(ctx(),1)
    return smss

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/mon")
def mon_():
    return mon.status(ctx())

@app.route("/getsms")
def hello():
    return getsms()

@app.route("/modemoff")
def modemoff():
    return dialup.switch_mobile_off(ctx())

@app.route("/modemon")
def modemon():
    return dialup.switch_mobile_on(ctx())

@app.route("/modemstatus")
def modemstatus():
    time.sleep(2)
    return  json.dumps({"status": dialup.get_mobile_status(ctx())})

@app.route("/reboot")
def reboot():
    d = sendsms()
    time.sleep(5)
    return json.dumps({"reboot" : device.reboot(ctx()), "message" : d})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
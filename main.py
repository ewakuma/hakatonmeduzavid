from flask import Flask, render_template, send_from_directory, jsonify, request, abort
from flask_cors import CORS
import pyowm
from datetime import datetime
import calendar
import json
import random

owm = pyowm.OWM("231b6d37a2c9836835ca0d77d8f06de1")

def get_weather(lat, lon):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(lat, lon)
    w = observation.weather
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    print(w.__dict__)

    return w.status

database = {
    "Clear": [
        {
            "title": "1",
            "url": "https://r6---sn-3c27sn7e.googlevideo.com/videoplayback?expire=1607560701&ei=nRnRX_bLDdPXkgbx2ICwBw&ip=107.155.88.192&id=o-AGhtyDsAuGyJXIPXrfGjdmx8hPWR98eNURVtXbBuwRWa&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=rCxx8S16eU5YW_NLbN5_8bAF&gir=yes&clen=1144522&dur=181.101&lmt=1566045753506211&fvip=4&keepalive=yes&beids=9466588&c=WEB&txp=2301222&n=yqky-ipu0XdPUzqb&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgHQAL9dMXx77DG2ew-AVOLbOM_ZCIOKLkTiYo-i1cZrUCICtf70WEfdwhHB4aFPoQx2eSfkrx0JjsaZ1Jt5lhghE1&ratebypass=yes&rm=sn-a5my67z&fexp=9466588&req_id=5f07a4756884a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afve7s&cms_redirect=yes&mh=Ob&mip=185.183.95.80&mm=29&mn=sn-3c27sn7e&ms=rdu&mt=1607539006&mv=m&mvi=6&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAO0x1sPm_Gn3T51dD6MDLSLBASWklGoIxWnEeJaSnmW9AiEA9ZBjh8J8-xWR3M-JNvaNXJwNQKK3j4oLWYmo96RbS1M%3D",
        }
    ],
    "Rain": [
        {
            "title": "2",
            "url": "https://r6---sn-3c27sn7e.googlevideo.com/videoplayback?expire=1607560701&ei=nRnRX_bLDdPXkgbx2ICwBw&ip=107.155.88.192&id=o-AGhtyDsAuGyJXIPXrfGjdmx8hPWR98eNURVtXbBuwRWa&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=rCxx8S16eU5YW_NLbN5_8bAF&gir=yes&clen=1144522&dur=181.101&lmt=1566045753506211&fvip=4&keepalive=yes&beids=9466588&c=WEB&txp=2301222&n=yqky-ipu0XdPUzqb&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgHQAL9dMXx77DG2ew-AVOLbOM_ZCIOKLkTiYo-i1cZrUCICtf70WEfdwhHB4aFPoQx2eSfkrx0JjsaZ1Jt5lhghE1&ratebypass=yes&rm=sn-a5my67z&fexp=9466588&req_id=5f07a4756884a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afve7s&cms_redirect=yes&mh=Ob&mip=185.183.95.80&mm=29&mn=sn-3c27sn7e&ms=rdu&mt=1607539006&mv=m&mvi=6&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAO0x1sPm_Gn3T51dD6MDLSLBASWklGoIxWnEeJaSnmW9AiEA9ZBjh8J8-xWR3M-JNvaNXJwNQKK3j4oLWYmo96RbS1M%3D",
        },  
        {
            "title": "3",
            "url": "https://r1---sn-3c27sn76.googlevideo.com/videoplayback?expire=1607561315&ei=AxzRX9D3BpLikgbf5ZWYAQ&ip=107.155.88.192&id=o-AEdF1BnkPIaPPEPm5J1IeZ48lQLGq_-s11tF9Wxn2ESH&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=LRBjYb2nHtzEXlDC983lhNoF&gir=yes&clen=1650955&dur=265.701&lmt=1582087805068513&fvip=1&keepalive=yes&c=WEB&txp=5431432&n=b8efULmLzRkh0QhS&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgZJsuushLkjSLSkqz4Z76hn5EkzA-0Gw3V_G_xbl5V6oCIQC0SL4kbO9j9_JkoMOX_h14ie2Xadh4LjVlgOTeLhQbYg==&ratebypass=yes&rm=sn-a5mkz7e&req_id=4d122710a736a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afvl7e&cms_redirect=yes&mh=HD&mip=185.183.95.80&mm=29&mn=sn-3c27sn76&ms=rdu&mt=1607539485&mv=m&mvi=1&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgWaSL9QloRR1DdTTT7MBPNYSM5TBb1O_mN3ppSfeUZpgCIQDWgy5RUVcxiNLB_1LVxOaArVgukQpVBuwpu0AAqmDPyg%3D%3D",
        },
    ],
    "Clouds": [
        {
            "title": "4",
            "url": "https://r6---sn-3c27sn7e.googlevideo.com/videoplayback?expire=1607560701&ei=nRnRX_bLDdPXkgbx2ICwBw&ip=107.155.88.192&id=o-AGhtyDsAuGyJXIPXrfGjdmx8hPWR98eNURVtXbBuwRWa&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=rCxx8S16eU5YW_NLbN5_8bAF&gir=yes&clen=1144522&dur=181.101&lmt=1566045753506211&fvip=4&keepalive=yes&beids=9466588&c=WEB&txp=2301222&n=yqky-ipu0XdPUzqb&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgHQAL9dMXx77DG2ew-AVOLbOM_ZCIOKLkTiYo-i1cZrUCICtf70WEfdwhHB4aFPoQx2eSfkrx0JjsaZ1Jt5lhghE1&ratebypass=yes&rm=sn-a5my67z&fexp=9466588&req_id=5f07a4756884a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afve7s&cms_redirect=yes&mh=Ob&mip=185.183.95.80&mm=29&mn=sn-3c27sn7e&ms=rdu&mt=1607539006&mv=m&mvi=6&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAO0x1sPm_Gn3T51dD6MDLSLBASWklGoIxWnEeJaSnmW9AiEA9ZBjh8J8-xWR3M-JNvaNXJwNQKK3j4oLWYmo96RbS1M%3D",
        } ,   
        {
            "title": "5",
            "url": "https://r1---sn-3c27sn76.googlevideo.com/videoplayback?expire=1607561315&ei=AxzRX9D3BpLikgbf5ZWYAQ&ip=107.155.88.192&id=o-AEdF1BnkPIaPPEPm5J1IeZ48lQLGq_-s11tF9Wxn2ESH&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=LRBjYb2nHtzEXlDC983lhNoF&gir=yes&clen=1650955&dur=265.701&lmt=1582087805068513&fvip=1&keepalive=yes&c=WEB&txp=5431432&n=b8efULmLzRkh0QhS&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgZJsuushLkjSLSkqz4Z76hn5EkzA-0Gw3V_G_xbl5V6oCIQC0SL4kbO9j9_JkoMOX_h14ie2Xadh4LjVlgOTeLhQbYg==&ratebypass=yes&rm=sn-a5mkz7e&req_id=4d122710a736a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afvl7e&cms_redirect=yes&mh=HD&mip=185.183.95.80&mm=29&mn=sn-3c27sn76&ms=rdu&mt=1607539485&mv=m&mvi=1&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgWaSL9QloRR1DdTTT7MBPNYSM5TBb1O_mN3ppSfeUZpgCIQDWgy5RUVcxiNLB_1LVxOaArVgukQpVBuwpu0AAqmDPyg%3D%3D",
        },
    ],
    "Rain": [
        {
            "title": "6",
            "url": "https://r6---sn-3c27sn7e.googlevideo.com/videoplayback?expire=1607560701&ei=nRnRX_bLDdPXkgbx2ICwBw&ip=107.155.88.192&id=o-AGhtyDsAuGyJXIPXrfGjdmx8hPWR98eNURVtXbBuwRWa&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=rCxx8S16eU5YW_NLbN5_8bAF&gir=yes&clen=1144522&dur=181.101&lmt=1566045753506211&fvip=4&keepalive=yes&beids=9466588&c=WEB&txp=2301222&n=yqky-ipu0XdPUzqb&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgHQAL9dMXx77DG2ew-AVOLbOM_ZCIOKLkTiYo-i1cZrUCICtf70WEfdwhHB4aFPoQx2eSfkrx0JjsaZ1Jt5lhghE1&ratebypass=yes&rm=sn-a5my67z&fexp=9466588&req_id=5f07a4756884a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afve7s&cms_redirect=yes&mh=Ob&mip=185.183.95.80&mm=29&mn=sn-3c27sn7e&ms=rdu&mt=1607539006&mv=m&mvi=6&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAO0x1sPm_Gn3T51dD6MDLSLBASWklGoIxWnEeJaSnmW9AiEA9ZBjh8J8-xWR3M-JNvaNXJwNQKK3j4oLWYmo96RbS1M%3D",
        } ,   
        {
            "title": "7",
            "url": "https://r1---sn-3c27sn76.googlevideo.com/videoplayback?expire=1607561315&ei=AxzRX9D3BpLikgbf5ZWYAQ&ip=107.155.88.192&id=o-AEdF1BnkPIaPPEPm5J1IeZ48lQLGq_-s11tF9Wxn2ESH&itag=249&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fwebm&ns=LRBjYb2nHtzEXlDC983lhNoF&gir=yes&clen=1650955&dur=265.701&lmt=1582087805068513&fvip=1&keepalive=yes&c=WEB&txp=5431432&n=b8efULmLzRkh0QhS&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgZJsuushLkjSLSkqz4Z76hn5EkzA-0Gw3V_G_xbl5V6oCIQC0SL4kbO9j9_JkoMOX_h14ie2Xadh4LjVlgOTeLhQbYg==&ratebypass=yes&rm=sn-a5mkz7e&req_id=4d122710a736a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-q5u5apox-afvl7e&cms_redirect=yes&mh=HD&mip=185.183.95.80&mm=29&mn=sn-3c27sn76&ms=rdu&mt=1607539485&mv=m&mvi=1&pl=22&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgWaSL9QloRR1DdTTT7MBPNYSM5TBb1O_mN3ppSfeUZpgCIQDWgy5RUVcxiNLB_1LVxOaArVgukQpVBuwpu0AAqmDPyg%3D%3D",
        },
    ],
}

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def hello():
    message = "Hello, World"
    return send_from_directory('pages/','index.html')

@app.route("/js/<path:path>")
def send_js(path):
    print(path)
    return send_from_directory('pages/', path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('pages/', path)


@app.route("/img/<path:path>")
def send_img(path):
    return send_from_directory('pages/img', path)

@app.route("/audio/<path:path>")
def send_audio(path):
    return send_from_directory('pages/audio', path)

@app.route("/api/get_music/", methods=['POST'])
def get_music():
    data = json.loads(request.data)
    print(data)
    lat, lon = data.get('lat', None), data.get('lon', None)
    if lat is None or lon is None:
        return abort(400)
    weather = get_weather(lat, lon)
    music = database[weather]
    random.shuffle(music)
    print(music)
    return jsonify({'music': music})
    

if __name__ == "__main__":
    app.run()

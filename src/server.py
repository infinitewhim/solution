from flask import Response, Flask
import prometheus_client
import time
import requests
from threading import Thread
from util import get_url_200_info, get_url_503_info


app = Flask(__name__)

# Global variables set up. We choose type gauge for measuring url response time and status
mapping = {}
mapping["time"] = prometheus_client.Gauge("url_monitor_response_time", "This is response time", ["url"])
mapping["status"] = prometheus_client.Gauge("url_monitor_status", "This is status", ["url"])

    
def start_monitor():
    print("monitoring internet URLs...")
    flag = True
    # we could write some logic to make the infinite loop more robust,
    # but for simplicity, we keep it this way
    while True:
        try:
            # 200 url
            url_200_resp_time, url_200_status = get_url_200_info()
            # 503 url
            url_503_resp_time, url_503_status = get_url_503_info()
            mapping["time"].labels("https://httpstat.us/200").set(url_200_resp_time)
            mapping["time"].labels("https://httpstat.us/503").set(url_503_resp_time)
            mapping["status"].labels("https://httpstat.us/200").set(url_200_status)
            mapping["status"].labels("https://httpstat.us/503").set(url_503_status)
        except requests.exceptions.Timeout:
            # could use logger
            print("Timeout experienced when querying URLs....")

        time.sleep(1)
        if flag == False:
            break

def start_monitor_thread():
    mon_thread = Thread(target=start_monitor)
    mon_thread.start()
    # could use logger in these places
    print("-------- monitor started ----------------")

start_monitor_thread()
    
@app.route("/metrics")
def requests_count():
    res = []
    for _, value in mapping.items():
        res.append(prometheus_client.generate_latest(value))
    return Response(res, mimetype="text/plain")

 

    
    

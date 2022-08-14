import requests


url_503 = "https://httpstat.us/503"
url_200 = "https://httpstat.us/200"
timeout = 5


def get_url_200_info():
    response = requests.get(url_200, timeout=timeout)
    url_200_resp_time = response.elapsed.total_seconds() * 1000
    url_200_status = 1 if response.status_code == 200 else 0
    return url_200_resp_time, url_200_status

def get_url_503_info():
    response = requests.get(url_503, timeout=timeout)
    url_503_resp_time = response.elapsed.total_seconds() * 1000
    url_503_status = 0 if response.status_code == 503 else 1
    return url_503_resp_time, url_503_status
# URL monitoring   

# Local testing without K8S  
A docker-compose.yaml file has been provived in order to be able to test locally. Once you execute ```docker-compose up```, the monitoring server(python-server), Prometheus, Grafana images will be build and services will be started. You should be able to see the exposed metrics in ```http://localhost:5000/metrics```, Prometheus in ```http://localhost:9090/```, Grafana in ```http://localhost:3000/```. Prometheus is set up to scrape our exposed metrics, and you just need to set up data sources, dashboards etc. in order to visulize it in Grafana.<br><br><br>


# Testing with K8S  
## Build process
Executing ```./build.sh``` will build the python-server images( stored in your local ). To make it simple for the test, we don't push the image to external online registries

## Deploy to k8s cluster
After setting up kube config correctly in you local, executing ```./deploy.sh``` will deploy our app into the cluster. There will be a deployment, and also a service.
In order to make the Prometheus in your cluster to scape our server(service), you need modify your prometheus config properly. 

# Unittest
At root directory of the repo, execute ```python3 -m unittest tests/test_app.py```.
Unit tests can be triggered with pre-commit hooks.

# Screenshots
<img width="1440" alt="prometheus_url_status_up_down" src="https://user-images.githubusercontent.com/8725900/184554229-37b657cf-6a59-4f77-ad06-9383c7a7524a.png">
<img width="1438" alt="prometheus_url_resp_time" src="https://user-images.githubusercontent.com/8725900/184554238-793d74e1-64a1-4c3d-8b00-dd56b0bffdb0.png">
<img width="1429" alt="prometheus_url_resp_time2" src="https://user-images.githubusercontent.com/8725900/184554243-3be3bdc9-514b-42d8-b74b-852bed3846df.png">
<img width="1431" alt="prometheus_url_status_up_dow<img width="1015" alt="grafana_status_up_down" src="https://user-images.githubusercontent.com/8725900/184554257-7caa2dcc-0d2f-4dd4-9e2c-509c1ff13134.png">
<img width="1003" alt="grafana_resp_time" src="https://user-images.githubusercontent.com/8725900/184554355-61fa2cf1-8018-4060-9f4a-21ee593ea434.png">


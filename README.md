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

#!/bin/bash

# deploy the server into K8S cluster
# could use helm charts for more complex cases
kubectl apply -f manifests/deployment.yaml
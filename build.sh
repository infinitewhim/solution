#!/bin/bash

# Build the image
docker build --tag infinitewhim/python-server .

# Push the image to dockerhub
# docker push infinitewhim/python-server:latest
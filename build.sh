#!/bin/bash

# Build server images in local. 
# To make it simple for the test, we don't push the image to external registries
docker build --tag python-server .
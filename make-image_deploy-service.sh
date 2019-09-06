#!/usr/bin/env bash
sudo docker build -t kingdo/knative-helloworld-python .
sudo docker push kingdo/knative-helloworld-python
kubectl delete --filename service.yaml
kubectl apply --filename service.yaml
kubectl get pods
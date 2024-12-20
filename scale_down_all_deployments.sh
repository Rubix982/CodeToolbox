#!/bin/bash

# Get all deployment names in the default namespace and scale them to 0 replicas
kubectl get deployments -n default -o jsonpath='{.items[*].metadata.name}' | tr ' ' '\n' | while read -r deployment; do
  echo "Scaling down deployment: $deployment"
  kubectl scale deployment "$deployment" --replicas=0 -n default
done


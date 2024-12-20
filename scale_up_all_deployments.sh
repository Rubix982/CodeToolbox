#!/bin/bash

# Revert scale to original replicas (scale back up)
kubectl get deployments -o jsonpath='{.items[*].metadata.name}' | tr ' ' '\n' | while read -r deployment; do
    echo "Scaling up deployment: $deployment to 1 replicas"
    kubectl scale deployment "$deployment" --replicas="1"
done


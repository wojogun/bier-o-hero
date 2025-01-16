#!/bin/bash

# Namespace festlegen
NAMESPACE="bierohero"

# Filtern des ersten Pods, der "mcce24-akt2-app-deployment" enthält
POD_NAME=$(kubectl get pods -n "$NAMESPACE" --no-headers | grep "frontend" | awk 'NR==1 {print $1}')
echo $POD_NAME

# Prüfen, ob ein Pod gefunden wurde
if [ -z "$POD_NAME" ]; then
  echo "Kein Pod mit 'frontend' gefunden."
  exit 1
fi

# Ausführen des Pods mit kubectl exec
kubectl exec -it "$POD_NAME" -n "$NAMESPACE" -- /bin/ash
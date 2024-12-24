# Overview
Deploying Jenkins instance in K8s for use in the different projects as CI/CD

# Deployment Steps
## Step 1 : Create a namespace
  $ kubectl create namespace jenkins

Confirm:
 $ kubectl get namespace
NAME              STATUS   AGE
default           Active   17d
jenkins           Active   11s
kube-node-lease   Active   17d
kube-public       Active   17d
kube-system       Active   17d

## Step 2 : Provision storage i,e persistentVolume and persistentVolumeClaim.
  $ kubectl apply -f manifests/jenkins-storage.yaml

Confirm:
  $ kubectl get persistentvolume
  $ kubectl get persistentvolumeclaim

## Step 3 : Deploy jenkins instance
 
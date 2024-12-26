# Overview
REF: https://www.jenkins.io/doc/book/installing/kubernetes/
Deploying Jenkins instance in K8s for use in the different projects as CI/CD

# Deployment Steps
## Step 1 : Create a namespace
  Create a Namespace for Jenkins. It is good to categorize all the DevOps tools as a separate namespace from other applications.
  
  $ kubectl create namespace devops-tools

Confirm:
 $ kubectl get namespace
NAME              STATUS   AGE
default           Active   17d
devops-tools      Active   25m
kube-node-lease   Active   17d
kube-public       Active   17d
kube-system       Active   17d

## Step 2: Create the service account using kubectl

The 'jenkins-serviceAccount.yaml' creates a 'jenkins-admin' clusterRole, 'jenkins-admin' ServiceAccount and binds the 'clusterRole' to the service account.

The 'jenkins-admin' cluster role has all the permissions to manage the cluster components. You can also restrict access by specifying individual resource actions.

## Step 2 : Provision storage i,e persistentVolume and persistentVolumeClaim.
  $ kubectl apply -f manifests/jenkins-storage.yaml

Confirm:
  $ kubectl get persistentvolume
  $ kubectl get persistentvolumeclaim

## Step 3 : Deploy jenkins instance
  $ kubectl apply -f manifests/jenkins-deployment.yaml

Confirm : 
  $ kubectl get deployments -n jenkins
  $ kubectl get pod -n jenkins
  $ kubectl get svc -n jenkins

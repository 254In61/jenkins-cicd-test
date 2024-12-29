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
- Build ClusterRole with set permissions.
- Build ServiceAccount within the devops-tools namespace
- Bind the ClusterRole to the ServiceAccount, effectively giving the permissions to the ServiceAccount

 $ kubectl apply -f manifests/jenkins-serviceAccount.yaml
clusterrole.rbac.authorization.k8s.io/jenkins-cr created
serviceaccount/jenkins-sa created
clusterrolebinding.rbac.authorization.k8s.io/jenkins-cr-sa-binding created

 Confirm:

  $ kubectl get ClusterRole      
  $ kubectl describe ClusterRole jenkins-cr

  $ kubectl get ServiceAccount -n devops-tools
  $ kubectl describe ServiceAccount jenkins-sa -n devops-tools

  $ kubectl get ClusterRoleBinding
  $ kubectl describe ClusterRoleBinding jenkins-cr-sa-binding

## Step 3 : Provision storage i,e persistentVolume and persistentVolumeClaim.
  $ kubectl apply -f manifests/jenkins-storage.yaml

Confirm:
  $ kubectl get sc
  $ kubectl describe sc jenkins-sc

  $ kubectl get pv
  $ kubectl describe pv jenkins-pv

  $ kubectl get pvc
  $ kubectl describe sc jenkins-pvc

## Step 4 : Deploy jenkins instance
  $ kubectl apply -f manifests/jenkins-deployment.yaml

Confirm : 
  $ kubectl describe deployment jenkins-deployment -n devops-tools

## Step 5 : Route jenkins service to the outside world

  $ kubectl apply -f manifests/jenkins-service.yaml
   service/jenkins-service created

Confirm :
  $ kubectl get svc -n devops-tools
  $ kubectl describe svc jenkins-service -n devops-tools
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

Confirm pod is up and running:
  $ kubectl get pods -n devops-tools
    NAME                                READY   STATUS    RESTARTS   AGE
    jenkins-deployment-c7b45ff9-brm4v   1/1     Running   0          2m35s

## Step 5 : Route jenkins service to the outside world

  $ kubectl apply -f manifests/jenkins-service.yaml
   service/jenkins-service created

Confirm :
  $ kubectl get svc -n devops-tools
  $ kubectl get svc -n devops-tools
NAME          TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
jenkins-svc   NodePort   10.152.183.149   <none>        8080:30000/TCP   6m31s

## Step 6 - Accessing the Jenkins UI
- With NodePort and Jenkins operational, you are ready to access the Jenkins UI and begin exploring it.

- Your NodePort service is accessible on port 30000 across the cluster nodes.
  You need to retrieve a node IP to access the Jenkins UI.

  $ kubectl get nodes -o wide
  NAME        STATUS   ROLES    AGE   VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
  sexy-guy    Ready    <none>   22d   v1.31.3   192.168.1.98    <none>        Ubuntu 24.04.1 LTS   6.8.0-48-generic   containerd://1.6.28
  the-eagle   Ready    <none>   22d   v1.31.3   192.168.1.100   <none>        Ubuntu 22.04.5 LTS   6.8.0-49-generic   containerd://1.6.28

- Get to Jenkins url : 
  http://<node internal ip>:30000
  example:
  http://192.168.1.100:30000

## Step 7 : Set up credentials and activate Jenkins

7.1) - Return to your terminal and retrieve your Pod name
  $ kubectl get pods -n devops-tools
  NAME                                READY   STATUS    RESTARTS   AGE
  jenkins-deployment-c7b45ff9-brm4v   1/1     Running   0          15m

7.2) - Next, check the Pod’s logs for the admin password.
  $ kubectl logs jenkins-deployment-c7b45ff9-brm4v -n devops-tools

  You might need to scroll up or down to find the password:

*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

<your password>

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************

7.3) - Copy your_jenkins_password. Now return to your browser and paste it into the Jenkins UI.
  - Continue the rest of steps from there.
  

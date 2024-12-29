Deploying Prometheus on your MicroK8s home cluster to monitor the cluster and running pods involves the following steps:

** Steps below take place in the worker-node, the-eagle

# Step 1 : Enable MicroK8s Addons
- MicroK8s provides a simple way to set up Prometheus with its observability addons.
1.1) Enable the prometheus addon:
  $ microk8s enable prometheus    .. This deprecated.
  $ microk8s enable observability

1.2) Confirm the deployment:
  - Check namespaces :
  $ kubectl get namespace
NAME              STATUS   AGE
default           Active   22d
devops-tools      Active   4d10h
kube-node-lease   Active   22d
kube-public       Active   22d
kube-system       Active   22d
observability     Active   25m

- Get pods within the observability namespace
 $ kubectl get pods -n observability
NAME                                                     READY   STATUS    RESTARTS      AGE
alertmanager-kube-prom-stack-kube-prome-alertmanager-0   2/2     Running   1 (24m ago)   24m
kube-prom-stack-grafana-649cb6588b-pb4fk                 3/3     Running   0             25m
kube-prom-stack-kube-prome-operator-7c7d5757db-7vlff     1/1     Running   0             25m
kube-prom-stack-kube-state-metrics-7c69654b66-c426g      1/1     Running   0             25m
kube-prom-stack-prometheus-node-exporter-8st6x           1/1     Running   0             25m
kube-prom-stack-prometheus-node-exporter-j5v76           1/1     Running   0             25m
loki-0                                                   1/1     Running   0             24m
loki-promtail-gctrm                                      1/1     Running   0             24m
loki-promtail-jwjbd                                      1/1     Running   0             24m
prometheus-kube-prom-stack-kube-prome-prometheus-0       2/2     Running   0             24m
tempo-0                                                  2/2     Running   0             24m

- Enable metrics-server
 $ microk8s enable observability
Infer repository core for addon observability
Addon core/observability is already enabled

# Step 2 : Verify Prometheus Setup
2.1) Confirm that Prometheus is collecting metrics:
 $ kubectl get svc -n observability
** Look for the Prometheus service***

2.2) Expose the Prometheus UI:
- Use a NodePort or an ingress rule to access it from your laptop
- Since no loadbalancer is to be deployed.
- REF: manifests/prometheus-service.yaml



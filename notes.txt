https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app


docker build -t gcr.io/${PROJECT_ID}/hello-app:v1 .

docker run --rm -p 8080:9999 gcr.io/${PROJECT_ID}/hello-app:v1

gcloud container clusters get-credentials hello-cluster


gcloud config set compute/zone us-central1-c

gcloud container clusters get-credentials cluster-1
gcloud config set compute/zone us-central1-c
gcloud container clusters get-credentials cluster-1



gcloud auth configure-docker


docker push gcr.io/${PROJECT_ID}/hello-app:v1


kubectl create deployment hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1 --v 9

kubectl expose deployment hello-web --type=LoadBalancer --port 80 --target-port 8080

kubectl edit service hello-web




kubectl logs hello-web-58d97944b-dbsw9 -f


 kubectl set image deployment/hello-web hello-app=gcr.io/${PROJECT_ID}/hello-app:v3 --v 9
https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#loss-of-client-source-ip-for-external-traffic


https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer


https://cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress





kubectl expose deployment hello-web  --port 80 --target-port 9999




# LogIngester
Log Ingester
This is a basic application to injest logs in scalable manner. The HTTP server accepts logs in json format on port 3000. It makes use of MongoDB Atlas, a remote mongodb database, to store the logs. 
K8S hpa scales the pods as per the load.

Get URL in Minikube: minikube `service 'service-name' --url`

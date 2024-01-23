# LogIngester
Log Ingester is a part of a project to demonstarte load balancing in cloud, based on various metrices. Original project is to design cloud based social media application using AWS Well Architected Framework. Please find the design and details of the project in report: https://drive.google.com/file/d/1b7ENt0jWYSg8ZpFgx4rKFrAgvMsZYkes/view?usp=sharing


This is a basic application to injest logs in scalable manner. The HTTP server accepts logs in json format on port 3000. It makes use of MongoDB Atlas, a remote mongodb database, to store the logs. 
K8S hpa scales the pods as per the load. The scaling metric is CPU usage.

Get URL in Minikube: minikube `service 'service-name' --url`

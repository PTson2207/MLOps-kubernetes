# Deploying Machine Learning Models on Kubernetes and Docker

## Containerising a Simple ML Model Scoring Service using Flask and Docker

```bash
py-flask-ml-score-api/
    | Dockerfile
    | Pipfile
    | Pipfile.lock
    | api.py
```
executes from flask to docker
``` bash
python run api.py
#then open localhost:5000/score
#run dockerfile
docker build --tag ptson/test-ml-score-api .
docker images
docker run --rm --name test-api -p 5000:5000 -d ptson/test-ml-score-api
docker ps
```
And then test the exposed API endpoint using,
```bash
curl http:localhost:5000/score \
--request POST \
--header "Content-Type: application/json" \
--data '{"X": [1, 2]}'
```
Expect a respone along the line of,
```json
{"score": [1, 2]}
```
## Kubernets testing
```bash
minikube start --memory 2048
kubectl cluster-info
```
### Deploying the Containerised ML Model Service to Kubernetes
```bash
kubectl create deployment test-ml-score-api --image=ptson/test-ml-score-api:latest
```
To check on the status of the deployment run,
```bash
kubectl rollout status deployment test-ml-score-api
```
And to see the pods that is has created run,
```bash
kubectl get pods
``
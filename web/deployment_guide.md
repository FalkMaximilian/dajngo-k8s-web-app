1. Test Django
```
python manage.py test
```


2. Build Container
```
docker build -f Dockerfile \
    -t registry.digitalocean.com/max-falk-containers/django-k8s-web:latest \
    -t registry.digitalocean.com/max-falk-containers/django-k8s-web:v1 \
    .

```

3. Push this container to DO Container Registry
```
docker push registry.digitalocean.com/max-falk-containers/django-k8s-web --all-tags
```

4. Update secrets
```
kubectl delete secret django-k8s-web-prod-env
kubectl create secret generic django-k8s-web-prod-env --from-env-file=web/.env.prod
```

5. Update deployment
```
kubectl apply -f k8s/apps/dajngo-k8s-web.yaml
```

6. Wait for rollout to finish
This is the same name as in the k8s deployment yaml file under metadata
```
kubectl rollout status deploymeny/django-k8s-web-deployment
```


7. Migrate database
Get the name of any one running pod so that we can migrate the database through it
```
export SINGLE_POD_NAME=$(kubectl get pod -l app=django-k8s-web-deployment -o jsonpath="{.items[0].metadata.name}")
```

Run the database migrations through that one pod
```
kubectl exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh
```
---
marp: true
---

# **One step closer to DevOps**

## workshop walkthrough

Welcome everyone! 🐍 🌈

---

# -> Where to start?

- the application is located within the `/helloladies` directory
- Let's write the dockerfile

---

# -> Dockerfile

```
FROM python:3.7

MAINTAINER Pyladies Workshop

WORKDIR /myapp

COPY app/ /myapp/app
COPY requirements.txt /myapp

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]
```

---

# -> Run your container

```
docker build . -t <IMAGE-TAG>   # build container with a tag
docker images                   #show built images
docker run --publish 5000:5000 --env NAME=<YOUR NAME> <IMAGE-TAG> # run container
```

`-env` defines an environment variable that will be present in your container's environment

go to [https://localhost:5000]

---

### -> Things to do

```
docker ps    # to list the running docker processes, and take note of your container's ID
docker logs <CONTAINER-ID>        #to view logs of the container
docker exec -it <CONTAINER-ID> sh #connect to container:
echo $NAME                        #see you env variable from container
docker stop <CONTAINER-ID>        #stop container:
```

---

# -> Exercises

- change the background color of the app
  - rerun steps from run your container
- change text in app
  - rerun steps from run your container
- show and tell

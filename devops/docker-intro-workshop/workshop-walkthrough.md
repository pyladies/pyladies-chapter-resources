---
marp: true
theme: uncover
_class: invert
---

# **One step closer to DevOps**

## workshop walkthrough

Welcome everyone! 🐍 🌈

---

# -> Where to start?

- the application is located within the `/helloladies` directory
- Dockerfile = Recipe

- Image = snapshot

- Container = executing snapshot

---

# -> How?

- make sure the Dockerfile exists and is empty
- base: `FROM python:3.7`
- meta: `MAINTAINER Me+) <email>`
- set the start folder: `WORKDIR myapp/`
- file system needs files: `COPY app /myapp/app`
- don't forget other files: `COPY requirements.txt myapp/`

---

# -> How? (contd.)

- install dependencies (as you normally would): `RUN pip install -r requirements.txt`
- communicate with the outside world: `EXPOSE 5000`
- Make the app work: `CMD ["python", "app/app.py"]`

---

# -> Run your container

- build container with a tag `$ docker build . -t <IMAGE-TAG>`
- show built images `docker images`
- run container `docker run --publish 5000:5000 --env NAME=<YOUR NAME> <IMAGE-TAG>`
- `-env` defines an environment variable that will be present in your container's environment
- go to [https://localhost:5000]

---

### -> Things to do

- `docker ps` to list the running docker processes, and take note of your container's ID
- `docker logs <CONTAINER-ID>` to view logs of the container
- connect to container: `docker exec -it <CONTAINER-ID> sh`
  - see you env variable from container: `echo $NAME`
- stop container: `docker stop <CONTAINER-ID>`

---

# -> Exercises

- change the background color of the app
  - rerun steps from run your container
- change text in app
  - rerun steps from run your container
- show and tell

---

### -> CheatSheet

![w:1000](cheatsheet.jpg)

---

# -> What for?

- Simplicity
- Reproducibility
- Scalability
- Collaboration+)
- Better sand boxing during development

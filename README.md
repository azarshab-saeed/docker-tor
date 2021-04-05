# docker-tor
Yet another tor-on-docker project, based on a tor container and a python client
which can **send requests to tor container** and also **make tor container's
public ip rotated**.

## Dependencies
* docker-compose

## Start project
```bash
docker-compose up -d --build
```
It launches two containers:
* Tor
* Flask server

## Test
When containers are running well:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

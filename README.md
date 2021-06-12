

## Configuration
All the python dependencies are present in  `./app/requirements.txt` file. The dependencies can be installed using pip package manager. 

Modify the `docker-compose.yml` and `Dockerfile` to your likings to configure exposed ports, volume mounts, extra files, scripts etc.

## Using the image in development
To not have to rebuild the container each time you have updated your code. If you are using docker-compose, you can run the command:
```
docker-compose build && docker-compose run --rm app bash
```
This will build a docker image and with the dependencies in the requirements.txt file, and then run the container with the console attached.

If you are using the image with pure docker, you can use the following commands:
```
docker build -t my-python-app .
docker run -it --rm -v "$PWD:/usr/src/app my-python-app bash"
```

Note that you can also install the dependencies in `requirements.txt` after you entered the container.

## Using the image in production or on a remote docker host
When the code is ready for production or you want to run it on  a remote server, remove the volume mounts and add a storage volume/container to store your files. then run the code as a regular docker-compose container set.
```
docker-compose build
docker-compose up -d
```
## OR
```
docker-compose up
```


## Swagger API Docs
All the api docs are present on endpoint  `localhost:port/apidocs/`

## Python Modules Used
`flask` for API Development 

`requests` for url payload extraction 

`flasgger` for Swaggeer Docs 

`logging` for dev logging 

`pytest` for app testing 

## Python Testing
For testing developer can use `pytest` module after starting up the server for local api testing

## Docker Commands

#### Docker Create Commands
* Create a container from <IMAGE_NAME>
```
docker create <IMAGE_NAME>
```

* Starts the container
```
docker start <container_id or container_name>
```

* Stops the container
```
docker stop <container_name or container_id>
```

* Restarts the container 
```
docker restart <container_name or container_id>
```

* Pause the container
```
docker pause  <container_name or container_id>
```

* Resumes the paused container
```
docker unpause <container_name or container_id>
```

* Kill the container
```
docker kill  <container_name or container_id>
```

* Renames the container to <new_name>
```
docker rename <container_id> <new_name>
```

#### Docker Run Commands

* Builds and runs the image on container
```
docker run <image-name>
```

* Builds and runs the image of specific version
```
docker run <image-name:Tag>
```

* Builds a container with <container_name> from <image_name>
```
docker run --name <container_name> <image_name>
```

* Run the container in interactive mode with sudo terminal
```
docker run -it <image-name>
```

* Publish the container port to host port
```
docker run -p <host_port:container_port>
```

* Persists the data to outside_directory instead of inside container
```
docker run -v <outside_directory:/var/lib/image_name>
```

* Run the container in detach mode(In background) and return <container_id>
```
docker run -d <container_name> or <container_id>
```

* Attach the container back
```
docker attach <container_id>
```

* Run the container with specified environment variable
```
docker run -e <ENV_VARIABLE>=<ENV_VARIABLE_VALUE>  <image_name> or <image_id>
```

* Build a link between already running container and <image_name> container
```
docker run --link <placeholder_container_name>:<already_running_container> <image_name>
```

* Persists the data to outside_directory instead of inside container by specifying type of mounting
```
docker run --mount type=bind, source=/source/path, target=/var/lib/mySQL mysql
```

#### Inspecting the container

* Provide details of container
```
docker inspect <container_name> or <container_id>
```

#### General Docker Commands

* Stop the container from running
```
docker stop <container_name> or <container_id>
```

* Remove the stopped the container
```
docker rm <container_name> or <container_id>
```

* Copies file from source to destination
```
docker cp <source_filepath> <container_id:destination_filepath>
```

* Show all the difference in filesystem change [A-Addition, D-Deletion, C-Changed]
```
docker diff <container_id>
```

* List all the port mapping of the container
```
docker port <container_id>
```

#### Docker Monitoring commands

* Display the logs of PID 1
```
docker logs <container_name> or <container_id>
```

* List all the running container
```
docker ps
```

* List the information about <container_name>
```
docker ps <container_name> or <container_id>
```

* List all the container (Running or Non Running)
```
docker ps -a
```

* Display a live stream of container(s) resource usage statistics
```
docker stats
```

* Display the running process of container in host machine
```
docker top <container_id>
```

#### Docker Volume related commands

* List all the volumes created by container
```
docker volume ls
```

* Creates a volume
```
docker volume create
```

* Creates a volume with <volume_name>
```
docker volume create <volume_name>
```

* Remove all unused local volume
```
docker volume prune
```

* Persists the data in <path_in_container> to <volume_name>
```
docker run -v <volume_name>:<path_in_container> 
```

* Persists the data in <path_in_container> to <path_in_host_machine>
```
docker run -v <path_in_host_machine>:<path_in_container>
```

* Display detailed information on one or more volumes
```
docker inspect <volume_name>
```

#### Docker network related commands

* Creates a network
```
docker network create <network_name>
```

* List networks
```
docker network ls 
```

* Remove one or more networks
```
docker networks rm <network_name>
```

* Remove all unused networks
```
docker network prune 
```

* Display detailed information on one or more networks
```
docker network inspects <network_name>
```

* Connect a container to a network
```
docker network connect <network_name> <container_id>
```

* Creates a container with <Image_name> with network <network_name>
```
docker run -itd --net=<network_name> <Image_name>
```

#### Docker Image related commands

* List all the images
```
docker images
```

* Remove the image
```
docker rmi <image_name> or <image_id>
```

* Downloads the image but won't run it
```
docker pull <image_name>
```

* Lists history of all the layer of images
```
docker history <image-name>
```

#### Executing a command inside container

* Runs the <_command> in <cotainer_name or container_id>
```
docker exec <cotainer_name or container_id> <comand>
```

#### Docker Build related commands
* Builds the image with name <Image_name> from <Dockerfile_name>
```
docker build . -f <Dockerfile name> -t <Image_name>
```
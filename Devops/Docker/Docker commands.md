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
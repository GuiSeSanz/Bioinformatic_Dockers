# Dockers

docker build -t <IMAGENAME> .

#create a container
docker run -itd --name <CONTAINERNAME> <IMAGENAME> bash

# enter the container interactively
docker exec -it <CONTAINERNAME> /bin/bash

# launch a command to the container
docker exec -it <CONTAINERNAME> Rscript /ImputationSaver/ImputeData.R

docker cp <src-path> <container>:<dest-path>
docker cp <container>:<src-path> <local-dest-path>
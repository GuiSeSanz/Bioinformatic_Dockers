# Dockers

`docker build -t <IMAGENAME> .`

### create a container and keep it running forever
`docker run -itd --name <CONTAINERNAME> <IMAGENAME> bash`

### create a container and run it
`docker run -it <IMAGENAME> bash`

### enter the container interactively
`docker exec -it <CONTAINERNAME> /bin/bash`

### launch a command to the container
`docker exec -it <CONTAINERNAME> Rscript /ImputationSaver/ImputeData.R`

### copy files from the container to the host or vice versa
`docker cp <src-path> <container>:<dest-path>`
`docker cp <container>:<src-path> <local-dest-path>`

### A trabajar!
<img src="https://giphy.com/media/7NoNw4pMNTvgc/giphy.gif" width="80" height="80" />

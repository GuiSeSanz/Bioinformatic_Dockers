# Dockers

`docker build -t <IMAGENAME> .`

### Create a container and keep it running forever (detached mode)
`docker run -itd --name <CONTAINERNAME> <IMAGENAME> bash`

### Create a container and run it
`docker run -it <IMAGENAME> bash`

### Enter an existing and running container interactively
`docker exec -it <CONTAINERNAME> bash`

### Enter a stoped container
`docker start -ai <CONTAINERNAME> bash`

### Launch a command to the container
`docker exec -it <CONTAINERNAME> Rscript /ImputationSaver/ImputeData.R`

### Copy files from the container to the host or vice versa
`docker cp <src-path> <container>:<dest-path>`
`docker cp <container>:<src-path> <local-dest-path>`

### A trabajar!
<img src="https://media.giphy.com/media/7NoNw4pMNTvgc/giphy.gif" width="150" height="150" />

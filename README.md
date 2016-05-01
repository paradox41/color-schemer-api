# Color Schemer API

## Getting Started

### Docker

Docker is being used to manage the components of color schemer, this readme assumes you already have docker installed.

### Get the code

1. Clone this repository into some directory
2. Clone [color-schemer-frontend](https://github.com/paradox41/color-schemer-frontend) into the same directory. Follow its readme, or at least run cd into it and run gulp.

### Install

1. `docker-compose up`

This will build and start 4 docker containers: web, nginx, postgresql, and data.

If this is you first time running the containers, or you need to update the database/data, run the `alembic upgrade` command described below.

## Container commands

The following commands are to be run in the context of a container. You can accomplish this one of two ways.

1. By using docker-compose to run the command directly, `docker-compose run <container> <command>`
2. By using docker-compose to launch a `bash` shell within a container, and then running the command(s) in the shell.
```bash
docker-compose run --rm <container> bash
# a bash shell gets launched within that container
<command>
```

Note: Docker launches a new <container> instance when you use `docker-compose run`. The --rm flag is passed to tell docker-compose to remove the container instance once we are finished with it.

### To initialize the database schema

1. `docker-compose run --rm web color-schemer create`

### To update the database schema

1. `docker-compose run --rm web alembic upgrade head`

### SSL certificates

Follow the guide [here](https://serversforhackers.com/video/self-signed-ssl-certificates-for-development) and put them into `./certificates` with the following names:

`color-schemer.com.crt`
`color-schemer.com.key`

### To access the app

1. [Go to it](https://dev.color-schemer.com)

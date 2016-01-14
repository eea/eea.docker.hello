# Hello world Docker image

Hello world docker image to be used to test load-balancers,
cache servers, apache/ngnix, etc


## Simple run

    $ docker run --rm -p 80:80 eeacms/hello


## Run with Docker compose


### docker-compose.yml

    haproxy:
      image: eeacms/haproxy
      links:
      - webapp
      ports:
      - "80:80"
      - "1936:1936"

    webapp:
      image: eeacms/hello


### Scale and test

     $ docker-compose scale webapp=4 haproxy=1

Now go to: http://localhost

Check backends health at: http://admin:admin@localhost:1936

### Supported environment variables

You can override default running port inside container via

  * `PORT` Serve on this port instead of 80 (e.g. 8080)


    $ docker run --rm -e PORT=8080 -p 80:8080 eeacms/hello

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
      image: hello


### Scale and test

     $ docker-compose scale webapp=4 haproxy=1

Now go to: http://localhost

Check backends health at: http://admin:admin@localhost:1936

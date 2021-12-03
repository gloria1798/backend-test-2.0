# Microservices Templates

The template was structured following the principles defined by [clean architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/).

## Requirements
- Docker installed

## Instructions
Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the microservices will run under the following ports:
- ecommerce-service: 8081
- delivery-service: 8082 

Check the **.env.example** file to change these or any other params.
# Microservices Templates

The template was structured following the principles defined by [clean architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/).

Each service has his own database, but the schema, user, password params are the same for both.

## Requirements
- Docker installed

## Instructions
Copy **.env.example** to **.env**. It will be used as environment variables source.

Inside Docker/app folders of ecommerce-service and delivery-services:
Copy **.env.example** to **.env**. It will be used as environment variables source.

Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the microservices will run under the following ports:
- ecommerce-service: 8081
- delivery-service: 8082 

Check the **.env.example** file to change these or any other params.
# Enviame's Python Backend Test

This test requires the design and development of two communicated microservices: 
1 ecommerce marketplace system.
2 shipping & Tracking service.

The project is focused in the logistics aspect of a typical ecommerce process. Than means you should make assumptions in other processes like payment or billing.

## Tech requirements
You must choose one of the follow languajes + frameworks.
- Python + flask

You must use Docker with Compose to provide a portable containerized app. 
If Your Not familiar with Docker We already provide a template here.

## Before you begin

- Provide a **private GitHub repository** with your code and add the following users as collaborators: **@rolivagon @rsebjara @vmolina-enviame @vham**
- You must provide two containerized microservices with the proper instructions tu run the app.
- Be specially carful to test your app in a clean environment and from zero, **if we can't run It, your test will be discarded inmediately.** and It will be terrible.
- As a backend test is not requiered to provide any view, all of contrary we ecourage You to provide an API where We could test all the features.

In case of any technical questions [Contact Us](mailto:tech-test@enviame.io)

### User Stories

#### ecommerce microservice
1. As a "Marketplace Administrator" you may create, view, edit, delete and list "sellers". Each seller requires: name, short description and at least one "Seller Administrator User".
2. As a "Seller User" you may view and edit seller information, and You must add a warehouse address as a previous condition to sell a product.
3. As a "Seller User" you may create, view, edit, edit, delete and list "products". Each product requires at least: name, short description and quantity.
4. As an internet user, You may register by your self as a "Marketplace User". Each marketplace user requires at least: email and shipping_addres.
5. As a "Marketplace User", You may buy products of different sellers, Your purchase couldn't exceed the stock of a product, and immediately reduce the available stock of the products according your purchase. In case the purchase exceed the stock of a product, the transacction will not be accepted.
6. As a "Seller User", You may list and view your "buy orders". You may changue the order's status from "created" to "confirmed", and from "confirmed" to "dispatched". Each order must have: product sku, product quantity and delivery information. When you change an order to dispatched status, the ecommerce microservice notify the delivery microservice through delivery creation endpoint provided by the delivery microservice api.
7. As a "Marketplace User", You may "cancell" an order only if the status is different to "confirmed". In case an order is cancelled the available stock of the products must be increased.
8. As a "Marketplace Administrator", You may list, view and "cancell" orders.
9. As any kind of user you must see the current status of an onder. The posible statuses are: "created", "confirmed", "dispached" and "delivered". The "delivered" status is triggered by the delivery microservices trough a webhook. That means the ecommerce microservice must provide an authenticated endpoint what will be registered in other microservices to notify when an order is delivered (or any other delivery status of an oder)


#### delivery microservice

1. The delivery microservice must provide an authenticated API that allows create, view, edit and delete a delivery. The functionality to get the status history (tracking) of a delivery must provided as well.

- The contract to create a delivery could be like this example:
**request:**
```json
{
    "order":
    {
        "foreing_order_id": "order number provided by ecommerce microservice",
        "products": [{
                "sku": "unique id of product",
                "name": "product name",
                "qty": "product quantity"
            }]
    },
    "origin": {
        "address": "pickup address"
    },
    "destination": {
        "name": "customer name",
        "address": "customer address"
    }
}
```

**response:**
```json
{
    "order":
    {
        "foreing_order_id": "order number provided by ecommerce microservice",
        "products": [{
                "sku": "unique id of product",
                "name": "product name",
                "qty": "product quantity"
            }]
    },
    "origin": {
        "address": "pickup address"
    },
    "destination": {
        "name": "customer name",
        "address": "customer address"
    },
    "trackig_number": "provided by the delivery microservice",
    "status": "provided by the delivery microservice"
}
```

- The contract to get the delivery tracking history could be like this example:
**reequest:**
```json
{
    "foreing_order_id": "",
    "trackig_number": ""
}
```

**response:**
```json
{
    "trackig_number": "",
    "status": "",
    "tracking": [{
        "status": "",
        "date"
    }]
}
```

2. The posible statuses of a delivery are: **"READY_FOR_PICK_UP", "IN_ORIGIN", "IN_ROUTE_OF_DELIVERY", "NOT_DELIVERED", "DELIVERED".**
3. The delivery microservice must provide a mechanism to change the status of all orders each 30 seconds, following the next rules:
    - The order of the statuses are: "READY_FOR_PICK_UP" -> "IN_ORIGIN" -> "IN_ROUTE_OF_DELIVERY".
    - From "IN_ROUTE_OF_DELIVERY" there are 50% of probability to changue to "NOT_DELIVERED" or "DELIVERED" (randomly).
    - From "NOT_DELIVERED" the order return to "IN_ROUTE_OF_DELIVERY". 
    - The "DELIVERED" status is a final status.

4. The delivery microservice must provide service to register an external endpoint to being reciving notifications of changes in the status of an order (using webhooks). Each status must be notified only one time. 

## Aspects to be evaluated

- Functionality
- Testing
- Proper use of http responses
- Proper handling of errors and exceptions
- Documentation
- Software design
- Programming style
- Appropriate framework use

## Aspects to be ignored

- Visual design of the solution
- Deployment of the solution

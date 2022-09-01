# ecommerce-products-api

## Introduction
This projects provides an RestAPI which provides the list of products for an E-Commerce website. It also comes with various filter and sort options. 


## Installation
```
conda create -n products_api python=3.8
conda activate products_api
git clone https://gitlab.com/python-projects35/ecommerce-products-api.git
cd ecommerce-products-api/products
```
Make you have docker installed in your system
````
docker-compose up --build
````
If everything goes well you can see below message and then you are good to go ahead
````
Watching for file changes with StatReloader
web_run_1      | Performing system checks...
web_run_1      | 
web_run_1      | System check identified no issues (0 silenced).
web_run_1      | August 07, 2022 - 08:49:27
web_run_1      | Django version 4.1, using settings 'products_api.settings'
web_run_1      | Starting development server at http://0.0.0.0:8000/
web_run_1      | Quit the server with CONTROL-C.
````
## API endpoints available
Below endpoint gives all the products in ascending of price, vendor, category
````
GET /list/products
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 8,
        "product_name": "Hornby 2014 Catalogue",
        "vendor": "Hornby",
        "category": "Hobbies",
        "price": 5.49,
        "description": "Product Description Hornby 2014 Catalogue Box Contains 1 x one catalogue"
    }
]
````
 Filter options available on category, vendor, price
````
GET /list/products/?search=mobiles


[
    {
        "id": 5,
        "product_name": "Iphone 13",
        "vendor": "Apple",
        "category": "Mobiles",
        "price": 899.99,
        "description": "Apple's iPhone 13 features Super Retina XDR display with True Tone and an A15 Bionic chip"
    },
    {
        "id": 6,
        "product_name": "Iphone 13",
        "vendor": "Apple",
        "category": "Mobiles",
        "price": 899.99,
        "description": "Apple's iPhone 13 features Super Retina XDR display with True Tone and an A15 Bionic chip"
    }
]
````
## TechStack
Tech-stack used in this application
* Python
* Django, Django Rest Framework, Django filters
* SQLite3 (Database)
* Docker
* Conda environment

## Workflow Diagram

![Alt text](images/products_api_workflow.png?raw=true "Title")

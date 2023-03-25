Project setup

1. Create virtual environment and activate it
2. To install requirements from requirements.txt, run the following command
   1. pip install -r requirements.txt
3. To migrate database, run the following commands
   1. python manage.py makemigrations
   2. python manage.py migrate
4. To run the project, run the following command
   1. python manage.py runserver



Product API's

1. http://127.0.0.1:8000/product/ - To list all products
2. http://127.0.0.1:8000/product/{id}/ - To view a product
3. http://127.0.0.1:8000/product/ - To create a product
4. http://127.0.0.1:8000/product/{id} - To update a product
5. http://127.0.0.1:8000/product/{id} - To delete a product


Order API's

1. POST http://localhost:8000/order/ - To create an order
2. PUT http://localhost:8000/order/{order_id}/ - To update the status of an order
3. GET http://localhost:8000/order/ - List all orders
4. GET http://localhost:8000/order/{order_id}/ - Retrieve order details
5. GET http://localhost:8000/order?status={status_id}&currency={currency_id}
   status: {1: 'Order Placed', 2: 'Order Cancelled', 3: 'Delivered'}
   currency: {1: 'USD', 2: 'INR'}
6. GET http://localhost:8000/order?ordering=total_desc - Orders the queryset in ascending or descending order based on 'total' filed
   ordering: total_desc -> Orders the queryset in descending order 
   ordering: total_asc -> Orders the queryset in ascending order
7. GET http://localhost:8000/order?start_range=250&end_range=350 - filters queryset based on a range on 'total' field
8. 
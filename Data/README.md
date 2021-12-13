## NOTICE!

This file contains the datasets received by Kaggle. In fact, it had to be done using Airflow and Spark technologies by
pulling data sets over AWS S3. However, although I ran the downloadS3.py and uploadS3.py files without any errors, I
could not connect the datasets with AWS.

# DATA

This is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders
from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple
dimensions: from order status, price, payment and freight performance to customer location, product attributes and
finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng
coordinates.

## Customer Dataset

This dataset has information about the customer and its location. Use it to identify unique customers in the orders
dataset and to find the orders delivery location. At our system each order is assigned to a unique customerid. This
means that the same customer will get different ids for different orders. The purpose of having a customerunique_id on
the dataset is to allow you to identify customers that made repurchases at the store. Otherwise you would find that each
order had a different customer associated with.

## Geolocation Dataset

This dataset has information Brazilian zip codes and its lat/lng coordinates. Use it to plot maps and find distances
between sellers and customers.

## Order Items Dataset

This dataset includes data about the items purchased within each order.

## Payments Dataset

This dataset includes data about the orders payment options.

## Order Reviews Dataset

This dataset includes data about the reviews made by the customers.

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order. Once the customer
receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where he
can give a note for the purchase experience and write down some comments.

## Order Dataset

This is the core dataset. From each order you might find all other information.

## Products Dataset

This dataset includes data about the products sold by Olist.

## Sellers Dataset

This dataset includes data about the sellers that fulfilled orders made at Olist. Use it to find the seller location and
to identify which seller fulfilled each product.

## Product Category Name Translation

Translates the productcategoryname to english.
# Libraries which i can need
import pandas as pd
import numpy as np
import matplotlib as plt



# Reading all the files
raw_path = 'C:\\Users\\yunus\\OneDrive\\Masaüstü\\Brazillian ECommerce\\myprojectecommerce\\Data\\'
olist_customer = pd.read_csv(raw_path + 'olist_customers_dataset.csv')
olist_geolocation = pd.read_csv(raw_path + 'olist_geolocation_dataset.csv')
olist_orders = pd.read_csv(raw_path + 'olist_orders_dataset.csv')
olist_order_items = pd.read_csv(raw_path + 'olist_order_items_dataset.csv')
olist_order_payments = pd.read_csv(raw_path + 'olist_order_payments_dataset.csv')
olist_order_reviews = pd.read_csv(raw_path + 'olist_order_reviews_dataset.csv')
olist_products = pd.read_csv(raw_path + 'olist_products_dataset.csv')
olist_sellers = pd.read_csv(raw_path + 'olist_sellers_dataset.csv')

# Collections for each dataset
datasets = [olist_customer, olist_geolocation, olist_orders, olist_order_items, olist_order_payments,
            olist_order_reviews, olist_products, olist_sellers]
names = ['olist_customer', 'olist_geolocation', 'olist_orders', 'olist_order_items', 'olist_order_payments',
         'olist_order_reviews', 'olist_products', 'olist_sellers']


# Analyze datas

""" There are 9 data sets. By referencing these data sets according to the schema, 
we examine their connections with each other.
Below we see the first 5 and last 5 data of all datasets. """

print("Head of all data files")
for heads in datasets:
    print(heads.head())

print("Tail of all data fiels")
for tails in datasets:
    print(tails.tail())



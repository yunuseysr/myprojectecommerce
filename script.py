# Libraries which i can need
import pandas as pd


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

# Analyze data

""" There are 9 data sets. By referencing these data sets according to the schema, 
we examine their connections with each other.
Below we see the first 5 and last 5 data of all datasets. """

print("Head of all data files")
for heads in datasets:
    print(heads.head())

print("Tail of all data files")
for tails in datasets:
    print(tails.tail())

print("Columns of all data files")
for news in datasets:
    print(news.columns)

"""In the analyze phase, I examined what information the columns of the data sets were filled with. 
The columns that I will answer the question are firstly included in the orders_item, products and orders datasets.
As seen in the diagram, order_items is a dataset linked to both products and orders. 
If I can create a Merge operation DataFrame, I think I can handle the data more properly."""

# Merge data from data lake datasets.
merge_DataFrame = olist_order_items.merge(olist_orders, on='order_id').merge(
    olist_products[['product_id', 'product_category_name']], on='product_id').merge(olist_sellers, on='seller_id')

#print(merge_DataFrame.head())
#print(merge_DataFrame.tail())

# Info merge data frame
print(merge_DataFrame.info())


# Columns of merge data frame
print(merge_DataFrame.columns)
# Index(['order_id', 'order_item_id', ....], dtype='object')

"""The shipping_limit_date column in the orders_items dataset and the order_delivered_carrier_date column in the orders dataset caught my attention. 
If I connect the delivery time to the shipment with the delivery time of the transportation, I can get the misses.
"""


missing_DataFrame = merge_DataFrame.loc[
    merge_DataFrame.shipping_limit_date < merge_DataFrame.order_delivered_carrier_date]

#print(missing_DataFrame.head())
#print(missing_DataFrame.tail())
print(missing_DataFrame.info())

# Columns of merge data frame
print(missing_DataFrame.columns)
# Index(['order_id', 'order_item_id', ....], dtype='object')


groupBy_DataFrame = missing_DataFrame.groupby('order_status').count()
missed_sellers = missing_DataFrame['seller_id']

# Sellers which missed their orders' deadline to be delivered to a carrier
for seller in missed_sellers:
    print(seller)


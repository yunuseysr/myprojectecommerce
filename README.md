# My Project is myprojectecommerce
I can say that I have opened new sails in the field of data science. It was a project that I gained some experience in many different fields and enjoyed preparing.
It is the project in which Brazil's E-Commerce Public Datasets are processed by Olist. While preparing this project, I benefited from many educational channels and documents. I will give them one by one in the links section. Let me briefly talk about what these E-commerce datasets are.

## Explanation
"This is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This is real commercial data, it has been anonymized, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses."
## Data
* https://www.kaggle.com/olistbr/brazilian-ecommerce

## Data Schema
The data is divided in multiple datasets for better understanding and organization. Please refer to the following data schema when working with it:
![img.png](img.png)

## Main Objectives
1. Construct a mock production data lake that is replete with the
dataset schema above (using AWS S3 is a bonus).
2. Analyze and clean the datasets.
3. Write a Spark and Spark SQL job to join together tables answering
the question, "Which sellers missed their orders’ deadline to be
delivered to a carrier?" (using spark is an optional bonus)
4. Build the ETL pipeline using Airflow (using Airflow is an optional bonus)
that accomplishes the following:
   * Downloads data from an AWS S3 bucket (if you have used it for the mock)
   * Runs a python script job that cleans the downloaded data and
   writes it to another folder to be used by the next job.
   * Runs a Spark/Spark SQL job on the clean data producing a
   dataset of delivery deadline missing orders.
   * Upload the output dataset to the same S3 bucket (if you have used it
   for the mock) in a folder ready for use for higher-level analytics


## ToDo List

* Construct a data lake that is replete with dataset schema ✓
* Analyze and clean the datasets ✓
* Answer the question, "which sellers missed their orders" deadline to be delivered to a carrier?" ✓
* Build ETL Pipeline using Airflow
  * Upload tha datasets manually to AWS S3 ✓
  * Downloads data from an AWS S3 bucket
  * Run script to answer the question ✓
  * Run Spark/Spark SQL the data producing a dataset of delivery deadline missing orders
  * Upload the output to datasets to the same bucket 


## Libraries
* pandas (v1.2.4)
* boto3 (v.1.20.23)

## Used Technologies: (Optimal)
* AWS S3
  * https://aws.amazon.com/tr/
* Apache Airflow 
  * https://airflow.apache.org
* Apache Spark
  * https://spark.apache.org
  
## Links to References
* How to Read Data from S3 using Python ( BOTO3 ) API
  * https://www.youtube.com/watch?v=Expy4DjViy4
* AWS ETL - Configure AWS Data Pipeline from MySql and S3
  * https://www.youtube.com/watch?v=u8Mub3ytUMg
* Apache Spark'a Giriş
  * https://www.youtube.com/watch?v=rkyUubl4Wo0
* About Spark
  * https://github.com/kaplanbora/spark-talk

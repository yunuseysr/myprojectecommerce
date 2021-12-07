# myprojectecommerce
This dataset contains information about the customer and its location. You can use this dataset to identify unique customers in the order dataset and find the delivery location of orders. 


# TODO List

* Initialize Apache Airflow and Spark
* Construct diagram on Airflow
* Get data via Kaggle
* AWS Platform and S3

# Main Objectives

* Construct a mock production data lake that is replete with dataset schema
* Analyze and clean the datasets
* Write a Spark and Spark SQL job to join together tables answering the question, 
"which sellers missed their orders" deadline to be delivered to a carrier?
* Build the ETL pipeline using Airflow that accomplishes the following:
  * Downloads data from an AWS S3 bucket
  * Runs a python script job that cleans the downloaded data and writes it to another folder to be used by the next job.
  * Runs a Spark/Spark SQL job on the clean data producing a dataset of delivery deadline missing orders.
  * Upload the output dataset to the same S3 bucket in a folder for use for higher-level analytics.


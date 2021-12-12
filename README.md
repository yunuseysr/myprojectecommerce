# myprojectecommerce
This dataset contains information about the customer and its location. You can use this dataset to identify unique customers in the order dataset and find the delivery location of orders. 


# TODO List

* Initialize Apache Airflow and Spark
* Construct diagram on Airflow
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

# Used Techologies:
 FaQ
* AWS S3 üzerinden data çekimi yapmak için boto3 kütüphanesinden yararlandık. Kütüphane S3 üzerinde daha önce eklediğimi dataları çekmemizde ve düzenlemizde yararlı olacaktır. 
* Daha önceden S3 üzerinde verilerimizin yüklemesini sağlamadım, bu sebeple AWS S3 üzerinden çalışmalarım bitti.
* Brazillian ECommerce Projesine kadar her hangi bir platformda Airflow, Spark ve AWS S3 yapılarını kullanmadığım için internet üzerinde araştırmalar yaptım. 
* Bilgi edindiğim yerlerin linkini aşağıya bırakacağım.
* Verilen şemayı incelediğim de cevap istenilen soruya -> "Which seller missed their orders' deadline to be delivered to a carrier ?" göre merge işlemlerini yapmam gerekiyormuş.

# Links
* How to Read Data from S3 using Python ( BOTO3 ) API
  * https://www.youtube.com/watch?v=Expy4DjViy4
* AWS ETL - Configure AWS Data Pipeline from MySql and S3
  * https://www.youtube.com/watch?v=u8Mub3ytUMg
* Apache Spark'a Giriş
  * https://www.youtube.com/watch?v=rkyUubl4Wo0


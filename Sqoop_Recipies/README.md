# Sqoop 2 Recipies
The folder will be storing some Sqoop recipes. Though this is mostly command line based but I will be making Python Scripts to run things around. 

Installing Sqoop is not that easy but yes, if you came across error where you `sqoop2-too verify` is failing because of hadoop binaries not found, I recommend, going through [this](http://brianoneill.blogspot.com/2014/10/sqoop-1993-w-hadoop-2-installation.html); It is also a tutorial on how to install. I won't be going through installation of Sqoop.  

# What is Sqoop 2
Earlier Sqoop was a connector for transferring data between your RDBMS and Data Warehouse designed in Hadoop Ecosystem. Sqoop 2 is more of general data transfer like from MySQL to Kafka or ftp to hdfs. So basically it will act like ETL script which you don't have to make anymore -- life's good again.   

The data I am using here is from [Movie Lense](https://grouplens.org/datasets/movielens/). You can feed your MySQL data with this. I will be using MySQL but there are other RDBMS supported by Sqoop. You may try that as well.

    
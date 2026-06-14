# Sales Data Analysis Using Hadoop MapReduce

![Hadoop](https://img.shields.io/badge/Hadoop-3.3.6-yellow)
![Java](https://img.shields.io/badge/Java-1.8-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.3-green)

## Project Overview
This project performs Big Data analysis on real sales data using Apache Hadoop MapReduce. Instead of processing data on a single machine, Hadoop distributes the workload making it fast and efficient for large datasets with 2824 records processed.

---

## What Does This Project Do
- Takes a real Kaggle Sales Dataset with 2824 records
- Uploads it to HDFS which is Hadoop Distributed File System
- Processes it using Java MapReduce
- Displays results on a Flask Web Dashboard with Bar and Pie Charts

---

## System Architecture

    WINDOWS 10/11 with WSL2
    |
    +-- Ubuntu 24.04 LTS
        |
        +-- Hadoop 3.3.6
        |   |
        |   +-- HDFS (Storage Layer)
        |   |   +-- NameNode
        |   |   +-- DataNode
        |   |
        |   +-- YARN (Processing Layer)
        |       +-- ResourceManager
        |       +-- NodeManager
        |
        +-- Java MapReduce (Analysis)
        |   +-- SalesMapper.java
        |   +-- SalesReducer.java
        |   +-- SalesDriver.java
        |
        +-- Python Flask (Web Dashboard)
            +-- Bar Chart
            +-- Pie Chart

---

## Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| WSL2 Ubuntu | 24.04 LTS | Linux Environment on Windows |
| Apache Hadoop | 3.3.6 | Distributed Storage and Processing |
| Java JDK | 1.8.0_492 | MapReduce Programming |
| Python | 3.x | Backend Web Server |
| Flask | 3.1.3 | Web Framework |
| Chart.js | Latest | Interactive Charts |
| Kaggle Dataset | 2824 records | Real Sales Data |

---

## Project Structure

    sales_project/
    |
    +-- src/
    |   +-- SalesMapper.java        (Mapper Class)
    |   +-- SalesReducer.java       (Reducer Class)
    |   +-- SalesDriver.java        (Driver Class)
    |
    +-- hadoop_config/
    |   +-- core-site.xml           (HDFS URI Configuration)
    |   +-- hdfs-site.xml           (Replication Settings)
    |   +-- mapred-site.xml         (MapReduce Framework)
    |   +-- yarn-site.xml           (Resource Manager)
    |   +-- hadoop-env.sh           (Java Home for Hadoop)
    |
    +-- sales_data_samples.csv      (Kaggle Dataset)
    +-- results.txt                 (MapReduce Output)
    +-- app.py                      (Flask Web Dashboard)
    +-- README.md                   (Documentation)

---

## Dataset Information

| Field | Details |
|---|---|
| Source | Kaggle Sample Sales Data |
| Total Records | 2824 rows |
| File Size | 530782 bytes |
| Format | CSV |

### Columns Used
- ORDERNUMBER is the Order ID
- QUANTITYORDERED is the Units Sold
- PRICEEACH is the Price per Unit
- SALES is the Total Sales Amount
- PRODUCTLINE is the Product Category used for Analysis

---

## Hadoop Configuration Files

### core-site.xml
Sets HDFS address to localhost port 9000

### hdfs-site.xml
Sets replication factor to 1 for single node

### mapred-site.xml
Sets MapReduce framework to YARN and defines HADOOP_MAPRED_HOME path

### yarn-site.xml
Enables mapreduce_shuffle for NodeManager

### hadoop-env.sh
Sets JAVA_HOME for Hadoop to use correct Java version

---

## MapReduce Flow

    INPUT
    CSV File uploaded to HDFS
          |
          v
    MAPPER (SalesMapper.java)
    Reads each CSV line
    Extracts ProductLine and Sales value
    Emits key-value pair (ProductLine, Sales)
          |
          v
    SHUFFLE AND SORT
    Hadoop groups all same ProductLines together
    Classic Cars -> [2871, 1580, 1782]
    Vintage Cars -> [1234, 2600]
          |
          v
    REDUCER (SalesReducer.java)
    Sums up all Sales values per ProductLine
    Classic Cars -> 6233.0
    Vintage Cars -> 3834.0
          |
          v
    OUTPUT
    Results saved in HDFS at /sales_output/part-r-00000

---

## Results

| Product Line | Total Sales |
|---|---|
| Classic Cars | 6233 dollars |
| Vintage Cars | 3834 dollars |
| Planes | 2210 dollars |
| Motorcycles | 1963 dollars |
| Trucks and Buses | 1873 dollars |
| Ships | 1591 dollars |
| Trains | 550 dollars |
| TOTAL | 18254 dollars |

Classic Cars is the top selling product line.

---

## How to Run Step by Step

### Step 1 - Environment Setup
Open Ubuntu terminal and run these commands

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export HADOOP_HOME=/home/bilal-raza/hadoop
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_YARN_HOME=$HADOOP_HOME
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

### Step 2 - Start Hadoop

    sudo service ssh start
    start-dfs.sh
    start-yarn.sh
    jps

Expected output from jps command
- NameNode
- DataNode
- SecondaryNameNode
- ResourceManager
- NodeManager

### Step 3 - Upload Data to HDFS

    hdfs dfs -mkdir /sales_input
    hdfs dfs -put sales_data_samples.csv /sales_input/
    hdfs dfs -ls /sales_input/

### Step 4 - Compile Java Code

    cd src/
    javac -classpath $(hadoop classpath) -d . *.java
    jar -cvf SalesAnalysis.jar *.class

### Step 5 - Run MapReduce Job

    hadoop jar SalesAnalysis.jar SalesDriver /sales_input /sales_output

### Step 6 - View Results

    hdfs dfs -cat /sales_output/part-r-00000

### Step 7 - Start Flask Dashboard

    cd ~/sales_project
    python3 app.py

### Step 8 - Open Browser

    localhost:5000  for Sales Dashboard
    localhost:9870  for HDFS Monitor
    localhost:8088  for YARN Monitor

---

## Web Interfaces

| URL | Purpose |
|---|---|
| localhost:5000 | Sales Analysis Dashboard with Charts |
| localhost:9870 | HDFS File System Monitor |
| localhost:8088 | YARN Resource Manager and Job Monitor |

---

## HDFS Commands Reference

    hdfs dfs -ls /                              List root directory
    hdfs dfs -ls /sales_input/                 List input folder
    hdfs dfs -mkdir /sales_input               Create folder
    hdfs dfs -put file.csv /folder/            Upload file
    hdfs dfs -get /folder/file ~/              Download file
    hdfs dfs -cat /sales_output/part-r-00000   View results
    hdfs dfs -rm -r /sales_output              Delete output folder

---

## Author

Muhammad Bilal Raza
- GitHub: bilal-raza12
- University: Sir Syed University of Engineering and Technology
- Department: Computer Engineering Batch 2021F
- Project: Sales Data Analysis Using Hadoop MapReduce


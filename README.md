<div align="center">

# 📊 Sales Data Analysis Using Hadoop MapReduce

### Big Data Processing & Visualization Platform

[![Hadoop](https://img.shields.io/badge/Hadoop-3.3.6-yellow?style=for-the-badge&logo=apache)](https://hadoop.apache.org/)
[![Java](https://img.shields.io/badge/Java-1.8-orange?style=for-the-badge&logo=java)](https://www.java.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![WSL](https://img.shields.io/badge/WSL2-Ubuntu_24.04-purple?style=for-the-badge&logo=ubuntu)](https://ubuntu.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-bilal--raza12-black?style=for-the-badge&logo=github)](https://github.com/bilal-raza12)

---

> A complete Big Data solution that processes **2,824 sales records** using **Apache Hadoop MapReduce**
> and visualizes insights through an interactive **Flask Web Dashboard** with real-time charts.

[🚀 Quick Start](#-how-to-run-step-by-step) • [📊 Results](#-results) • [🛠️ Tech Stack](#-technologies-used) • [👨‍💻 Author](#-author)

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [What This Project Does](#-what-this-project-does)
- [System Architecture](#-system-architecture)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Dataset Information](#-dataset-information)
- [Hadoop Configuration](#-hadoop-configuration)
- [MapReduce Flow](#-mapreduce-flow)
- [Results](#-results)
- [How to Run](#-how-to-run-step-by-step)
- [Web Interfaces](#-web-interfaces)
- [HDFS Commands Reference](#-hdfs-commands-reference)
- [Author](#-author)

---

## 🎯 Project Overview

This project demonstrates how **Apache Hadoop MapReduce** can be used to process large-scale sales data efficiently. Traditional tools like Excel or Python struggle with massive datasets, but Hadoop distributes the workload across multiple nodes, making it blazing fast.

The project ingests a **real-world Kaggle Sales Dataset**, processes it through a custom **Java MapReduce pipeline**, and presents the insights through a **beautiful Flask Web Dashboard** featuring interactive Bar and Pie charts.

---

## 🧠 What This Project Does

| Step | Action | Tool Used |
|------|--------|-----------|
| 1 | Load real sales CSV dataset | Kaggle |
| 2 | Store data in distributed file system | HDFS |
| 3 | Process data using MapReduce | Java + Hadoop |
| 4 | Aggregate sales by product line | Reducer |
| 5 | Display results as interactive charts | Flask + Chart.js |

---

## 🏗️ System Architecture

    +----------------------------------------------------------+
    |                  WINDOWS 10/11                           |
    |                                                          |
    |   +--------------------------------------------------+   |
    |   |              WSL2 - Ubuntu 24.04                 |   |
    |   |                                                  |   |
    |   |   +--------------------+  +------------------+  |   |
    |   |   |   HADOOP 3.3.6     |  |   FLASK APP      |  |   |
    |   |   |                    |  |                  |  |   |
    |   |   |  +-------------+  |  |  +------------+  |  |   |
    |   |   |  |    HDFS     |  |  |  |  Bar Chart |  |  |   |
    |   |   |  |  NameNode   |  |  |  +------------+  |  |   |
    |   |   |  |  DataNode   |  |  |  +------------+  |  |   |
    |   |   |  +-------------+  |  |  |  Pie Chart |  |  |   |
    |   |   |                    |  |  +------------+  |  |   |
    |   |   |  +-------------+  |  |                  |  |   |
    |   |   |  |    YARN     |  |  |  localhost:5000   |  |   |
    |   |   |  | ResourceMgr |  |  +------------------+  |   |
    |   |   |  | NodeManager |  |                        |   |
    |   |   |  +-------------+  |                        |   |
    |   |   |                    |                        |   |
    |   |   |  +-------------+  |                        |   |
    |   |   |  |  MapReduce  |  |                        |   |
    |   |   |  |   Mapper    |  |                        |   |
    |   |   |  |   Reducer   |  |                        |   |
    |   |   |  |   Driver    |  |                        |   |
    |   |   |  +-------------+  |                        |   |
    |   |   +--------------------+                        |   |
    |   +--------------------------------------------------+   |
    +----------------------------------------------------------+

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| **Apache Hadoop** | 3.3.6 | Distributed Storage and Processing |
| **Java JDK** | 1.8.0_492 | MapReduce Programming Language |
| **Python** | 3.12.3 | Backend Web Server |
| **Flask** | 3.1.3 | Web Framework for Dashboard |
| **Chart.js** | Latest | Interactive Bar and Pie Charts |
| **WSL2 Ubuntu** | 24.04 LTS | Linux Environment on Windows |
| **HDFS** | 3.3.6 | Distributed File Storage |
| **YARN** | 3.3.6 | Resource Management and Job Scheduling |
| **Kaggle Dataset** | - | Real World Sales Data Source |

---

## 📁 Project Structure

    sales_project/
    |
    +-- src/                            Java MapReduce Source Code
    |   |
    |   +-- SalesMapper.java            Mapper Class
    |   |   Reads CSV lines
    |   |   Extracts ProductLine and Sales
    |   |   Emits key-value pairs
    |   |
    |   +-- SalesReducer.java           Reducer Class
    |   |   Groups values by ProductLine
    |   |   Sums up total sales
    |   |   Writes final output
    |   |
    |   +-- SalesDriver.java            Driver Class
    |       Configures the MapReduce job
    |       Sets input and output paths
    |       Connects Mapper and Reducer
    |
    +-- hadoop_config/                  Hadoop Configuration Files
    |   |
    |   +-- core-site.xml               HDFS URI set to localhost:9000
    |   +-- hdfs-site.xml               Replication factor set to 1
    |   +-- mapred-site.xml             MapReduce framework set to YARN
    |   +-- yarn-site.xml               NodeManager shuffle enabled
    |   +-- hadoop-env.sh               JAVA_HOME path for Hadoop
    |
    +-- sales_data_samples.csv          Kaggle Sales Dataset (2824 records)
    +-- results.txt                     MapReduce Output Results
    +-- app.py                          Flask Web Dashboard Application
    +-- README.md                       Project Documentation

---

## 📦 Dataset Information

| Property | Details |
|---|---|
| **Source** | Kaggle — Sample Sales Data |
| **Total Records** | 2,824 rows |
| **File Size** | 530,782 bytes (~530 KB) |
| **Format** | CSV (Comma Separated Values) |
| **HDFS Path** | /sales_input/sales_data_samples.csv |

### Key Columns

| Column | Description | Used In |
|---|---|---|
| ORDERNUMBER | Unique Order ID | Reference |
| QUANTITYORDERED | Units Sold | Reference |
| PRICEEACH | Price per Unit | Reference |
| SALES | Total Sale Amount | Reducer Input |
| PRODUCTLINE | Product Category | Mapper Key |
| COUNTRY | Customer Country | Reference |
| DEALSIZE | Size of the Deal | Reference |

---

## ⚙️ Hadoop Configuration

### core-site.xml
Sets the default HDFS filesystem URI

    fs.defaultFS = hdfs://localhost:9000

### hdfs-site.xml
Sets replication factor for single node cluster

    dfs.replication = 1

### mapred-site.xml
Configures MapReduce to run on YARN with correct paths

    mapreduce.framework.name = yarn
    yarn.app.mapreduce.am.env = HADOOP_MAPRED_HOME=/home/bilal-raza/hadoop
    mapreduce.map.env = HADOOP_MAPRED_HOME=/home/bilal-raza/hadoop
    mapreduce.reduce.env = HADOOP_MAPRED_HOME=/home/bilal-raza/hadoop

### yarn-site.xml
Enables MapReduce shuffle service on NodeManager

    yarn.nodemanager.aux-services = mapreduce_shuffle

### hadoop-env.sh
Sets Java home directory for Hadoop

    JAVA_HOME = /usr/lib/jvm/java-8-openjdk-amd64

---

## 🔄 MapReduce Flow

    +---------------------------+
    |      INPUT LAYER          |
    |  sales_data_samples.csv   |
    |  stored in HDFS           |
    |  /sales_input/            |
    +---------------------------+
                |
                v
    +---------------------------+
    |      MAPPER LAYER         |
    |  SalesMapper.java         |
    |                           |
    |  Input:                   |
    |  10107,30,95.7,Motorcycles|
    |                           |
    |  Processing:              |
    |  Extract ProductLine      |
    |  Extract Sales value      |
    |                           |
    |  Output:                  |
    |  (Motorcycles, 2871.0)    |
    |  (Classic Cars, 1580.0)   |
    +---------------------------+
                |
                v
    +---------------------------+
    |    SHUFFLE AND SORT       |
    |  Hadoop automatically     |
    |  groups same keys         |
    |                           |
    |  Classic Cars ->          |
    |  [1580, 2871, 1782, ...]  |
    |                           |
    |  Vintage Cars ->          |
    |  [1234, 2600, ...]        |
    +---------------------------+
                |
                v
    +---------------------------+
    |      REDUCER LAYER        |
    |  SalesReducer.java        |
    |                           |
    |  Input:                   |
    |  Classic Cars ->          |
    |  [1580, 2871, 1782]       |
    |                           |
    |  Processing:              |
    |  Sum all values           |
    |                           |
    |  Output:                  |
    |  Classic Cars -> 6233.0   |
    +---------------------------+
                |
                v
    +---------------------------+
    |      OUTPUT LAYER         |
    |  Saved in HDFS            |
    |  /sales_output/           |
    |  part-r-00000             |
    +---------------------------+

---

## 📊 Results

### MapReduce Statistics

| Metric | Value |
|---|---|
| Map Input Records | 2,824 |
| Map Output Records | 2,823 |
| Reduce Input Groups | 7 |
| Reduce Output Records | 7 |
| Total Bytes Read | 530,782 |
| Total Bytes Written | 123 |

### Sales Analysis Output

| Rank | Product Line | Total Sales | Share |
|---|---|---|---|
| 1st | Classic Cars | $6,233 | 34.2% |
| 2nd | Vintage Cars | $3,834 | 21.0% |
| 3rd | Planes | $2,210 | 12.1% |
| 4th | Motorcycles | $1,963 | 10.8% |
| 5th | Trucks and Buses | $1,873 | 10.3% |
| 6th | Ships | $1,591 | 8.7% |
| 7th | Trains | $550 | 3.0% |
| | **TOTAL** | **$18,254** | **100%** |

**Classic Cars is the top performing product line with 34.2% of total sales.**

---

## 🚀 How to Run Step by Step

### Prerequisites

- Windows 10 or 11 with WSL2 enabled
- Ubuntu 24.04 installed via WSL
- Java JDK 8 installed
- Apache Hadoop 3.3.6 installed
- Python 3.x with Flask installed

### Step 1 — Set Environment Variables

Open Ubuntu terminal and run

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export HADOOP_HOME=/home/bilal-raza/hadoop
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_YARN_HOME=$HADOOP_HOME
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

### Step 2 — Start Hadoop Services

    sudo service ssh start
    start-dfs.sh
    start-yarn.sh
    jps

Expected output from jps

    NameNode
    DataNode
    SecondaryNameNode
    ResourceManager
    NodeManager

### Step 3 — Upload Dataset to HDFS

    hdfs dfs -mkdir /sales_input
    hdfs dfs -put sales_data_samples.csv /sales_input/
    hdfs dfs -ls /sales_input/

### Step 4 — Compile Java MapReduce Code

    cd src/
    javac -classpath $(hadoop classpath) -d . *.java
    jar -cvf SalesAnalysis.jar *.class

### Step 5 — Run MapReduce Job

    hadoop jar SalesAnalysis.jar SalesDriver /sales_input /sales_output

### Step 6 — View Raw Results

    hdfs dfs -cat /sales_output/part-r-00000

### Step 7 — Get Results File

    hdfs dfs -get /sales_output/part-r-00000 ~/sales_project/results.txt

### Step 8 — Start Flask Dashboard

    cd ~/sales_project
    python3 app.py

### Step 9 — Open in Browser

    http://localhost:5000   Sales Analysis Dashboard
    http://localhost:9870   HDFS File Monitor
    http://localhost:8088   YARN Job Monitor

---

## 🌐 Web Interfaces

| Interface | URL | Description |
|---|---|---|
| Sales Dashboard | localhost:5000 | Interactive charts with Bar and Pie visualization |
| HDFS Monitor | localhost:9870 | View files stored in Hadoop file system |
| YARN Monitor | localhost:8088 | Track MapReduce job status and history |

---

## 📚 HDFS Commands Reference

    hdfs dfs -ls /                            List root directory
    hdfs dfs -ls /sales_input/               List input folder contents
    hdfs dfs -mkdir /folder                  Create new directory
    hdfs dfs -put localfile /hdfs/path       Upload file to HDFS
    hdfs dfs -get /hdfs/path ~/local         Download file from HDFS
    hdfs dfs -cat /sales_output/part-r-00000 View output results
    hdfs dfs -rm -r /sales_output            Delete output folder
    hdfs dfs -du -h /                        Check disk usage

---

## 👨‍💻 Author

**Muhammad Bilal Raza**

| Field | Details |
|---|---|
| GitHub | bilal-raza12 |
| University | Sir Syed University of Engineering and Technology |
| Department | Computer Engineering |
| Batch | 2021F |
| Project Title | Sales Data Analysis Using Hadoop MapReduce |

---

## 📄 License

This project is open source and available under the MIT License.

---

<div align="center">

**If you found this project helpful, please give it a star!**

Made with by Muhammad Bilal Raza

</div>

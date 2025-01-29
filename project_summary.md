# Smart Environmental Monitoring System Project


## Links
**GitHub Repository**: https://gitlab.com/eshaanramaul/smart-environmental-monitoring-system

**Youtube Video**: https://www.youtube.com/watch?v=RrDg5QunI60

## Introduction
This project involves monitoring environmental temperature and humidity using two DHT22 sensors. Data is collected by a simulated Raspberry Pi Pico W microcontroller running MicroPython and transmitted via Wi-Fi module to a Virtual Private Server (VPS) hosted on Azure. The backend, developed with Node.js, uses a REST API that processes data and stores it in an InfluxDB database. Nginx serves as the HTTP web server for handling API requests.




## System overview
1. **Data Generation**: The data is generated in the wokwi simulator using a raspberry pi pico W with two sensors measuring temperature and humidity data. The code is written in MicroPython

2. **Data Transmission**: The microcontroller sends HTTP POST request to the VM on which there is Nginx(v1.24.0) which handles the HTTP traffic to the servers API endpoint.

3. **Backend**: The Node.js receives and processes the data.

4. **Data Storage**: The processed data is then stored in InfluxDB which is a time series database which is used to handle time stamped data.

5. **Visualization**: I have used a dashboard in InfluxDB to visualise the stored data.




## Services Used

 **Virtual Private Server**: Azure virtual private server Azure VPS with specifications including [Standard B1s, 1 GiB RAM, VM architecture: x64].

 **Operating System**: Linux (ubuntu 24.04)

 **Backend**: Node.js v23

 **Database**: InfluxDB v2.7.10

 **HTTP Web Server**: Nginx v1.24.0

 **Data Generation**: Micropython code running on wokwi Raspberry Pi pico w


## Setup Details

1. **Raspberry Pi Pico W**:
    1. Used wokwi to create the prototype using two sensors, wires and module.
    2. Coded a micropython script to read data from sensor and send it to backend.

2. **Backend Setup**:
    1. Setup the Virtual Machine on Azure.
    2. Install Node.js to vps
    3. Install Nginx to vps
    4. Install Pm2 to keep backend running all the time.
    5. Configure Nginx to send requests to the Node.js backend.
    6. Develop a RESP API to handle data.

3. **Database Setup**:
   1. Install InfluxDB to vps
   2. Created a bucket named for storing sensor readings.
   3. Use the token to connect to the backend and handle the POST request

4. **Data Visualisation**
    1. Use the InfluxDB Dashboard to visualise data




## Operating Costs

**VPS Hosting**: Used student subscription



## Benefits of the System

**Scalable**: Sensors can be added easily and more data can be handled easily.

**Cost-Effective**: Using open source services and affordable cloud hosting service

**Real-Time Monitoring**: Updates are showed in real time

**Easy to maintain**: Modular design simplifies updates and troubleshooting.

**Security**: Used secure methods to protect and transmit data securely

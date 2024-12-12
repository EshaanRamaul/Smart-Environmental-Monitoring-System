wokwi link: https://wokwi.com/projects/415645179887571969

This project is a Smart Environmental Monitoring Sensor that shows the temperature and humidity in the surroundings using Tw o DHT22 sensors. The collected data is transferred from the microcontroller via Wi-fi module to a virtual machine hosted on Azure.  In the backend, there is a Node.js(NODEJS 23) environment which runs a REST API. The data is stored in an InfluxDB
(InfluxDB v2.7.10) bucket and then visualized using the Dashboard. 
HTTP Web server Nginx (v1.24.0)

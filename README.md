# bme280-exporter
provide a exporter to allow scarping of data of BME280 sensor data by prometheus

## Hardware precondition
Sensor is connected on i2c bus e.g. on Raspberry PI on adress 0x77

## Build and run the Container

Requires docker installed on the system you would like to build and run the container!

Build with 
`docker build -t bme280-exporter .`

check on what i2c device port BME280 is connected

`i2cdetect -y 1` 

and use it on docker run command to allow container to read from.


Run with 
`docker run --device /dev/i2c-1 -d -p 8000:8000 bme280-exporter`


## Scraping and visualization of the data

Insert the following target into you prometheus.yml. Make sure you insert the correct server IP and Port.

    scrape_configs:
    - job_name: 'prometheus'
        scrape_interval: 5s
        static_configs:
            - targets: ['localhost:9090']
    - job_name: 'bme280environment'
        scrape_interval: 30s
        static_configs:
            - targets: ['localhost:8000']

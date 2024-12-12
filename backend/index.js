require('dotenv').config(); // Load environment variables from .env
const express = require('express');
const bodyParser = require('body-parser');
const { InfluxDB, Point } = require('@influxdata/influxdb-client');

const app = express();

// Middleware
app.use(bodyParser.json());

// InfluxDB configuration using environment variables
const INFLUX_URL = process.env.INFLUX_URL;
const INFLUX_TOKEN = process.env.INFLUX_TOKEN;
const INFLUX_ORG = process.env.INFLUX_ORG;
const INFLUX_BUCKET = process.env.INFLUX_BUCKET;

const influxDB = new InfluxDB({ url: INFLUX_URL, token: INFLUX_TOKEN });
const writeApi = influxDB.getWriteApi(INFLUX_ORG, INFLUX_BUCKET);

writeApi.useDefaultTags({ location: 'final-project-vm' });

// API endpoint to receive data
app.post('/api/data', (req, res) => {
    const { sensor_id, temperature, humidity } = req.body;
    if (!sensor_id || temperature === undefined || humidity === undefined) {
        return res.status(400).send('Invalid data');
    }
    const point = new Point('sensor_data')
        .tag('sensor_id', sensor_id)
        .floatField('temperature', temperature)
        .floatField('humidity', humidity);

    writeApi.writePoint(point);
    writeApi.flush()
        .then(() => res.status(200).send('Data written successfully!'))
        .catch(err => res.status(500).send(`Failed to write data: ${err}`));
});

// Start server
const PORT = process.env.PORT || 3000; // Use PORT from .env or default to 3000
app.listen(PORT, () => {
    console.log(`Backend running on http://localhost:${PORT}`);
});

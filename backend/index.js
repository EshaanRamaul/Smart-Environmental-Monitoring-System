const express = require('express');
const bodyParser = require('body-parser');
const { InfluxDB, Point } = require('@influxdata/influxdb-client');

const app = express();

// Middleware
app.use(bodyParser.json());

// InfluxDB configuration
const INFLUX_URL = 'http://localhost:8086';
const INFLUX_TOKEN = 'zUzV5nzVBGg2VUNqf9oocP2pXPU--VvhAA2yra44jGEadf2EiSoTfoqfbrOigc6KCFeDCSeaWEQiK94Kc9GreQ==';
const INFLUX_ORG = 'LAB';
const INFLUX_BUCKET = 'Smart Environmental Monitor';

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
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Backend running on http://localhost:${PORT}`);
});

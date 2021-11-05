import express from 'express';
import { db } from './utils/db.js';
import bodyParser from 'body-parser';

import AnimalsRoutes from './routes/animals.js'

db();

const app = express();
const port = 5000;

app.use(bodyParser());

app.use('/', AnimalsRoutes);

app.get('/:name', (req, res) => {
    let { name } = req.params;
    res.send(`Hello ${name}`);
    // res.send('Hello' + name);
});

app.get('/', (req, res) => {
    res.send('Hello World !');
});

app.listen(port, () => {
    console.log(`Server started on http//localhost:${port} ...`);
});
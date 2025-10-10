const express = require('express');
const app = express();

const studentsRoute = require('./routes/students');

app.use('/students', studentsRoute);

app.get('/', (req, res) => {
    res.send({
    name: 'University API',
    version: '1.0.0',
    description: 'A simple API to fetch university student data.',
    endpoints: {
      root: 'GET /',
      allStudents: 'GET /students',
      student1: 'GET /students/s1'
    }
})
})

app.listen(3000);
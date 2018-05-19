const express = require('express');
const app = express();
const port = 5000;

app.get('/api/hello', (req, res) => {
    res.send({
        express: "Hello from express"
    });
});

const MongoClient = require('mongodb').MongoClient;
const mongoURI = "mongodb://localhost:27017/mydb";
MongoClient.connect(mongoURI, (error, db) => {
    if (error) throw error;
    console.log('Mongodb is now connected');
    const collection = db.collection('things');
    app.get('/api/getStateWiseCount', (req, res) => {
        collection.aggregate([{
            $group: {
                _id: '$state',
                count: {
                    $sum: 1
                }
            }
        }]).toArray(function (err, data) {
            res.send(
                data);
        });
    });
    app.get('/api/getYearWiseCount', (req, res) => {
        collection.aggregate([{
            $project: {
                year: {
                    $year: '$date'
                }
            }
        }, {
            $group: {
                _id: '$year',
                count: {
                    $sum: 1
                }
            }
        }]).toArray(function (err, data) {
            res.send(data)
        })
    });
});

app.listen(port, () => console.log(`listening on port ${port}`));

#!/usr/bin/node

url = process.argv[2];
file = process.argv[3];

const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        fs.writeFile(file, body, 'utf-8', (err) => {
        if (err) {
            console.error(err);
        }
        });
    }
    }
);


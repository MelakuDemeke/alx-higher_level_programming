#!/usr/bin/node

url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        const todos = JSON.parse(body);
        const completed = {};
        for (const todo of todos) {
            if (todo.completed) {
                if (completed[todo.userId] === undefined) {
                    completed[todo.userId] = 1;
                } else {
                    completed[todo.userId] += 1;
                }
            }
        }
        console.log(completed);
    }
});

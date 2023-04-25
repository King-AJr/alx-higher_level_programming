#!/usr/bin/node
/* print status code of a get request */
const request = require('request');

const args = process.argv.slice(2);
const url = args[0];
request.get(url).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
});

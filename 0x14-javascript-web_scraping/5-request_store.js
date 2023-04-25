#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */
const fs = require('fs');
const request = require('request');

const args = process.argv.slice(2);
request(args[0]).pipe(fs.createWriteStream(args[1]));

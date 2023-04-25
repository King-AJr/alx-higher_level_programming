#!/usr/bin/node
/* writing data to a file */
const fs = require('fs');

const args = process.argv.slice(2);
const filename = args[0];
const data = args[1];

fs.appendFile(filename, data, (err) => {
  if (err) {
    console.error(err);
  }
});

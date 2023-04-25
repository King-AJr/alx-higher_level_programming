#!/usr/bin/node
/* get file name and print file content */
const fs = require('fs');
const args = process.argv.slice(2);
const filename = args[0];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

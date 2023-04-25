#!/usr/bin/node
/* prints the title of a Star Wars movie
where the episode number matches a given integer */
const request = require('request');

const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

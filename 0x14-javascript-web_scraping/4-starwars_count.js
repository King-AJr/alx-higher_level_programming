#!/usr/bin/node
/* prints the number of movies where 
the character Wedge Antilles with 
character ID 18 is present*/
const request = require('request');

const args = process.argv.slice(2);
request(args[0], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});

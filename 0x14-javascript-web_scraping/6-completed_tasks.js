#!/usr/bin/node
/* computes the number of tasks completed by user id.*/
const request = require('request');

const args = process.argv.slice(2);
request(args[0], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    let completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});

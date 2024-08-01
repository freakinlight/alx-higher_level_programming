#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const tasksCompleted = {};
  body.forEach(task => {
    if (task.completed) {
      if (!tasksCompleted[task.userId]) {
        tasksCompleted[task.userId] = 0;
      }
      tasksCompleted[task.userId]++;
    }
  });
  console.log(tasksCompleted);
});

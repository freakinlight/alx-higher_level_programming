#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    return console.error('error:', error);
  }
  if (response.statusCode !== 200) {
    return console.log('Not Found');
  }
  console.log(body.title);
});

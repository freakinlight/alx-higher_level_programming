#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    return console.error('Error:', error);
  }
  if (response.statusCode !== 200) {
    return console.log('Failed to fetch data');
  }

  let count = 0;
  body.results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/18/`)) {
      count++;
    }
  });
  
  console.log(count);
});

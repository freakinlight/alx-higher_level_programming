#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const characters = body.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      console.log(charBody.name);
    });
  });
});

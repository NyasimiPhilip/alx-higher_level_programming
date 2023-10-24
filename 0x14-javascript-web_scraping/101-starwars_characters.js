#!/usr/bin/env node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./starwars_characters.js [Movie ID]');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    if (characters && characters.length > 0) {
      printCharacters(characters, 0);
    } else {
      console.log('No characters found for this movie.');
    }
  } else {
    console.error('Error:', `Status Code: ${response.statusCode}`);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    } else {
      console.error('Error:', `Status Code: ${response.statusCode}`);
    }

    printCharacters(characters, index + 1);
  });
}

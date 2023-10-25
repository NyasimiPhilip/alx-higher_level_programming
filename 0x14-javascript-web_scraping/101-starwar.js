#!/usr/bin/node
const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./starwars_characters.js [Movie ID]');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

axios.get(apiUrl)
  .then((response) => {
    const characters = response.data.characters;

    if (characters && characters.length > 0) {
      printCharacters(characters, 0);
    } else {
      console.log('No characters found for this movie.');
    }
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  axios.get(characters[index])
    .then((response) => {
      const characterData = response.data;
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    })
    .catch((error) => {
      console.error('Error:', error.message);
      printCharacters(characters, index + 1);
    });
}


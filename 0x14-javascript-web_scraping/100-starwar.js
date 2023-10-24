#!/usr/bin/env node
const axios = require('axios');
const process = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];

axios.get(url)
  .then((response) => {
    const data = response.data;

    if (movieId >= data.results.length) {
      console.log(`Invalid movie ID: ${movieId}`);
      return;
    }

    const characters = data.results[movieId].characters;

    characters.forEach((characterUrl) => {
      axios.get(characterUrl)
        .then((characterResponse) => {
          const characterData = characterResponse.data;
          console.log(characterData.name);
        })
        .catch((error) => {
          console.log(error.message);
        });
    });
  })
  .catch((error) => {
    console.log(error.message);
  });


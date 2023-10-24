#!/usr/bin/env node
const axios = require('axios');
const process = require('process');
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

axios.get(url)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.error(error.message);
  });

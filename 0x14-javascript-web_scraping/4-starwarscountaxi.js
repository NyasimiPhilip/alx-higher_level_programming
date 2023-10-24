#!/usr/bin/env node
const axios = require('axios');
const process = require('process');
const url = process.argv[2];

const charId = '18';

axios.get(url)
  .then(response => {
    const data = response.data;
    let charTotal = 0;

    data.results.forEach(item => {
      item.characters.forEach(film => {
        if (film.includes(charId)) {
          charTotal += 1;
        }
      });
    });

    console.log(charTotal);
  })
  .catch(error => {
    console.error(error.message);
  });

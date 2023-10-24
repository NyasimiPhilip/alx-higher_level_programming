#!/usr/bin/env node
const axios = require('axios');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

axios.get(url)
  .then(response => {
    fs.writeFile(filename, response.data, 'utf-8', err => {
      if (err) {
        console.log(err);
      } else {
        console.log(`Saved to ${filename}`);
      }
    });
  })
  .catch(error => {
    console.log(error.message);
  });


#!/usr/bin/env node
const axios = require('axios');
const process = require('process');

const url = process.argv[2];

axios.get(url)
  .then((response) => {
    const mydict = {};

    response.data.forEach((item) => {
      if (item.completed) {
        if (!mydict[item.userId]) {
          mydict[item.userId] = 1;
        } else {
          mydict[item.userId] += 1;
        }
      }
    });

    console.log(mydict);
  })
  .catch((error) => {
    console.log(error.message);
  });

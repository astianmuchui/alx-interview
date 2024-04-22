#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const uri = 'https://swapi-api.hbtn.io/api/films/' + arg;

request(uri, async (error, res, body) => {
  if (error) {
    console.log(error);
  }
  for (const char of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(char, (error, res, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});

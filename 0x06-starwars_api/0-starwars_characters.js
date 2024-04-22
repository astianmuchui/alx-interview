#!/usr/bin/node

const request = require('request');
const sys = require('process');
const url = 'https://swapi-api.alx-tools.com/api/films/' + sys.argv[1];
console.log(url);
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const results = data.results;
    for (let i = 0; i < results.length; i++) {
      console.log(results[i].name);
    }
  }
});

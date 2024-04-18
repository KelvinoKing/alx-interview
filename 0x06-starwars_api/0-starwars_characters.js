#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first positional argument passed is the Movie ID - example:
// 3 = “Return of the Jedi”
// Display one character name per line in the same order as the
// “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(res);
    }
  }
});

#!/usr/bin/node
/* script that prints all characters of a Star Wars movie: */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data);
      } else {
        reject(error);
      }
    });
  });
}

async function fetchData () {
  try {
    const filmData = await makeRequest(url);

    for (const character of filmData.characters) {
      try {
        const charData = await makeRequest(character);
        console.log(charData.name);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
}

fetchData();

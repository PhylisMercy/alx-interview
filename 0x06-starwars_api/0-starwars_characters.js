#!/usr/bin/node

const request = require('request');
const film = process.argv[2] + '/';

const endpoints = {
  people: 'https://swapi-api.hbtn.io/api/people/',
  planets: 'https://swapi-api.hbtn.io/api/planets/',
  films: 'https://swapi-api.hbtn.io/api/films/',
  species: 'https://swapi-api.hbtn.io/api/species/',
  vehicles: 'https://swapi-api.hbtn.io/api/vehicles/',
  starships: 'https://swapi-api.hbtn.io/api/starships/'
};

const url = endpoints.films + film;

const payload = {
  url: url,
  method: 'GET'
};

request(payload, async (err, res, data) => {
  if (err) return;

  data = JSON.parse(data);
  const characters = data.characters;

  const makePromise = (url) => {
    return new Promise(function (resolve, reject) {
      request(url, (err, res, data) => {
        if (err) reject(err);
        else resolve(data);
      });
    });
  };

  for (const character in characters) {
    const res = await makePromise(characters[character]);
    const data = JSON.parse(res);
    console.log(data.name);
  }
});

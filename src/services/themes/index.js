'use strict';

const service = require('feathers-sequelize');
const themes = require('./themes-model');
const hooks = require('./hooks');

class ThemesService {
  constructor() {
    this.themes = [];
  }

  find(params) {
    return Promise.resolve(this.themes);
  }

  create(data, params) {
    this.themes.push(data);

    return Promise.resolve(data);
  }
}

module.exports = function() {
  const app = this;

  const options = {
    Model: themes(app.get('sequelize')),
    paginate: {
      default: 5,
      max: 25
    }
  };

  // Initialize our service with any options it requires
  app.use('/themes', service(options));
  app.use('/themes', new ThemesService());

  app.service('themes').on('created', (theme) => {
    console.log('Created theme', theme);
  });

  // Get our initialize service to that we can bind hooks
  const themesService = app.service('/themes');

  // Set up our before hooks
  themesService.before(hooks.before);

  // Set up our after hooks
  themesService.after(hooks.after);
};

'use strict';

const themes = require('./themes');

const authentication = require('./authentication');
const user = require('./user');
const Sequelize = require('sequelize');

module.exports = function() {
  const app = this;

  const sequelize = new Sequelize(app.get('postgres'), {
    dialect: 'postgres'
  });

  app.set('sequelize', sequelize);

  app.configure(authentication);
  app.configure(user);
  app.configure(themes);
};

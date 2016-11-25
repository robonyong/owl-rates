// webpack.config.js
var webpack = require('webpack');

var path = require('path'),
  assets_path = path.join(__dirname, 'js'),
  bundle_path = path.join(__dirname, '../', 'app', 'static', 'js'),
  node_modules_dir = path.join(__dirname, 'node_modules');

console.log('DEV MODE:: Building assets in :',assets_path);

var deps = [
  //'react/dist/react-with-addons.min.js',
  //'react-bootstrap/dist/react-bootstrap.min.js',
  // 'underscore/underscore-min.js',
  'moment/min/moment.min.js',
  // 'jquery/dist/jquery.min.js'
];
//var react_addons_path = 'react/dist/react-with-addons.min.js';


var config = {
  context: path.resolve(assets_path),
  entry: path.resolve(assets_path, 'index.js'),
  output: {
    filename: 'app.js',
    path: path.resolve(bundle_path)
  },
  externals: {
    jQuery: 'var jQuery'
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.json'],
    root: path.resolve(assets_path),
    alias: {}
  },
  devtool: "eval",
  module: {
    loaders: [
      { test: /\.(js|jsx)$/,
        exclude: /(node_modules)/,
        include: [ path.resolve(assets_path) ],
        loader: "babel-loader"
      },
      { test: /\.json$/,
        include: /\.json$/,
        loader: "json-loader"
      }
    ],
    noParse: []
  }
  //plugins: [
    //new webpack.ProvidePlugin({
      //$: 'jquery',
      //jQuery: "jquery",
      //"window.jQuery": "jquery"
    //})
  //]
};

//Shortcut each major lib to it's min file!
deps.forEach(function (dep) {
  var depPath = path.resolve(node_modules_dir, dep);
  config.resolve.alias[dep.split(path.sep)[0]] = depPath;
  config.module.noParse.push(depPath);
});

//var depPath = path.resolve(
  //node_modules_dir,
  //react_addons_path
//);
//config.resolve.alias['react/addons'] = depPath;
//config.module.noParse.push(depPath);

console.log('aliasing', config.resolve.alias);
//console.log(config.module.noParse);


module.exports = config;
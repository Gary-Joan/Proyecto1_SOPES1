var express = require('express');
var router = express.Router();
const axios = require("axios");
/* GET home page. */
const servidorA ="http://146.148.51.151/items"
const servidorB ="http://146.148.51.151/items"
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
var cont=0;
router.get('/publiA', async function(req, res){
  cont= cont+1
  let res1 = await axios
  .get(servidorA)
  .catch(function (error) {
    console.log(error);
  });
  console.log(res1.data);
  var nombre_servidor = "Publicaciones Servidor A";
  res.render('publicaciones', {publicaciones: res1.data, nombre:nombre_servidor});

});
router.get('/publiB', async function(req, res){
  cont= cont+1
  let res1 = await axios
  .get(servidorB)
  .catch(function (error) {
    console.log(error);
  });
  console.log(res1.data);
  var nombre_servidor = "Publicaciones Servidor B";
  res.render('publicaciones', {publicaciones: res1.data, nombre:nombre_servidor});

});

router.get('/chart', function(req, res){
  cont= cont+1
  
  res.render('chart', {contador: cont});

});
module.exports = router;

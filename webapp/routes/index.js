var express = require('express');
var router = express.Router();
const axios = require("axios");
/* GET home page. */
const servidorA ="http://146.148.51.151"
const servidorB ="http://34.121.214.76"
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
var cont=0;
router.get('/publiA', async function(req, res){
  cont= cont+1
  let res1 = await axios
  .get(servidorA+"/items")
  .catch(function (error) {
    console.log(error);
  });

  var nombre_servidor = "Publicaciones Servidor A";
  res.render('publicaciones', {publicaciones: res1.data, nombre:nombre_servidor});

});
router.get('/publiB', async function(req, res){
  cont= cont+1
  let res1 = await axios
  .get(servidorB+"/items")
  .catch(function (error) {
    console.log(error);
  });
 
  var nombre_servidor = "Publicaciones Servidor B";
  res.render('publicaciones', {publicaciones: res1.data, nombre:nombre_servidor});

});

router.get('/chart', async function(req, res){
  cont= cont+1
  let infoservidor_A = await axios.get(servidorA+"/memoria").catch(function(error){console.log(error)});
  let infoservidor_B = await axios.get(servidorB+"/memoria").catch(function(error){console.log(error)});
  var RAM={
      "servidorA":100-infoservidor_A.data['Porcentaje Libre'],
      "servidorB":100-infoservidor_B.data['Porcentaje Libre'],
  }
  let inforservidor_A_cpu = await axios.get(servidorA+"/cpu").catch(function(error){console.log(error)});
  let inforservidor_B_cpu = await axios.get(servidorB+"/cpu").catch(function(error){console.log(error)});
  var cpuA= 100*((inforservidor_A_cpu.data['CPU']['total time']/inforservidor_A_cpu.data['CPU']['HZ'])/inforservidor_A_cpu.data['CPU']['seconds ']);
  var cpuB= 100*((inforservidor_B_cpu.data['CPU']['total time']/inforservidor_B_cpu.data['CPU']['HZ'])/inforservidor_B_cpu.data['CPU']['seconds ']);
  var CPU={
      "servidorA":cpuA,
      "servidorB":cpuB
  }
  res.render('chart', {ram: RAM, cpu: CPU});

});
module.exports = router;

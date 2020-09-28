import React from 'react';
import './App.css';
import Nav from './components/nav';
import Publicaciones from './components/publicaciones';
import Graficas from './components/graficas';

import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
function App() {
  return (
    
      <Router >
          <div className="App">
          <Nav />
          <Switch>
          <Route path="/" exact component={home}/>
          <Route path="/publi" component={Publicaciones} />
          <Route path="/grafica" component={Graficas} />
          </Switch>
      </div>
     </Router>
   
   
  );
}
 const home = () => (
   <div>
     <h1>Pagina principal</h1>
   </div>
 );
export default App;

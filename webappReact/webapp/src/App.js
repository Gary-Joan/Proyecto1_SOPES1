import React from 'react';
import './App.css';
import Nav from './components/nav';
import Publicaciones from './components/publicaciones';
import Graficas from './components/graficas';
import 'bootstrap/dist/css/bootstrap.min.css';
function App() {
  return (
    <div className="App">
     <Nav />
     <Publicaciones />
     <Graficas />

    </div>
  );
}

export default App;

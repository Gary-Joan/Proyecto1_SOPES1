import React,{useState,useEffect} from 'react';
import Dropdown from 'react-bootstrap/Dropdown'

function Publicaciones() {
  return (
    <div >
    <Dropdown>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        Dropdown Button
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
        
      </Dropdown.Menu>
    </Dropdown>
    </div>
  );
}

export default Publicaciones;

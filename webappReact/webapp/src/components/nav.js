import React from "react";
import "../App.css";
import { Link } from "react-router-dom";
function Nav() {
  const navstyle = {
    color: "white",
  };
  return (
    <nav>
      <h4>SOPES 1</h4>
      <ul className="nav-links">
        <Link style={navstyle} to="/publi">
          <li>Publicaciones</li>
        </Link>
        <Link style={navstyle} to="/grafica">
          <li>Graficas</li>
        </Link>
      </ul>
    </nav>
  );
}

export default Nav;

import React from "react";
import {Link} from "react-router-dom";
import './Styles.css';

function Navbar() {
  return (
    <nav id="Navbar" className="Bar">
      <ul>
        <Link className="Link" to="">
              <button> Home </button>
        </Link>
        <Link className="Link" to="/SteuerungStart">
              <button> SteuerungStart </button>
        </Link>
      </ul>
    </nav>
  );
}

export default Navbar;
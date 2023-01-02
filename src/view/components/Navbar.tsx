import React from "react";
import {Link} from "react-router-dom";
import './Styles.css';

function Navbar() {
  return (
    <nav className="Navbar">
      <ul>
        <li>
            <Link to="">
              <button> Home </button>
            </Link>
        </li>
        <li>
            <Link to="/SteuerungStart">
              <button> SteuerungStart </button>
            </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
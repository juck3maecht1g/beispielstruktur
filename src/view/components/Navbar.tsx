import React from "react";
import { BrowserRouter, Route, Link } from "react-router-dom";
import './Styles.css';

function Navbar() {
  return (
    <nav className="Navbar">
      <ul>
        <li>
            <Link className="Link" to="">Home</Link>
        </li>
        <li>
            <Link className="Link" to="/SteuerungStart">SteuerungStart</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
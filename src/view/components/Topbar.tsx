import React from "react";
import {Link} from "react-router-dom";
import './Styles.css';

function Topbar() {
  return (
    <nav id="Topbar" className="Bar">
      <ul>
        <Link className="Link" to="">
              <button> Back </button>
        </Link>
        <Link className="Link" to="/Burgermenü">
              <button> Burgermenü </button>
        </Link>
      </ul>
    </nav>
  );
}

export default Topbar;
import React from 'react';
import StartButtonFunction from '../../controller/tsx_ctrl/component_ctrl/StartButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function StartButton() {
    return (
        
        <Link to="/SteuerungStop">
              <button id="StartButton"className="Button" onClick={StartButtonFunction}>Start</button>
        </Link>
        
    );
}
import React from 'react';
import AbortButtonFunction from '../../controller/tsx_ctrl/component_ctrl/AbortButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function AbortButton() {
    return (
        <Link to="/SteuerungStart">
            <button id="AbortButton" className="Button" onClick={AbortButtonFunction}>Abort</button>
        </Link>
    );
}
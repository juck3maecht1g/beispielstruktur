import React from 'react';
import AbortButtonFunction from '../../controller/tsx_ctrl/component_ctrl/AbortButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function SavePositionButton() {
    return (
        <Link className="Link" to="/SteuerungStart">
            <button id="AbortButton" className="Button" onClick={AbortButtonFunction}>Abort</button>
        </Link>
    );
}
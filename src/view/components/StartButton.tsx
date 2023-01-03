import React from 'react';
import {StartButtonFunction, GetStartButtonInfo} from '../../controller/tsx_ctrl/component_ctrl/StartButtonFunction';
import ForFetchTest from '../../controller/tsx_ctrl/forFetchTest';
import './Styles.css';
import {Link} from "react-router-dom";

export function StartButton() {
    var name = GetStartButtonInfo();
    return (
        <Link to="/SteuerungStop">
              <button id="StartButton"className="Button" onClick={StartButtonFunction}>Start {name}</button>
        </Link>
            );
}

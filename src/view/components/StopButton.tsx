import React from 'react';
import StopButtonFunction from '../../controller/tsx_ctrl/component_ctrl/StopButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function StopButton() {
    return (
        <Link className="Link" to="/SteuerungStart">
            <button id="StopButton" className="Button" onClick={StopButtonFunction}>Stop</button>
        </Link>
    );
}
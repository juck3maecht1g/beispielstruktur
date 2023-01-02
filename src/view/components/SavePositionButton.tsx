import React from 'react';
import SavePositionButtonFunction from '../../controller/tsx_ctrl/component_ctrl/SavePositionButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function SavePositionButton() {
    return (
            <button id="SavePositionButton" className="Button" onClick={SavePositionButtonFunction}>SafePosition</button>
    );
}
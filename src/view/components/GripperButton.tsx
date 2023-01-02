import React from 'react';
import GripperButtonFunction from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";

export function GripperButton() {
    return (
            <button id="GripperButton" className="Button" onClick={GripperButtonFunction}>Gripper</button>
    );
}
import React from 'react';
import GripperButtonFunction from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunction';
import './Styles.css';
import {Link} from "react-router-dom";
import { GetGripperButtonInfo } from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunctions';

export function GripperButton() {
    let ips = GetGripperButtonInfo()
    return (
            <button id="GripperButton" className="Button" onClick={GripperButtonFunction}>Gripper   {ips}</button>
    );
}
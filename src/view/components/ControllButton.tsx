import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';
import { GripperButtonFunctionShort, GetGripperButtonInfo } from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunctions';

export function ControllButton() {
    let ips = GetGripperButtonInfo()
    
    return (
        <button id="ControllButton" className="Button" onClick={ControllButtonFunction}>Controll + {ips}</button>
    );
}
import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';
import { GripperButtonFunctionShort, GetGripperButtonInfo } from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunctions';

export function ControllButton() {
    let ips = GetGripperButtonInfo()
    
    return (
        <button className="ControllButton" onClick={GripperButtonFunctionShort}>Controll + {ips}</button>
    );
}
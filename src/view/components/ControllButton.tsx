import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';
import { GripperButtonFunctionShort, GetGripperButtonInfo } from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunctions';

export function ControllButton() {

    
    return (
        <button id="ControllButton" className="Button" onClick={ControllButtonFunction}>Controll</button>
    );
}
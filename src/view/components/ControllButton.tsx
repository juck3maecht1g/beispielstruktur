import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';

export function ControllButton() {
    return (
        <button id="ControllButton" className="Button" onClick={ControllButtonFunction}>Controll</button>
    );
}
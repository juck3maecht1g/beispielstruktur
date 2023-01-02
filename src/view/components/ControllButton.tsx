import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';

export function ControllButton() {
    return (
        <button className="ControllButton" onClick={ControllButtonFunction}>Controll</button>
    );
}
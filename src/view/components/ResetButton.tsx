import React from 'react';
import ResetButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ResetButtonFunction';
import './Styles.css';

export function ResetButton() {
    return (
        <button id="ResetButton" className="Button" onClick={ResetButtonFunction}>Reset</button>
    );
}
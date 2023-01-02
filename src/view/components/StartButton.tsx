import React from 'react';
import StartButtonFunction from '../../controller/tsx_ctrl/component_ctrl/StartButtonFunction';
import './Styles.css';

export function StartButton() {
    return (
        <button className="StartButton" onClick={StartButtonFunction}>Start</button>
    );
}
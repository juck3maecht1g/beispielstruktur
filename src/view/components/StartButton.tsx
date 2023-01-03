import React from 'react';
import {StartButtonFunction, GetStartButtonInfo} from '../../controller/tsx_ctrl/component_ctrl/StartButtonFunction';
import ForFetchTest from '../../controller/tsx_ctrl/forFetchTest';
import './Styles.css';

export function StartButton() {
    var name = GetStartButtonInfo();
    return (
        <button className="StartButton" onClick={StartButtonFunction}>{"start " + name}</button>
    );
}

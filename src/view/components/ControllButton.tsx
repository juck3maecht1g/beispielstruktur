import React from 'react';
import ControllButtonFunction from '../../controller/tsx_ctrl/component_ctrl/ControllButtonFunction';
import { GripperButtonFunctionShort, GetGripperButtonInfo } from '../../controller/tsx_ctrl/component_ctrl/GripperButtonFunctions';


export class ControllButton extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <button id="ControllButton" className="Button" onClick={ControllButtonFunction}>{this.props.name}</button>
        );
    }
}
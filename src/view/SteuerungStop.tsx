import React from 'react';
import {StopButton} from "./components/StopButton"
import {ControllButton} from "./components/ControllButton"
import {AbortButton} from "./components/AbortButton"
import { SavePositionButton } from './components/SavePositionButton';
import { GripperButton } from './components/GripperButton';
import './components/Styles.css';

function SteuerungStop() {
    return (
        <h1 className="Page">
            <StopButton></StopButton>
            <ControllButton></ControllButton>
            <AbortButton></AbortButton>
            <SavePositionButton></SavePositionButton>
            <GripperButton></GripperButton>
        </h1>
    );
}

export default SteuerungStop
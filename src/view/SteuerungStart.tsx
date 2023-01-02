import React from 'react';
import {StartButton} from "./components/StartButton"
import {ControllButton} from "./components/ControllButton"
import {ResetButton} from "./components/ResetButton"
import { SavePositionButton } from './components/SavePositionButton';
import { GripperButton } from './components/GripperButton';
import './components/Styles.css';

function SteuerungsStart() {
    return (
        <h1 className="Page">
            <div>
                <ControllButton></ControllButton>
                <ResetButton></ResetButton>
                <SavePositionButton></SavePositionButton>
                <StartButton></StartButton>
                <GripperButton></GripperButton>
            </div>
        </h1>
    );
}

export default SteuerungsStart
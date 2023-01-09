import React from 'react';
import './components/Styles.css';
import ChooseButton from './components/ChooseButton';

function Burgermenü() {
    let button = new ChooseButton();

    return (
        <h1>
            <ChooseButton name="hallo"/>
        </h1>
    );

}

export default Burgermenü
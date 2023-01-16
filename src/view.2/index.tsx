import React, { useEffect, useState } from "react";
import ReactDom from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "../view/Layout";
import Home from "../view/StartPage";
//import "../controllPage/controllPage";
import SteuerungStop from "../view/SteuerungStop";
import Burgermenü from "../view/BurgerMenü";

export default class App extends React.Component {
  state = {
    dta: ""
  }
  
  info() {
    
  }

  render() {
    return (
      <div>
        <button onClick={() => {
          fetch(
      "http://127.0.0.1:5000/about"
    ).then(response => response.json()).then(data => {
      console.log("success") 
      this.setState({dta: data})
      })}}>Cick me</button>
        {this.state.dta}
      </div>       
    );
  }
}


ReactDom.render(
    <App /> , document.getElementById("root"));
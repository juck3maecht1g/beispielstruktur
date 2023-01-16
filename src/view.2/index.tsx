import React from "react";
import ReactDom from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ControlPage from "./controlPage/ControllPage";
import ChooseRobotPage from "./choosePage/ChooseRobotPage";
import Layout from "./../view/Layout"
import ChooseFolderPage from "./chooseFolderPage/ChooseFolderPage";

export default class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Routes >
          <Route path="/" element={<Layout />}>
            <Route index element={<ChooseFolderPage />} />
            <Route path="ControlPage" element={<ControlPage />} />
            <Route path="ChoosePage" element={<ChooseRobotPage/>} />
          </Route>
        </Routes>
      </BrowserRouter>
    );
  }
}


ReactDom.render(
    <App /> , document.getElementById("root"));
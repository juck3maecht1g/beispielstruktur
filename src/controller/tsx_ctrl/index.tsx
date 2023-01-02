import React from "react";
import ReactDom from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./../../view/Layout";
import Home from "./../../view/StartPage";
import SteuerungsStart from "./../../view/SteuerungStart";
import SteuerungStop from "./../../view/SteuerungStop";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="SteuerungStart" element={<SteuerungsStart />} />
          <Route path="SteuerungStop" element={<SteuerungStop />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}


ReactDom.render(
    <App /> , document.getElementById("root"));
import React from "react";
import {Outlet} from "react-router-dom";
import Navbar from "./components/Navbar";
import Topbar from "./components/Topbar";

const Layout = () => {
  return (
    <>
      <Navbar />
      <Outlet/>
      <Topbar />
    </>
  );
};

export default Layout;
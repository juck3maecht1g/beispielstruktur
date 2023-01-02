import React from "react";
import ReactDom from "react-dom/client";
import ForFetchTest from "./forFetchTest";




const root = ReactDom.createRoot(
  document.getElementById('root') , HTMLElement
);
root.render(
  <div>
    <div> help</div>
    <ForFetchTest/>
  </div>
);
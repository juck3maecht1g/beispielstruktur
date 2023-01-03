import { json } from "react-router-dom"
import React, {useState, useEffect} from 'react'
const gripper_key = "open";

/**type FetchedData ={
  state: string;
  expName: string;
};
**/

export function GripperButtonFunctionShort() {
  
    const response = fetch("http://127.0.0.1:5000/gripper-cmd", {
      'method': 'POST',
       headers : {
        'Content-Type': 'application/json'
      },
      body : JSON.stringify(gripper_key)
      }).then(res => {
    
      if (res.ok) {
        console.log('response ok')
      } else {
        console.log('response not ok')
      }
    })
    
  console.log("yes")
      
}
  


  export function GetGripperButtonInfo() {
    
    var [ips, setIPs] = React.useState([])
        // fetch data
        useEffect(() => {
          fetch(
              "http://127.0.0.1:5000/gripper-info"
            ).then(response => response.json()).then(data => { setIPs(data);})
          
        }, [])
        console.log(ips)
        var a = "";
        ips.forEach(function (value) {
            a += value + ", ";
        })

      return a
  }

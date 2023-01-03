import { json } from "react-router-dom"
import React, {useState, useEffect} from 'react'
const start_key = "start";

/**type FetchedData ={
  state: string;
  expName: string;
};
**/

export function StartButtonFunction() {
  
    const response = fetch("http://127.0.0.1:5000/start-cmd", {
      'method': 'POST',
       headers : {
        'Content-Type': 'application/json'
      },
      body : JSON.stringify(start_key)
      }).then(res => {
    
      if (res.ok) {
        console.log('response ok')
      } else {
        console.log('response not ok')
      }
    })
    
  console.log("yes")
      
}
  


  export function GetStartButtonInfo() {
    
    var [name, setName] = React.useState(start_key)
        // fetch data
        useEffect(() => {
          fetch(
              "http://127.0.0.1:5000/start-info"
            ).then(response => response.json()).then(data => { setName(data);})
          
        }, [])
      return name
  }

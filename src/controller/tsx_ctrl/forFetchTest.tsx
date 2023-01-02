import React, {useState, useEffect} from 'react'

export function ForFetchTest() {
    let toLog= {}
    const [test, setTest] = useState({})

    useEffect(() => {
      // fetch data
      const dataFetch = async () => {
        const data = await (
          await fetch(
            "http://127.0.0.1:5000/commands"
          )
        ).json();
            console.log(data)
        // set state when the data received
        toLog = data
        console.log(toLog)
      };
  
      dataFetch();
    }, []);

    

    

  return (
    <div>
      loaded
      <button onClick={async () => {
      const response = await fetch("http://127.0.0.1:5000/post-data", {
        'method': 'POST',
        headers : {
          'Content-Type': 'application/json'
        },
        body : JSON.stringify('abc')
      })

      if (response.ok) {
        console.log('response ok')
      } else {
        console.log('response not ok')
      }
    }}>click me</button>
    </div>
  )
}

export default ForFetchTest

import React, {useState, useEffect} from 'react'

export function ForFetchTest() {

    const [test, setTest] = useState({})

    useEffect(() => {
        fetch("http://127.0.0.1:5000/").then(
            res => {
            res.json
            console.log(res)
            }
        ).then(
          response => {
          console.log('data: ' + response)
          setTest(response)
          console.log('test: ' + test)
          
        })
    }, [])

    

    

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

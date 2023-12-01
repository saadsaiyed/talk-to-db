import React, { useState, useEffect }  from 'react'
// import logo from './logo.svg';
import './App.css';

const App = () => {

  const [ data, setData ] = useState([{}])
  // call homepage api route and accept any json
  // data coming from that backend data route
  useEffect(() => {
    fetch("/api/home").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log("data from backend")
        console.log(JSON.stringify(data))
      }
    )
  }, [])

  return (
    <div> 
      <h1>Talk to DB App</h1>
      {(typeof data.home === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.home.map((h, i) => (
          <p key={i}>{h}</p>
        ))
      )}
    </div>
  )
}

export default App
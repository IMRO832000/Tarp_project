import React from "react";
import "./styles.css";
import Wallet from "./Wallet/Wallet";

export default function App() {
  return (
    <div className="App">
      <div className="header">
        <img className="logo" src="https://static.toiimg.com/thumb/77480569/India-Flag.jpg?width=1200&height=900" alt="logo"/>
      </div>
      <Wallet />

      <div className="footer">
        
        <br />
    
        <br />
        <p>
          <h1>Indian Voting System</h1>
          Contact: help@bchainify.com <br /> Phone: (+91)999999999
        </p>
      </div>
    </div>
  );
}

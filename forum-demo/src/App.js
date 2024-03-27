import './App.css';
import React, { useState } from 'react';
import HeaderWeb from './components/HeaderWeb';
import Login from './login/Login';


function App() {
  return (
    <div className="App">
      <HeaderWeb></HeaderWeb>
      <Login></Login>
    </div>
  );
}

export default App;

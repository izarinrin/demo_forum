import './App.css';
import React, { useState } from 'react';
import Login from './pages/login/Login';
import MainPage from './pages/MainPage';


function App() {
  return (
    <div className="App">
      <Login/>
      <MainPage/>
    </div>
  );
}

export default App;

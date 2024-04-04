import './App.css';
import React, { useState } from 'react';
import Login from './pages/login/Login';
import MainPage from './pages/MainPage';

const BASE_URL = 'http://localhost:8000/'

function App() {
  return (
    <div className="App">
      <Login/>
      <MainPage/>
    </div>
  );
}

export default App;

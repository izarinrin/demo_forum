import React from 'react'
import './Login.css'


function login() {
    const shoot = () => {
        alert("Test Button");
    }
    return (
        <div className='loginContainer' >
            Login to account
            <div>
                <input name="username" placeholder={'username'} />
            </div>
            <div>
                <input secureTextEntry= {true} name="password" placeholder={'password'} />
            </div>
            <div>
                <button onClick={shoot}>Login</button>
            </div>
        </div>
    )
}

export default login
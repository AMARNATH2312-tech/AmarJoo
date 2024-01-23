import React from 'react'
import SignUp from './SignUp';


const Login = () => {
  return (
    <div>
        <form>
            <label>Email</label>
            <br></br>
            <input type='text' placeholder='Enter the username'></input>
            <br></br>
            <label>Password</label>
            <br></br>
            <input type='text' placeholder='Enter the password'></input>
            <button></button>
        </form> 
        
    </div>
  )
}

export default Login
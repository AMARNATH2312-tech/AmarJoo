import React, { useState, useEffect } from "react";
import axios from "axios";

const Login = () => {
  // const [username, setUsername] = useState("");
  // const [password, setPassword] = useState("");

  const [login, setLogin] = useState({ username: "", password: "" });
  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(name);
    setLogin({ ...login, [name]: value });
  };

  // const handleusername = (e) => {
  //   console.log(e.target.name);
  //   console.log(e.target.value);
  //   setUsername(e.target.value);
  // };

  // const handlepassword = (e) => {
  //   console.log(e.target.value);

  //   setPassword(e.target.value);
  // };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("submit button is working...");
    const payload = {
      email: e.target.email.value,
      password: e.target.password.value,
    };
    axios
      .post("http://localhost:8080/", payload, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => console.log(res))
      .catch((error) => console.log(error));
  };
  return (
    <div>
      <form onSubmit={(e) => handleSubmit(e)}>
        <label>Email</label>
        <br></br>
        <input
          onChange={handleChange}
          name="email"
          type="email"
          value={login.email}
          placeholder="Enter the username"
        ></input>
        <br></br>
        <label>Password</label>
        <br></br>
        <input
          onChange={handleChange}
          type="text"
          value={login.password}
          name="password"
          placeholder="Enter the password"
        ></input>
        <br></br>
        <button type="submit">Login</button>
      </form>
      
    </div>
  );
};

export default Login;

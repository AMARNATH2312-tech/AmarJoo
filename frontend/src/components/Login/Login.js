import AccountBoxIcon from "@mui/icons-material/AccountBox";
import React, { useEffect, useState } from "react";
import "./Login.css";
import axios from "axios";
import { useNavigate } from "react-router";

export default function Login() {
  const [login, setLogin] = useState({ email: "", password: "" });
  const navigate = useNavigate();
  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(name);
    setLogin({ ...login, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("submit button is working...");
    const payload = {
      email: e.target.email.value,
      password: e.target.password.value,
    };
    axios
      .post("http://localhost:8080/", payload)
      .then((res) => {
        console.log(res);
        // window.location.pathname = "/dashboard";
        navigate("/dashboard");
      })
      .catch((error) => console.log(error));
  };
  return (
    <div className="outer_container">
      <form onSubmit={(e) => handleSubmit(e)} className="wrapper">
        <h2>LOGIN</h2>
        <section className="group">
          <input
            onChange={handleChange}
            type="text"
            size="30"
            className="input"
            name="email"
            required
            value={login.email}
          />
          <label htmlFor="email" className="label">
            Email
          </label>
        </section>
        <section className="group">
          <input
            onChange={handleChange}
            type="password"
            minLength="8"
            className="input"
            name="password"
            required
            value={login.password}
          />
          <label htmlFor="password" className="label">
            Password
          </label>
        </section>
        <button type="submit" className="btn">
          LOGIN
        </button>
        <span className="footer"></span>
      </form>
    </div>
  );
}

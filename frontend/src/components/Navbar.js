import React, { useEffect, useState } from "react";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import PersonPinIcon from "@mui/icons-material/PersonPin";
import { Link } from "react-router-dom";
import "./Navbar.css";

const roomies = [
  "Sabari",
  "Susi",
  "Amar",
  "Vicky",
  "Raja Nidhi",
  "Keshav",
  "Any one",
];

export default function Navbar() {
  const [cleaner, setCleaner] = useState(0);
  useEffect(() => {
    const currentDate = new Date();
    const dayOfWeek = currentDate.getDay();
    setCleaner(dayOfWeek);
  }, []);
  return (
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          {/* Navbar */}
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div id="scroll-container">
            <div id="scroll-text">Today kuppa poruki {roomies[cleaner]}</div>
          </div>
          <div className="row">
            <div className="col mr-1">
              <PersonPinIcon />
            </div>
            <div className="col ">
              <Link to={"/"}>
                <ExitToAppIcon />
              </Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}

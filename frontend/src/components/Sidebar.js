import React, { useEffect } from "react";
import { useState } from "react";
import ElectricBoltIcon from "@mui/icons-material/ElectricBolt";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";
import DashboardIcon from "@mui/icons-material/Dashboard";
import AccountBoxIcon from "@mui/icons-material/AccountBox";
import SettingsIcon from "@mui/icons-material/Settings";
import ContactsIcon from "@mui/icons-material/Contacts";
import DesignServicesIcon from "@mui/icons-material/DesignServices";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import { Link } from "react-router-dom";
import { AiFillThunderbolt } from "react-icons/ai";
import "./Sidebar.css";

export default function Sidebar(props) {
  const { open, setOPen } = props;
  const [active, setActive] = useState(0);
  const [pathname, setPathName] = useState(null);

  useEffect(() => {
    console.log(window.location.pathname);
    setPathName(window.location.pathname);
  }, [active]);
  const Menus = [
    {
      title: "Dashboard",
      src: <DashboardIcon />,
      path: "/dashboard",
    },
    {
      title: "Admin",
      src: <AccountBoxIcon />,
      path: "/admin",
    },
  ];
  return (
    <>
      <div
        className="text-white"
        style={{
          width: open ? "4%" : "20%",
          height: "100vh",
          backgroundColor: "midnightblue",
          transition: "width 0.3s ease-in-out, margin 0.3s ease-in-out",
        }}
      >
        <div className="mt-2">
          <div
            className=""
            style={{
              padding: "8px",
              marginTop: "-5px",
              margin: "5px",
              textAlign: open ? "center" : "",
              //   transform: open ? "rotateZ(360deg)" : "",
            }}
          >
            <ElectricBoltIcon />
            {!open && (
              <span className="" style={{ marginLeft: "20px" }}>
                Roomies
              </span>
            )}
          </div>
          <div
            style={{
              marginTop: "5%",
              transition: "width 0.3s ease-in-out", // Add transition property for both width and margin
            }}
          >
            {Menus.map((item, index) => {
              return (
                <div
                  onClick={() => {
                    setActive(index);
                  }}
                  className=""
                  style={{
                    padding: "8px",
                    margin: "5px",
                    background: item.path === pathname ? "#5c5cb8" : "",
                    cursor: "pointer",
                    borderRadius: "5px",
                    textAlign: open ? "center" : "",
                    transition: "width 0.3s ease-in-out",
                  }}
                >
                  <Link
                    to={item.path}
                    style={{
                      textDecoration: "none",
                      color: "white",
                      display: "flex",
                      alignItems: "center",
                      width: "100%",
                    }}
                  >
                    <span>{item.src}</span>
                    {!open && (
                      <span className="" style={{ marginLeft: "20px" }}>
                        {item.title}
                      </span>
                    )}
                  </Link>
                </div>
              );
            })}
          </div>
        </div>
      </div>
      <div
        style={{
          width: "23px",
          height: "23px",
          position: "absolute",
          textAlign: "center",
          margin: open ? "1.4% 0% 0% 3%" : "1.4% 0% 0% 19%",
          color: "midnightblue",
          background: "white",
          borderRadius: "50%",
          border: "1px solid midnightblue",
          cursor: "pointer",
          transition: "margin 0.3s ease-in-out",
          zIndex: 2,
        }}
        onClick={() => {
          setOPen(!open);
        }}
      >
        <ArrowBackIosNewIcon
          className=""
          style={{
            fontSize: "14px",
            textAlign: "center",
            marginTop: "-30%",
            transform: open ? "rotateZ(180deg)" : "",
          }}
        />
      </div>
    </>
  );
}

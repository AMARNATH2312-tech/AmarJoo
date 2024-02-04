import React, { useState } from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
const Layout = ({ children }) => {
  const [open, setOPen] = useState(false);
  return (
    <>
      <div className="d-flex">
        <Sidebar open={open} setOPen={setOPen} />
        <div
          className="text-center"
          style={{ width: open ? "96%" : "80%", height: "100vh" }}
        >
          <Navbar />
          <div className="content">{children}</div>
        </div>
      </div>
    </>
  );
};

export default Layout;

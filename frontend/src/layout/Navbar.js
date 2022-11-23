import React from "react";
import { Menubar } from "primereact/menubar";
// import Logo from "../assets/images/logo.png";

import "../styles/Navbar.css";

import { Link } from "react-router-dom";

const Navbar = () => {
  const start = (
    <>
      <Link to="/">
        <img
          alt="logo"
          src="assets/images/logo.png"
          onError={(e) =>
            (e.target.src =
              "https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png")
          }
          height="40"
          className="mr-2 mt-3"
        ></img>
        <h4 style={{ float: "right", color: "skyblue" }}>Optimisation Project</h4>
      </Link>
    </>
  );
  const end = (
    <>
      <a href="https://github.com/MohamedAmineBenAmmar/Numerical-Analysis-Project" target="_blank">
        <i className="pi pi-github mr-5" style={{ fontSize: "1.5em" }}></i>
      </a>
    </>
  );

  return (
    <div>
      <div className="card">
        <Menubar model={[]} start={start} end={end} className="navbar" />
      </div>
    </div>
  );
};

export default Navbar;
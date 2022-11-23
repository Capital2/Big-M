import React from "react";
import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Footer from "./Footer";

export default function AppLayout() {
  return (
    <div className="App w-auto">
      <div className="App-header">
        <Navbar />
      </div>
      <div className="App-content">
        <Outlet />
      </div>
      <div className="App-footer">
        <Footer />
      </div>
    </div>
  );
}

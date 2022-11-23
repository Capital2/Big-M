import React from "react";
import { Button } from 'primereact/button'
import { useNavigate } from 'react-router-dom'

export default function Panel() {
  const navigate = useNavigate()
  const handleRedirection = () => {
    navigate('/BigM')
  }
  const handleRedirectionYoutube = () => {
    window.open('https://youtu.be/upgpVkAkFkQ', '_blank');
  }
  return (
    <div className="grid grid-nogutter surface-0 text-800">
      <div className="col-12 md:col-6 p-6 text-center md:text-left flex align-items-center ">
        <section>
          <span className="block text-5xl font-bold mb-1">
            Big M Method Calculator
          </span>
          <div className="text-6xl text-primary font-bold mb-3">
            your visitors deserve to see
          </div>
          <p className="mt-0 mb-4 text-700 line-height-3">
          Solve your linear programming exercises with the big M method calculator online automatically and easily with our online calculator.
          </p>

          <Button
            label="Learn More"
            type="button"
            className="mr-3 p-button-raised"
            onClick={handleRedirectionYoutube}
          />
          <Button
            label="Live Demo"
            type="button"
            className="p-button-outlined"
            onClick={handleRedirection}
          />
        </section>
      </div>
      <div className="col-12 md:col-6 overflow-hidden">
        <img
          src="/assets/images/hero-1.jpg"
          alt="hero-1"
          className="md:ml-auto block md:h-full"
          style={{ clipPath: "polygon(8% 0, 100% 0%, 100% 100%, 0 100%)" }}
        />
      </div>
    </div>
  );
}

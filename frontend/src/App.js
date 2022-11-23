import Router from "./router";

import "./App.css";
import "primereact/resources/themes/lara-light-indigo/theme.css"; //theme
import "primereact/resources/primereact.min.css"; //core css
import "primeicons/primeicons.css"; //icons
import 'primeflex/primeflex.css';

import PrimeReact from "primereact/api";

function App() {
  PrimeReact.ripple = true;
  return <Router />;
}

export default App;

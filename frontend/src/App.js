import './App.css';
import AppLayout from './layout/AppLayout';

import Footer from './layout/Footer';
import Navbar from './layout/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <AppLayout/>
      <Footer/>
      
    </div>
  );
}

export default App;

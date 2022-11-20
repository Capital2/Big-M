import './App.css';
import StatCellList from './components/StatsCellList';
import Footer from './layout/Footer';
import Navbar from './layout/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Footer/>
      <StatCellList/>
    </div>
  );
}

export default App;

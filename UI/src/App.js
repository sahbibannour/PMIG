import logo from './logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          DATA MIGRATION SOLUTION.
        </p>
        <br/>
        <button type="button" className="button">New Project</button>
        <br/>
        
        <button type="file" className="button">Open Project</button>
       
        
      </header>
    </div>
  );
}

export default App;

import './App.css';
import Login from './Login';
import SignUp from './SignUp';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <p>Welcome to Lazy boys Website</p>
        <Router>
          <Routes>
            <Route path="" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </Router>

      </header>
    </div>
  );
}

export default App;

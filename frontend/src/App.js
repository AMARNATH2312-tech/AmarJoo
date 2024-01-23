import logo from './logo.svg';
import './App.css';
import Login from './Login';
import SignUp from './SignUp';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {

  const MyComponent = ({ match }) => {
    console.log(match.params);  // Access URL parameters
    console.log(match.path);    // Access the pattern that the route matched
    console.log(match.url);     // Access the matched portion of the URL
  
    return (
      <Login></Login>
    );
  };

  const MyComponent1 = ({ location }) => {
    console.log(location.pathname);  // Access the current URL path
    console.log(location.search);    // Access the query string
    console.log(location.state);     // Access additional state information
  
    return (
      <SignUp></SignUp>
    );
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <Router>
          <Routes>
            <Route path="/example" component={MyComponent} />
            <Route path="/example/:id" component={MyComponent1} />
          </Routes>
        </Router>

      </header>
    </div>
  );
}

export default App;

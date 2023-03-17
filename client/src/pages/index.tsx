import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
// import Home from './home';
import NavigationMap from './navigation/Navigation';

function App() {
  return (
    <Router>
      
        <Routes>
          {/* <Route index path="/" element={<Home />} /> */}
          <Route index path="/" element={<NavigationMap  />} />
        </Routes>
   
    </Router>
  );
}

export default App;

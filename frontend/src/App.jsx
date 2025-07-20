import './App.css'

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Hoodie from "./pages/Hoodie";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        {/* dynamic route for each hoodie by id */}
        <Route path="/hoodie/:id" element={<Hoodie />} />
      </Routes>
    </Router>
  );
}

export default App

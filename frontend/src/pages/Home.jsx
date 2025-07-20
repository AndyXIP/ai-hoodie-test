// src/pages/Home.jsx

import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import HoodieCard from "../components/HoodieCard";

export default function Home() {
  const [hoodies, setHoodies] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/hoodies") // or your deployed backend URL
      .then((res) => res.json())
      .then(setHoodies)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>All Hoodies</h1>
      <div style={{ display: "flex", flexWrap: "wrap" }}>
        {hoodies.map((hoodie) => (
          <Link key={hoodie.id} to={`/hoodie/${hoodie.id}`} style={{ margin: 10 }}>
            <HoodieCard hoodie={hoodie} />
          </Link>
        ))}
      </div>
    </div>
  );
}

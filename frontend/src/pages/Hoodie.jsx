// src/pages/Hoodie.jsx

import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Hoodie() {
  const { id } = useParams();
  const [hoodie, setHoodie] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/hoodies/${id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Not found");
        return res.json();
      })
      .then(setHoodie)
      .catch(() => setHoodie(null));
  }, [id]);

  if (hoodie === null) return <p>Loading...</p>;
  if (!hoodie) return <p>Hoodie not found!</p>;

  return (
    <div>
      <h2>{hoodie.name}</h2>
      <img src={hoodie.image_url} alt={hoodie.name} style={{ maxWidth: "300px" }} />
      <p>{hoodie.description}</p>
    </div>
  );
}
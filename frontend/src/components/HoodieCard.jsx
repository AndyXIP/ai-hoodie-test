// src/components/HoodieCard.jsx

export default function HoodieCard({ hoodie }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: 10, width: 150 }}>
      <img src={hoodie.imageUrl} alt={hoodie.name} style={{ width: "100%" }} />
      <h3>{hoodie.name}</h3>
    </div>
  );
}

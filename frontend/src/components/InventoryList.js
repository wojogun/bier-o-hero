import React, { useState, useEffect } from "react";

function InventoryList() {
  const [inventory, setInventory] = useState([]);
  const [error, setError] = useState(null);

  // API URL mit HTTPS für das inventory-service
  const API_URL = "https://inventory-service.bierohero/inventory/";

  useEffect(() => {
    fetchInventory();
  }, []);

  const fetchInventory = async () => {
    try {
      const response = await fetch(API_URL);

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setInventory(data);
    } catch (err) {
      setError(`Failed to fetch inventory: ${err.message}`);
      console.error("Error fetching inventory:", err);
    }
  };

  return (
    <div>
      <h2>Inventory List</h2>
      {error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : (
        <ul>
          {inventory.map((item) => (
            <li key={item.id}>
              <strong>{item.product_name}</strong>: {item.stock} units available
              (Purchase Price: {item.purchase_price}, Sale Price: {item.sale_price})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default InventoryList;

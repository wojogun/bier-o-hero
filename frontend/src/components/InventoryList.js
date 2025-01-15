import React, { useState, useEffect } from "react";

function InventoryList() {
  const [inventory, setInventory] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8001/inventory/")
      .then((response) => response.json())
      .then((data) => setInventory(data));
  }, []);

  return (
    <div>
      <h2>Inventory</h2>
      <ul>
        {inventory.map((item) => (
          <li key={item.id}>
            {item.product_name}: {item.stock} units available
          </li>
        ))}
      </ul>
    </div>
  );
}

export default InventoryList;

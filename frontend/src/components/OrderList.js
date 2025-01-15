import React, { useState, useEffect } from "react";

function OrderList() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/orders/")
      .then((response) => response.json())
      .then((data) => setOrders(data));
  }, []);

  return (
    <div>
      <h2>Orders</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            {order.customer_name} ordered {order.product_name} ({order.quantity})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default OrderList;

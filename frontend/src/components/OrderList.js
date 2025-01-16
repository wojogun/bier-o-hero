import React, { useState, useEffect } from "react";

function OrderList() {
  const [orders, setOrders] = useState([]);
  const [newOrder, setNewOrder] = useState({
    customer_name: "",
    customer_email: "", // Email-Adresse hinzugefügt
    customer_address: "",
    customer_zipcode: "",
    customer_city: "",
    contents: [{ product_name: "", quantity: 1 }],
  });
  const [status, setStatus] = useState("");

  // API URL
  const API_URL = "https://order-service.bierohero/orders/";

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setOrders(data);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewOrder({ ...newOrder, [name]: value });
  };

  const handleContentChange = (index, field, value) => {
    const updatedContents = [...newOrder.contents];
    updatedContents[index][field] = value;
    setNewOrder({ ...newOrder, contents: updatedContents });
  };

  const addProduct = () => {
    setNewOrder({
      ...newOrder,
      contents: [...newOrder.contents, { product_name: "", quantity: 1 }],
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Submitting order...");
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newOrder),
      });

      if (response.ok) {
        setStatus("Order submitted successfully!");
        fetchOrders(); // Refresh the list
        setNewOrder({
          customer_name: "",
          customer_email: "",
          customer_address: "",
          customer_zipcode: "",
          customer_city: "",
          contents: [{ product_name: "", quantity: 1 }],
        });
      } else {
        const errorData = await response.json();
        throw new Error(errorData.message || "Failed to submit order.");
      }
    } catch (error) {
      setStatus(`Error: ${error.message}`);
      console.error("Error submitting order:", error);
    }
  };

  return (
    <div>
      <h2>Order List</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.order_id}>
            <strong>{order.customer_name}</strong> ({order.customer_city}, {order.customer_email}): {/* E-Mail-Adresse angezeigt */}
            <ul>
              {order.contents.map((content, idx) => (
                <li key={idx}>
                  {content.product_name} - {content.quantity}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
      <h3>Create New Order</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="customer_name"
          placeholder="Name"
          value={newOrder.customer_name}
          onChange={handleInputChange}
          required
        />
        <input
          type="email"
          name="customer_email"
          placeholder="Email"
          value={newOrder.customer_email}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="customer_address"
          placeholder="Address"
          value={newOrder.customer_address}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="customer_zipcode"
          placeholder="Zipcode"
          value={newOrder.customer_zipcode}
          onChange={handleInputChange}
          required
        />
        <input
          type="text"
          name="customer_city"
          placeholder="City"
          value={newOrder.customer_city}
          onChange={handleInputChange}
          required
        />
        <h4>Order Contents</h4>
        {newOrder.contents.map((content, index) => (
          <div key={index}>
            <input
              type="text"
              placeholder="Product Name"
              value={content.product_name}
              onChange={(e) =>
                handleContentChange(index, "product_name", e.target.value)
              }
              required
            />
            <input
              type="number"
              placeholder="Quantity"
              value={content.quantity}
              min="1"
              onChange={(e) =>
                handleContentChange(index, "quantity", e.target.value)
              }
              required
            />
          </div>
        ))}
        <button type="button" onClick={addProduct}>
          Add Another Product
        </button>
        <button type="submit">Submit Order</button>
      </form>
      {status && <p>{status}</p>}
    </div>
  );
}

export default OrderList;

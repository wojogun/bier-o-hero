import React, { useState } from "react";

function PaymentForm() {
  const [orderId, setOrderId] = useState("");
  const [amount, setAmount] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:8003/payments/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ order_id: orderId, amount: parseFloat(amount) }),
    });
  };

  return (
    <div>
      <h2>Process Payment</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Order ID"
          value={orderId}
          onChange={(e) => setOrderId(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button type="submit">Pay</button>
      </form>
    </div>
  );
}

export default PaymentForm;

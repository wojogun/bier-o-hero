import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import OrderList from "./components/OrderList";
import InventoryList from "./components/InventoryList";
import NotificationForm from "./components/NotificationForm";
import PaymentForm from "./components/PaymentForm";
import EventList from "./components/EventList";

function App() {
  return (
    <Router>
      <div>
        <h1>Bier-o'Hero Frontend</h1>
        <Routes>
          <Route path="/" element={<OrderList />} />
          <Route path="/inventory" element={<InventoryList />} />
          <Route path="/notifications" element={<NotificationForm />} />
          <Route path="/payments" element={<PaymentForm />} />
          <Route path="/events" element={<EventList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

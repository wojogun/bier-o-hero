import React, { useState } from "react";

function NotificationForm() {
  const [recipient, setRecipient] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState("");

  // API URL mit HTTPS
  const API_URL = "https://notification-service.bierohero/notify/";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Sending...");

    const payload = {
      recipient,
      subject,
      message,
    };

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        setStatus("Notification sent successfully!");
        setRecipient("");
        setSubject("");
        setMessage("");
      } else {
        const errorData = await response.json();
        throw new Error(errorData.message || "Failed to send notification.");
      }
    } catch (error) {
      setStatus(`Error: ${error.message}`);
      console.error("Notification Error:", error);
    }
  };

  return (
    <div>
      <h2>Send Notification</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Recipient:
            <input
              type="email"
              value={recipient}
              onChange={(e) => setRecipient(e.target.value)}
              required
              placeholder="Enter recipient email"
            />
          </label>
        </div>
        <div>
          <label>
            Subject:
            <input
              type="text"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              required
              placeholder="Enter email subject"
            />
          </label>
        </div>
        <div>
          <label>
            Message:
            <textarea
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              required
              placeholder="Enter your message"
            />
          </label>
        </div>
        <button type="submit">Send</button>
      </form>
      {status && <p>{status}</p>}
    </div>
  );
}

export default NotificationForm;

import React, { useState, useEffect } from "react";

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("https://localhost:8004/events/")
      .then((response) => response.json())
      .then((data) => setEvents(data));
  }, []);

  return (
    <div>
      <h2>Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            {event.name}: {event.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EventList;

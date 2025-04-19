import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const savedDate = localStorage.getItem("demobDate");
  const [demobDate, setDemobDate] = useState(savedDate || "");
  const [daysLeft, setDaysLeft] = useState(null);

  useEffect(() => {
    if (demobDate) {
      calculateDaysLeft(demobDate);
    }
  }, [demobDate]);

  const calculateDaysLeft = (date) => {
    const end = new Date(date);
    const now = new Date();
    const diffTime = end - now;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    setDaysLeft(diffDays);
  };

  const handleChange = (e) => {
    const date = e.target.value;
    setDemobDate(date);
    localStorage.setItem("demobDate", date);
  };

  return (
    <div className="container">
      <h1>Счётчик до дембеля</h1>
      <label>Дата дембеля:</label>
      <input type="date" value={demobDate} onChange={handleChange} />

      {daysLeft !== null && (
        <div className="result">
          <p>Осталось <strong>{daysLeft}</strong> дней</p>
        </div>
      )}
    </div>
  );
}

export default App;

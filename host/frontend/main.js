async function fetchStats() {
  try {
    const res = await fetch("http://localhost:8000/get-stats");
    const data = await res.json();
    document.getElementById("stats").innerText = data.data;
  } catch (err) {
    document.getElementById("stats").innerText = "Error connecting to backend.";
  }
}

fetchStats();
setInterval(fetchStats, 5000);

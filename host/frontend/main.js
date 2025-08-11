async function fetchStats() {
  try {
    const res = await fetch("http://localhost:8000/get-stats"); // Change as needed
    const data = await res.json();
    document.getElementById("stats").innerText = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("stats").innerText = "Error connecting to backend.";
  }
}

// Initial fetch + refresh every 5 seconds
fetchStats();
setInterval(fetchStats, 50000);


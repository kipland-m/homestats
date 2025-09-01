function formatBytes(bytes) {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));

  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function formatTimestamp(timestamp) {
  if (!timestamp || timestamp === 'N/A') return 'N/A';
  const date = new Date(timestamp);

  return date.toLocaleTimeString();
}

// nifty function that will handle the display of every agent 'card'
function createAgentCard(agent) {
  return `
    <div class="agent-card">
      <div class="agent-header">
        AGENT ${agent.id} - ${agent.ip_address} (${agent.mac_address})
        <span style="float: right; opacity: 0.7;">LAST SEEN: ${formatTimestamp(agent.timestamp)}</span>
      </div>
      <div class="stats-grid">
        <div class="stat-item">
          <span class="stat-label">CPU CORES:</span>
          <span class="stat-value">${agent.cpu_cores}</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">CPU THREADS:</span>
          <span class="stat-value">${agent.cpu_threads}</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">CPU PERCENT:</span>
          <span class="stat-value">${agent.cpu_percent}%</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">MEMORY:</span>
          <span class="stat-value">${agent.memory_gb} GB</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">DISK:</span>
          <span class="stat-value">${agent.disk_gb} GB</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">BYTES SENT:</span>
          <span class="stat-value">${formatBytes(agent.bytes_sent)}</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">BYTES RECV:</span>
          <span class="stat-value">${formatBytes(agent.bytes_recv)}</span>
        </div>
      </div>
    </div>
  `;
}

function updateDisplay(data) {
  const statsDisplay = document.getElementById('stats-display');
  const agentCount = document.getElementById('agent-count');
  const lastUpdate = document.getElementById('last-update');
  
  const uniqueAgents = [...new Set(data.agents.map(a => a.ip_address))].length;
  agentCount.textContent = `${uniqueAgents} ACTIVE AGENT${uniqueAgents !== 1 ? 'S' : ''}`;
  lastUpdate.textContent = `LAST UPDATE: ${new Date().toLocaleTimeString()}`;
  
  if (data.agents.length === 0) {
    statsDisplay.innerHTML = '<div class="error-message">NO AGENT DATA AVAILABLE</div>';
    return;
  }
  
  const agentsByIP = {};
  data.agents.forEach(agent => {
    if (!agentsByIP[agent.ip_address] || agent.id > agentsByIP[agent.ip_address].id) {
      agentsByIP[agent.ip_address] = agent;
    }
  });
  
  const agentCards = Object.values(agentsByIP)
    .sort((a, b) => b.id - a.id)
    .map(createAgentCard)
    .join('');
    
  statsDisplay.innerHTML = agentCards;
}

async function fetchStats() {
  try {
    const res = await fetch("http://localhost:8000/get-stats");
    const data = await res.json();
    
    if (res.ok) {
      updateDisplay(data);
    } else {
      throw new Error('Failed to fetch data');
    }
  } catch (err) {
    console.error('Error fetching stats:', err);
    document.getElementById('stats-display').innerHTML = 
      '<div class="error-message">ERROR CONNECTING TO BACKEND</div>';
  }
}

document.getElementById('stats-display').innerHTML = 
  '<div class="loading">INITIALIZING HOMESTATS...</div>';

fetchStats();
setInterval(fetchStats, 5000);

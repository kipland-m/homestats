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


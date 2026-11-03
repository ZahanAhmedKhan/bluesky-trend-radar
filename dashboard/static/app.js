const state = {
  postsChart: null,
  languageChart: null,
  timer: null,
};

function formatStatus(status) {
  if (status === 'critical') return 'Critical';
  if (status === 'warning') return 'Warning';
  return 'Healthy';
}

function renderBars(list) {
  const container = document.getElementById('top-hashtags');
  container.innerHTML = list.map((item) => {
    const width = Math.min(100, Math.max(12, (item.mentions / 300) * 100));
    return `
      <div class="bar-row">
        <span>#${item.tag}</span>
        <div class="bar-track">
          <span class="bar-fill" style="width:${width}%"></span>
        </div>
        <span class="value">${item.mentions}</span>
      </div>
    `;
  }).join('');
}

function renderRisers(list) {
  const container = document.getElementById('biggest-risers');
  container.innerHTML = list.map((item) => `
    <div class="riser-row">
      <span class="tag">#${item.tag}</span>
      <span>${item.current} / ${item.baseline}</span>
      <span class="ratio">x${item.ratio}</span>
    </div>
  `).join('');
}

function updateDashboard(data) {
  document.getElementById('campaign-title').textContent = data.campaign.title;
  document.getElementById('posts-per-minute').textContent = data.posts_per_minute;
  document.getElementById('momentum-value').textContent = `${data.signals.momentum}%`;
  document.getElementById('lag-value').textContent = `${data.health.lag_seconds}s`;
  document.getElementById('dlq-rate').textContent = `${data.health.dlq_rate}%`;
  document.getElementById('status-text').textContent = `${formatStatus(data.health.status)} pipeline`;
  document.getElementById('signal-chip').textContent = data.signals.heat;
  document.getElementById('uptime-value').textContent = `${data.health.uptime_minutes} min`;
  document.getElementById('alerts-value').textContent = data.health.alerts;
  document.getElementById('focus-signal').textContent = data.signals.focus;

  renderBars(data.top_hashtags);
  renderRisers(data.biggest_risers);

  if (state.postsChart) {
    state.postsChart.data.labels = data.time_series.map((point) => new Date(point.time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
    state.postsChart.data.datasets[0].data = data.time_series.map((point) => point.value);
    state.postsChart.update();
  }

  if (state.languageChart) {
    state.languageChart.data.labels = data.language_share.map((lang) => lang.label.toUpperCase());
    state.languageChart.data.datasets[0].data = data.language_share.map((lang) => lang.value);
    state.languageChart.update();
  }
}

function buildCharts() {
  const postsCtx = document.getElementById('postsChart');
  state.postsChart = new Chart(postsCtx, {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Posts / minute',
        data: [],
        fill: true,
        borderColor: '#57b8ff',
        backgroundColor: 'rgba(87,184,255,0.18)',
        tension: 0.45,
        pointRadius: 0,
        borderWidth: 3,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { ticks: { color: '#a7b7d8' }, grid: { display: false } },
        y: { ticks: { color: '#a7b7d8' }, grid: { color: 'rgba(148,163,184,0.14)' } },
      },
    },
  });

  const languageCtx = document.getElementById('languageChart');
  state.languageChart = new Chart(languageCtx, {
    type: 'doughnut',
    data: {
      labels: [],
      datasets: [{
        data: [],
        backgroundColor: ['#57b8ff', '#a78bfa', '#f5c76d', '#45d8a4', '#ff7a88', '#7dd3fc'],
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '60%',
      plugins: { legend: { position: 'bottom', labels: { color: '#ecf4ff', usePointStyle: true } } },
    },
  });
}

async function refreshData() {
  try {
    const response = await fetch('/api/overview');
    const data = await response.json();
    updateDashboard(data);
  } catch (error) {
    console.error('Unable to refresh dashboard', error);
  }
}

buildCharts();
refreshData();
state.timer = setInterval(refreshData, 5000);

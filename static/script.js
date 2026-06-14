/* ============================================================
   BOAT DASHBOARD — script.js
   Handles:
     - SSE live data stream
     - Sonar depth graph (canvas)
     - DOM updates for all gauges
     - Fishing advisor panel
     - Trip timer
     - Log catch modal
   ============================================================ */

// ── SONAR SETUP ──────────────────────────────────────────────
const sonarCanvas = document.getElementById("sonar");
const sCtx = sonarCanvas.getContext("2d");
const sonarPoints = [];
const SONAR_MAX_DEPTH = 50;

function resizeSonar() {
  sonarCanvas.width  = sonarCanvas.offsetWidth;
  sonarCanvas.height = sonarCanvas.offsetHeight;
}
resizeSonar();
window.addEventListener("resize", resizeSonar);

function drawSonar(depth) {
  const W = sonarCanvas.width;
  const H = sonarCanvas.height;

  const y = (depth / SONAR_MAX_DEPTH) * H;
  sonarPoints.push(y);
  if (sonarPoints.length > W) sonarPoints.shift();

  sCtx.clearRect(0, 0, W, H);

  // Grid lines
  sCtx.strokeStyle = "rgba(26,58,63,0.6)";
  sCtx.lineWidth = 1;
  for (let d = 10; d < SONAR_MAX_DEPTH; d += 10) {
    const gy = (d / SONAR_MAX_DEPTH) * H;
    sCtx.beginPath();
    sCtx.moveTo(0, gy);
    sCtx.lineTo(W, gy);
    sCtx.stroke();
    sCtx.fillStyle = "rgba(74,122,112,0.5)";
    sCtx.font = "9px 'Share Tech Mono'";
    sCtx.fillText(d + "ft", 4, gy - 3);
  }

  // Fill under the line
  const grad = sCtx.createLinearGradient(0, 0, 0, H);
  grad.addColorStop(0,   "rgba(0,229,160,0.0)");
  grad.addColorStop(0.6, "rgba(0,229,160,0.08)");
  grad.addColorStop(1,   "rgba(0,229,160,0.2)");

  sCtx.beginPath();
  sCtx.moveTo(0, sonarPoints[0]);
  for (let i = 1; i < sonarPoints.length; i++) sCtx.lineTo(i, sonarPoints[i]);
  sCtx.lineTo(sonarPoints.length - 1, H);
  sCtx.lineTo(0, H);
  sCtx.closePath();
  sCtx.fillStyle = grad;
  sCtx.fill();

  // Depth line
  sCtx.beginPath();
  sCtx.moveTo(0, sonarPoints[0]);
  for (let i = 1; i < sonarPoints.length; i++) sCtx.lineTo(i, sonarPoints[i]);
  sCtx.strokeStyle = "#00e5a0";
  sCtx.lineWidth = 1.5;
  sCtx.shadowColor = "#00e5a0";
  sCtx.shadowBlur = 4;
  sCtx.stroke();
  sCtx.shadowBlur = 0;
}

// ── CLOCK ────────────────────────────────────────────────────
function updateClock() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, "0");
  const m = String(now.getMinutes()).padStart(2, "0");
  const s = String(now.getSeconds()).padStart(2, "0");
  document.getElementById("clock").textContent = `${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();

// ── TRIP TIMER ───────────────────────────────────────────────
const tripStart = Date.now();

function updateTripTimer() {
  const elapsed = Math.floor((Date.now() - tripStart) / 1000);
  const h = Math.floor(elapsed / 3600);
  const m = Math.floor((elapsed % 3600) / 60);
  const s = elapsed % 60;
  document.getElementById("trip-timer").textContent =
    `${h}:${String(m).padStart(2,"0")}:${String(s).padStart(2,"0")}`;
}
setInterval(updateTripTimer, 1000);
updateTripTimer();

// ── DOM HELPERS ───────────────────────────────────────────────
function set(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function fmtCoord(val, pos, neg) {
  return Math.abs(val).toFixed(6) + "° " + (val >= 0 ? pos : neg);
}

// ── UPDATE DASHBOARD ──────────────────────────────────────────
function update(data) {
  // Depth
  set("depth", data.depth.toFixed(1));
  drawSonar(data.depth);

  // Battery
  set("battery", data.battery.toFixed(1));
  const battPct = Math.max(0, Math.min(((data.battery - 11.0) / (13.0 - 11.0)) * 100, 100));
  const battBar = document.getElementById("batt-bar");
  battBar.style.width = battPct + "%";
  if (data.battery < 11.8) {
    battBar.style.background = "#e04040";
    set("batt-status", "LOW — HEAD IN SOON");
  } else if (data.battery < 12.2) {
    battBar.style.background = "#f5a623";
    set("batt-status", "DRAINING");
  } else {
    battBar.style.background = "#00e5a0";
    set("batt-status", "GOOD");
  }

  // GPS
  set("lat", fmtCoord(data.lat, "N", "S"));
  set("lon", fmtCoord(data.lon, "E", "W"));

  // Advisor
  if (data.advisor && data.advisor.conditions) {
    updateAdvisor(data.advisor);
  }
}

// ── FISHING ADVISOR ───────────────────────────────────────────
function updateAdvisor(adv) {
  const c = adv.conditions;

  set("adv-season",    c.season);
  set("adv-time",      c.time_of_day);
  set("adv-temp-f",    c.temp_f ? c.temp_f.toFixed(1) : "--");
  set("adv-updated",   adv.updated);
  set("advisor-tip",   adv.tip);

  // Species
  const speciesEl = document.getElementById("advisor-species");
  if (speciesEl && adv.active_species) {
    speciesEl.innerHTML = adv.active_species.map(s => `
      <div class="species-item">
        <div class="species-dot"></div>
        <div>
          <div class="species-name">${s.species}</div>
          ${s.reason ? `<div class="species-reason">${s.reason}</div>` : ""}
        </div>
      </div>
    `).join("");
  }

  // Baits
  const baitsEl = document.getElementById("advisor-baits");
  if (baitsEl && adv.baits) {
    baitsEl.innerHTML = adv.baits.map(b => `
      <div class="bait-item">
        <div class="bait-check">✓</div>
        <div>
          <div class="bait-name">${b.bait}</div>
          <div class="bait-reason">${b.reason}</div>
        </div>
      </div>
    `).join("");
  }
}

// ── LOG CATCH MODAL ───────────────────────────────────────────
let selectedSpecies = null;
let selectedBait    = null;

function openLogModal() {
  document.getElementById("modal-overlay").classList.add("open");
  document.getElementById("modal-confirm").textContent = "";
  selectedSpecies = null;
  selectedBait    = null;
  document.querySelectorAll(".opt-btn").forEach(b => b.classList.remove("selected"));
}

function closeLogModal() {
  document.getElementById("modal-overlay").classList.remove("open");
}

function selectOption(btn, type) {
  const group = type === "species" ? "species-options" : "bait-options";
  document.getElementById(group)
    .querySelectorAll(".opt-btn")
    .forEach(b => b.classList.remove("selected"));
  btn.classList.add("selected");
  if (type === "species") selectedSpecies = btn.textContent;
  else selectedBait = btn.textContent;
}

function saveCatch() {
  if (!selectedSpecies || !selectedBait) {
    document.getElementById("modal-confirm").textContent = "Pick a species and bait first.";
    document.getElementById("modal-confirm").style.color = "#f5a623";
    return;
  }

  fetch("/api/log-catch", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      species: selectedSpecies,
      bait:    selectedBait,
    })
  })
  .then(r => r.json())
  .then(data => {
    document.getElementById("modal-confirm").textContent = "✓ CATCH LOGGED";
    document.getElementById("modal-confirm").style.color = "#00e5a0";
    setTimeout(closeLogModal, 1500);
  })
  .catch(() => {
    document.getElementById("modal-confirm").textContent = "Error saving catch.";
    document.getElementById("modal-confirm").style.color = "#e04040";
  });
}

// ── SERVER-SENT EVENTS ────────────────────────────────────────
const dot   = document.getElementById("conn-dot");
const label = document.getElementById("conn-label");

function connect() {
  const source = new EventSource("/stream");

  source.onopen = () => {
    dot.classList.add("live");
    dot.classList.remove("dead");
    label.textContent = "LIVE";
  };

  source.onmessage = (event) => {
    try {
      update(JSON.parse(event.data));
    } catch(e) {
      console.warn("Parse error:", e);
    }
  };

  source.onerror = () => {
    dot.classList.remove("live");
    dot.classList.add("dead");
    label.textContent = "RECONNECTING";
    source.close();
    setTimeout(connect, 3000);
  };
}

connect();
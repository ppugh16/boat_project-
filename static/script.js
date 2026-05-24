/* ============================================================
   BOAT DASHBOARD — script.js
   Handles:
     - SSE connection to /stream
     - Live DOM updates for all gauges
     - Compass canvas drawing
     - Sonar rolling graph
   ============================================================ */

// ── SONAR SETUP ──────────────────────────────────────────────
const sonarCanvas = document.getElementById("sonar");
const sCtx = sonarCanvas.getContext("2d");
const sonarPoints = [];
const SONAR_MAX_DEPTH = 50; // feet — adjust for your water

function resizeSonar() {
  sonarCanvas.width  = sonarCanvas.offsetWidth;
  sonarCanvas.height = sonarCanvas.offsetHeight;
}
resizeSonar();
window.addEventListener("resize", resizeSonar);

function drawSonar(depth) {
  const W = sonarCanvas.width;
  const H = sonarCanvas.height;

  // Map depth to Y position (shallow = low Y)
  const y = (depth / SONAR_MAX_DEPTH) * H;
  sonarPoints.push(y);
  if (sonarPoints.length > W) sonarPoints.shift();

  sCtx.clearRect(0, 0, W, H);

  // Grid lines
  sCtx.strokeStyle = "rgba(26,58,63,0.8)";
  sCtx.lineWidth = 1;
  for (let d = 10; d < SONAR_MAX_DEPTH; d += 10) {
    const gy = (d / SONAR_MAX_DEPTH) * H;
    sCtx.beginPath();
    sCtx.moveTo(0, gy);
    sCtx.lineTo(W, gy);
    sCtx.stroke();
    sCtx.fillStyle = "rgba(74,122,112,0.6)";
    sCtx.font = "10px 'Share Tech Mono'";
    sCtx.fillText(d + "ft", 4, gy - 3);
  }

  // Depth fill (water column)
  const grad = sCtx.createLinearGradient(0, 0, 0, H);
  grad.addColorStop(0, "rgba(0,229,160,0.0)");
  grad.addColorStop(0.7, "rgba(0,229,160,0.12)");
  grad.addColorStop(1, "rgba(0,229,160,0.25)");

  sCtx.beginPath();
  sCtx.moveTo(0, sonarPoints[0]);
  for (let i = 1; i < sonarPoints.length; i++) {
    sCtx.lineTo(i, sonarPoints[i]);
  }
  sCtx.lineTo(sonarPoints.length - 1, H);
  sCtx.lineTo(0, H);
  sCtx.closePath();
  sCtx.fillStyle = grad;
  sCtx.fill();

  // Depth line
  sCtx.beginPath();
  sCtx.moveTo(0, sonarPoints[0]);
  for (let i = 1; i < sonarPoints.length; i++) {
    sCtx.lineTo(i, sonarPoints[i]);
  }
  sCtx.strokeStyle = "#00e5a0";
  sCtx.lineWidth = 1.5;
  sCtx.shadowColor = "#00e5a0";
  sCtx.shadowBlur = 4;
  sCtx.stroke();
  sCtx.shadowBlur = 0;
}

// ── COMPASS SETUP ─────────────────────────────────────────────
const compassCanvas = document.getElementById("compass");
const cCtx = compassCanvas.getContext("2d");
const CX = compassCanvas.width / 2;
const CY = compassCanvas.height / 2;
const CR = CX - 8;

function drawCompass(heading) {
  cCtx.clearRect(0, 0, compassCanvas.width, compassCanvas.height);

  // Outer ring
  cCtx.beginPath();
  cCtx.arc(CX, CY, CR, 0, Math.PI * 2);
  cCtx.strokeStyle = "#1a3a3f";
  cCtx.lineWidth = 2;
  cCtx.stroke();

  // Cardinal tick marks
  const cardinals = ["N", "E", "S", "W"];
  for (let i = 0; i < 36; i++) {
    const angle = (i * 10 - heading) * (Math.PI / 180);
    const isCardinal = i % 9 === 0;
    const isMajor = i % 3 === 0;
    const r1 = isCardinal ? CR - 18 : (isMajor ? CR - 10 : CR - 6);

    cCtx.beginPath();
    cCtx.moveTo(
      CX + Math.sin(angle) * (CR - 2),
      CY - Math.cos(angle) * (CR - 2)
    );
    cCtx.lineTo(
      CX + Math.sin(angle) * r1,
      CY - Math.cos(angle) * r1
    );
    cCtx.strokeStyle = isCardinal ? "#00e5a0" : "#1a3a3f";
    cCtx.lineWidth = isCardinal ? 2 : 1;
    cCtx.stroke();

    if (isCardinal) {
      const label = cardinals[i / 9];
      const lx = CX + Math.sin(angle) * (r1 - 12);
      const ly = CY - Math.cos(angle) * (r1 - 12) + 4;
      cCtx.font = "bold 11px 'Orbitron'";
      cCtx.fillStyle = label === "N" ? "#f5a623" : "#00e5a0";
      cCtx.textAlign = "center";
      cCtx.fillText(label, lx, ly);
    }
  }

  // Heading needle
  const needleAngle = 0; // always points up (heading rotates the dial)
  cCtx.save();
  cCtx.translate(CX, CY);

  // North needle (amber)
  cCtx.beginPath();
  cCtx.moveTo(0, -(CR - 28));
  cCtx.lineTo(6, 10);
  cCtx.lineTo(-6, 10);
  cCtx.closePath();
  cCtx.fillStyle = "#f5a623";
  cCtx.shadowColor = "#f5a623";
  cCtx.shadowBlur = 8;
  cCtx.fill();

  // South needle (dim)
  cCtx.beginPath();
  cCtx.moveTo(0, CR - 28);
  cCtx.lineTo(5, -8);
  cCtx.lineTo(-5, -8);
  cCtx.closePath();
  cCtx.fillStyle = "#1a3a3f";
  cCtx.shadowBlur = 0;
  cCtx.fill();

  // Center dot
  cCtx.beginPath();
  cCtx.arc(0, 0, 4, 0, Math.PI * 2);
  cCtx.fillStyle = "#00e5a0";
  cCtx.fill();

  cCtx.restore();
}

// ── DOM HELPERS ───────────────────────────────────────────────
function set(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function setWarning(cardId, level) {
  // level: null | 'warn' | 'danger'
  const card = document.getElementById(cardId);
  if (!card) return;
  card.classList.remove("card--warn", "card--danger");
  if (level) card.classList.add("card--" + level);
}

// ── LIVE CLOCK ────────────────────────────────────────────────
function updateClock() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, "0");
  const m = String(now.getMinutes()).padStart(2, "0");
  const s = String(now.getSeconds()).padStart(2, "0");
  set("clock", `${h}:${m}:${s}`);
}
setInterval(updateClock, 1000);
updateClock();

// ── GPS FORMAT ────────────────────────────────────────────────
function fmtCoord(val, pos, neg) {
  const dir = val >= 0 ? pos : neg;
  return Math.abs(val).toFixed(6) + "° " + dir;
}

// ── UPDATE DASHBOARD ──────────────────────────────────────────
function update(data) {
  // Depth
  set("depth", data.depth.toFixed(1));
  drawSonar(data.depth);
  const depthPct = Math.min(data.depth / SONAR_MAX_DEPTH * 100, 100);
  document.getElementById("depth-bar").style.width = depthPct + "%";
  setWarning("card-depth", data.depth < 3 ? "danger" : data.depth < 6 ? "warn" : null);

  // Speed
  set("speed", data.speed.toFixed(1));
  setWarning("card-speed", data.speed > 10 ? "warn" : null);

  // Heading
  set("heading-val", data.heading + "°");
  drawCompass(data.heading);

  // Water temp
  set("water-temp", data.water_temp.toFixed(1));

  // Battery
  set("battery", data.battery.toFixed(1));
  const battPct = Math.max(0, Math.min(((data.battery - 11.0) / (13.0 - 11.0)) * 100, 100));
  const battBar = document.getElementById("batt-bar");
  battBar.style.width = battPct + "%";
  battBar.style.background = data.battery < 11.8 ? "#e04040" : data.battery < 12.2 ? "#f5a623" : "#00e5a0";

  // GPS
  set("lat", fmtCoord(data.lat, "N", "S"));
  set("lon", fmtCoord(data.lon, "E", "W"));
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
      const data = JSON.parse(event.data);
      update(data);
    } catch (e) {
      console.warn("Parse error:", e);
    }
  };

  source.onerror = () => {
    dot.classList.remove("live");
    dot.classList.add("dead");
    label.textContent = "RECONNECTING";
    source.close();
    // Try again in 3 seconds
    setTimeout(connect, 3000);
  };
}

connect();

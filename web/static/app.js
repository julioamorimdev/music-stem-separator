const $ = (id) => document.getElementById(id);

const file = $("file");
const btnUpload = $("btnUpload");
const statusEl = $("status");
const progress = $("progress");

const player = $("player");
const audioInst = $("audioInst");
const audioVoc = $("audioVoc");
const volInst = $("volInst");
const volVoc = $("volVoc");
const dlInst = $("dlInst");
const dlVoc = $("dlVoc");
const btnSync = $("btnSync");
const btnReset = $("btnReset");

let currentJobId = null;
let syncing = false;

function setStatus(text, kind = "muted") {
  statusEl.className = `status ${kind}`;
  statusEl.textContent = text;
}

function showProgress(show) {
  progress.classList.toggle("hidden", !show);
  if (!show) progress.value = 0;
}

function setPlayerVisible(visible) {
  player.classList.toggle("hidden", !visible);
}

function syncVolumes() {
  audioInst.volume = Number(volInst.value);
  audioVoc.volume = Number(volVoc.value);
}

function syncCurrentTime(from, to) {
  // evita loop infinito de sync
  if (syncing) return;
  syncing = true;
  try {
    const delta = Math.abs((to.currentTime || 0) - (from.currentTime || 0));
    if (delta > 0.15) to.currentTime = from.currentTime || 0;
  } finally {
    syncing = false;
  }
}

function syncPlayPause(from, to) {
  if (from.paused) {
    to.pause();
  } else {
    // tenta tocar o outro também (pode exigir gesto do usuário dependendo do navegador)
    to.currentTime = from.currentTime || 0;
    to.play().catch(() => {});
  }
}

async function createJob(f) {
  const fd = new FormData();
  fd.append("file", f);
  const res = await fetch("/api/jobs", { method: "POST", body: fd });
  const data = await res.json();
  if (!data.ok) throw new Error(data.error || "Falha ao criar job.");
  return data.job;
}

async function fetchJob(jobId) {
  const res = await fetch(`/api/jobs/${jobId}`);
  const data = await res.json();
  if (!data.ok) throw new Error(data.error || "Falha ao consultar job.");
  return data.job;
}

async function waitForDone(jobId) {
  showProgress(true);
  setStatus("Processando… isso pode levar alguns minutos.", "muted");
  progress.value = 10;
  while (true) {
    const job = await fetchJob(jobId);
    if (job.status === "done") return job;
    if (job.status === "error") throw new Error(job.error || "Erro no processamento.");
    // progresso estimado simples (não temos callback real do Demucs)
    progress.value = Math.min(95, progress.value + 3);
    await new Promise((r) => setTimeout(r, 1500));
  }
}

function wireAudioSync() {
  audioInst.addEventListener("play", () => syncPlayPause(audioInst, audioVoc));
  audioVoc.addEventListener("play", () => syncPlayPause(audioVoc, audioInst));
  audioInst.addEventListener("pause", () => syncPlayPause(audioInst, audioVoc));
  audioVoc.addEventListener("pause", () => syncPlayPause(audioVoc, audioInst));
  audioInst.addEventListener("seeking", () => syncCurrentTime(audioInst, audioVoc));
  audioVoc.addEventListener("seeking", () => syncCurrentTime(audioVoc, audioInst));
  audioInst.addEventListener("timeupdate", () => syncCurrentTime(audioInst, audioVoc));
  audioVoc.addEventListener("timeupdate", () => syncCurrentTime(audioVoc, audioInst));
}

wireAudioSync();
volInst.addEventListener("input", syncVolumes);
volVoc.addEventListener("input", syncVolumes);

btnReset.addEventListener("click", () => {
  audioInst.pause();
  audioVoc.pause();
  audioInst.currentTime = 0;
  audioVoc.currentTime = 0;
});

btnSync.addEventListener("click", () => {
  // força alinhamento e toca ambos
  const t = Math.max(audioInst.currentTime || 0, audioVoc.currentTime || 0);
  audioInst.currentTime = t;
  audioVoc.currentTime = t;
  audioInst.play().catch(() => {});
  audioVoc.play().catch(() => {});
});

btnUpload.addEventListener("click", async () => {
  const f = file.files && file.files[0];
  if (!f) {
    setStatus("Selecione um arquivo primeiro.", "muted");
    return;
  }

  setPlayerVisible(false);
  showProgress(false);
  setStatus("Enviando…", "muted");
  btnUpload.disabled = true;

  try {
    const job = await createJob(f);
    currentJobId = job.id;
    const done = await waitForDone(currentJobId);
    const { vocals_url, instrumental_url } = done.result;

    audioInst.src = instrumental_url;
    audioVoc.src = vocals_url;
    dlInst.href = instrumental_url;
    dlInst.download = "instrumental.mp3";
    dlVoc.href = vocals_url;
    dlVoc.download = "vocais.mp3";

    syncVolumes();
    setStatus("Pronto! Use os controles abaixo.", "muted");
    progress.value = 100;
    setPlayerVisible(true);
    showProgress(false);
  } catch (e) {
    setStatus(`Erro: ${e.message}`, "muted");
    showProgress(false);
  } finally {
    btnUpload.disabled = false;
  }
});


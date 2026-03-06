// ── Sidebar toggle (mobile) ──
function toggleSidebar() {
  const aside = document.querySelector('aside');
  const overlay = document.querySelector('.sidebar-overlay');
  const toggle = document.querySelector('.menu-toggle');
  aside.classList.toggle('open');
  overlay.classList.toggle('active');
  toggle.classList.toggle('active');
}

function closeSidebar() {
  const aside = document.querySelector('aside');
  const overlay = document.querySelector('.sidebar-overlay');
  const toggle = document.querySelector('.menu-toggle');
  aside.classList.remove('open');
  overlay.classList.remove('active');
  toggle.classList.remove('active');
}

// ── Section navigation ──
function showSection(id, navBtn, sidebarItem) {
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');

  if (navBtn) {
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    navBtn.classList.add('active');
  }
  if (sidebarItem) {
    document.querySelectorAll('.sidebar-item').forEach(b => b.classList.remove('active'));
    sidebarItem.classList.add('active');
  }

  // Close sidebar on mobile after navigation
  if (window.innerWidth <= 768) {
    closeSidebar();
  }
}

// ── Compare toggle ──
function toggleCompare(group, variant, btn) {
  document.querySelectorAll(`#${group}-fbv, #${group}-cbv`).forEach(el => el.classList.remove('active'));
  document.getElementById(`${group}-${variant}`).classList.add('active');
  btn.parentElement.querySelectorAll('.compare-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}

// ── Quiz ──
function answer(btn, result, msg) {
  const q = btn.closest('.quiz-q');
  if (q.dataset.answered) return;
  q.dataset.answered = true;
  btn.classList.add(result);
  const fb = q.querySelector('.quiz-feedback');
  fb.textContent = msg;
  fb.classList.add('show', result === 'correct' ? 'ok' : 'bad');
  q.querySelectorAll('.quiz-opt').forEach(b => b.style.pointerEvents = 'none');
}

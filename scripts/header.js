/* ═══════════════════════════════════════════════════════
   Reusable Header Component + Shared Page Interactions
   ═══════════════════════════════════════════════════════
   Usage — set window.__PAGE before loading this script:

   <script>
     window.__PAGE = {
       logo:    'Django',                  // plain text or inner HTML
       tag:     'CRUD in Action',          // header-tag text (optional)
       homeLink:'../index.html',           // link back to landing (optional)
       nav: [                              // nav buttons (optional)
         { id: 'overview', label: 'Overview' },
         { id: 'setup',    label: 'Setup'    },
       ]
     };
   </script>
   <script src="../scripts/header.js"></script>
   ═══════════════════════════════════════════════════════ */

(function () {
  'use strict';

  const cfg = window.__PAGE || {};

  /* ── Build header ────────────────────────────────── */
  function buildHeader() {
    const header = document.createElement('header');

    // Hamburger (mobile)
    const toggle = document.createElement('button');
    toggle.className = 'menu-toggle';
    toggle.setAttribute('aria-label', 'Toggle sidebar');
    toggle.innerHTML = '<span></span><span></span><span></span>';
    toggle.addEventListener('click', toggleSidebar);
    header.appendChild(toggle);

    // Logo
    const logo = document.createElement('div');
    logo.className = 'logo';
    if (cfg.homeLink) {
      const a = document.createElement('a');
      a.href = cfg.homeLink;
      a.innerHTML = cfg.logo || 'Learn Django';
      a.style.cssText = 'color:inherit;text-decoration:none';
      logo.appendChild(a);
    } else {
      logo.innerHTML = cfg.logo || 'Learn Django';
    }
    header.appendChild(logo);

    // Nav buttons
    if (cfg.nav && cfg.nav.length) {
      const nav = document.createElement('nav');
      cfg.nav.forEach(function (item, i) {
        const btn = document.createElement('button');
        btn.textContent = item.label;
        if (i === 0) btn.classList.add('active');
        btn.addEventListener('click', function () {
          showSection(item.id, btn);
        });
        nav.appendChild(btn);
      });
      header.appendChild(nav);
    }

    // Tag
    if (cfg.tag) {
      const tag = document.createElement('div');
      tag.className = 'header-tag';
      tag.textContent = cfg.tag || 'BootCamp 2026';
      header.appendChild(tag);
    }

    return header;
  }

  /* ── Build sidebar overlay ───────────────────────── */
  function buildOverlay() {
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    overlay.addEventListener('click', closeSidebar);
    return overlay;
  }

  /* ── Inject into DOM ─────────────────────────────── */
  const target = document.getElementById('header-mount') || document.body;
  const header = buildHeader();
  const overlay = buildOverlay();

  if (target === document.body) {
    document.body.insertBefore(overlay, document.body.firstChild);
    document.body.insertBefore(header, document.body.firstChild);
  } else {
    target.appendChild(header);
    target.parentNode.insertBefore(overlay, target.nextSibling);
  }

  /* ═══════════════════════════════════════════════════
     Shared interactive functions (exposed globally)
     ═══════════════════════════════════════════════════ */

  /* ── Sidebar toggle (mobile) ─────────────────────── */
  function toggleSidebar() {
    var aside   = document.querySelector('aside');
    var overlay = document.querySelector('.sidebar-overlay');
    var toggle  = document.querySelector('.menu-toggle');
    if (aside)   aside.classList.toggle('open');
    if (overlay) overlay.classList.toggle('active');
    if (toggle)  toggle.classList.toggle('active');
  }

  function closeSidebar() {
    var aside   = document.querySelector('aside');
    var overlay = document.querySelector('.sidebar-overlay');
    var toggle  = document.querySelector('.menu-toggle');
    if (aside)   aside.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
    if (toggle)  toggle.classList.remove('active');
  }

  /* ── Section navigation ──────────────────────────── */
  function showSection(id, navBtn, sidebarItem) {
    document.querySelectorAll('.section').forEach(function (s) {
      s.classList.remove('active');
    });
    var sec = document.getElementById(id);
    if (sec) sec.classList.add('active');

    if (navBtn) {
      document.querySelectorAll('nav button').forEach(function (b) {
        b.classList.remove('active');
      });
      navBtn.classList.add('active');
    }
    if (sidebarItem) {
      document.querySelectorAll('.sidebar-item').forEach(function (b) {
        b.classList.remove('active');
      });
      sidebarItem.classList.add('active');
    }

    // Close sidebar on mobile after navigation
    if (window.innerWidth <= 768) {
      closeSidebar();
    }
  }

  /* ── Compare / toggle panels ─────────────────────── */
  function toggleCompare(group, variant, btn) {
    document.querySelectorAll('[id^="' + group + '-"]').forEach(function (el) {
      el.classList.remove('active');
    });
    var panel = document.getElementById(group + '-' + variant);
    if (panel) panel.classList.add('active');
    if (btn) {
      btn.parentElement.querySelectorAll('.compare-btn').forEach(function (b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');
    }
  }

  /* ── Quiz answer ─────────────────────────────────── */
  function answer(btn, result, msg) {
    var card = btn.closest('.quiz-q');
    if (!card || card.dataset.done) return;
    card.dataset.done = '1';
    btn.classList.add(result);
    var fb = card.querySelector('.quiz-feedback');
    if (fb) {
      fb.textContent = msg;
      fb.classList.add('show', result === 'correct' ? 'ok' : 'bad');
    }
    card.querySelectorAll('.quiz-opt').forEach(function (b) {
      b.style.pointerEvents = 'none';
    });
  }

  /* ── Expose globals ──────────────────────────────── */
  window.toggleSidebar  = toggleSidebar;
  window.closeSidebar   = closeSidebar;
  window.showSection    = showSection;
  window.toggleCompare  = toggleCompare;
  window.answer         = answer;

  /* ── Scroll to element by ID ─────────────────────── */
  function scrollToId(id) {
    var el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  window.scrollToId = scrollToId;

})();

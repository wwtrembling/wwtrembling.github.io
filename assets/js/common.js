// Tool Shelf - Common JavaScript Utilities

/**
 * Language Switcher
 * Handles navigation between different language versions
 */
const LanguageSwitcher = {
  languages: {
    ko: { name: '한국어', flag: '🇰🇷' },
    en: { name: 'English', flag: '🇺🇸' },
    ja: { name: '日本語', flag: '🇯🇵' },
    'zh-cn': { name: '简体中文', flag: '🇨🇳' },
    'zh-tw': { name: '繁體中文', flag: '🇹🇼' },
    hi: { name: 'हिन्दी', flag: '🇮🇳' },
    id: { name: 'Bahasa Indonesia', flag: '🇮🇩' },
    vi: { name: 'Tiếng Việt', flag: '🇻🇳' },
    th: { name: 'ภาษาไทย', flag: '🇹🇭' },
    de: { name: 'Deutsch', flag: '🇩🇪' },
    pt: { name: 'Português', flag: '🇧🇷' }
  },

  getCurrentLang() {
    const path = window.location.pathname;
    const match = path.match(/\/(zh-cn|zh-tw|ko|en|ja|hi|id|vi|th|de|pt)\//);
    return match ? match[1] : 'en';
  },

  switchLanguage(targetLang) {
    const currentPath = window.location.pathname;
    const currentLang = this.getCurrentLang();

    // Replace current language with target language in path
    const newPath = currentPath.replace(`/${currentLang}/`, `/${targetLang}/`);
    window.location.href = newPath;
  },

  renderSwitcher(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const currentLang = this.getCurrentLang();
    let html = '';

    for (const [code, info] of Object.entries(this.languages)) {
      const isActive = code === currentLang;
      html += `
        <button 
          class="lang-btn ${isActive ? 'active' : ''}" 
          onclick="LanguageSwitcher.switchLanguage('${code}')"
          title="${info.name}"
        >
          ${info.flag} ${code.toUpperCase()}
        </button>
      `;
    }

    container.innerHTML = html;
  }
};

/**
 * Utility Functions
 */
const Utils = {
  // Copy text to clipboard
  copyToClipboard(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text)
        .then(() => this.showToast('Copied to clipboard!'))
        .catch(() => this.fallbackCopy(text));
    } else {
      this.fallbackCopy(text);
    }
  },

  fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    let ok = false;
    try {
      ok = document.execCommand('copy');
    } catch (e) {
      ok = false;
    }
    document.body.removeChild(textarea);
    this.showToast(ok ? 'Copied to clipboard!' : 'Copy failed');
  },

  // Show toast notification
  showToast(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    toast.style.cssText = `
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: #0f172a;
      color: white;
      padding: 1rem 1.5rem;
      border-radius: 0.5rem;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
      z-index: 1000;
      animation: slideIn 0.3s ease;
      max-width: calc(100vw - 32px);
      text-align: center;
    `;

    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'slideOut 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, duration);
  },

  // Format number with commas
  formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  },

  // Debounce function
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  },

  // Download file
  downloadFile(content, filename, mimeType = 'text/plain') {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }
};

/**
 * Analytics Helper
 *
 * Thin wrapper over GA4's gtag(). All calls are no-ops when gtag is absent
 * (e.g. AdSense/GA blocked, or running offline), so callers never need to
 * guard. Consent Mode v2 defaults (set in the GA4 <head> block) still apply —
 * without a CMP these events arrive as modeled/cookieless pings.
 */
const Analytics = {
  // Fire a GA4 custom event. `params` is an optional object of event params.
  track(name, params) {
    if (typeof gtag === 'function') {
      gtag('event', name, params || {});
    }
  },

  // Tool slug from the URL path (/<lang>/<slug>/...). '' on the index / root.
  toolSlug() {
    const m = window.location.pathname.match(/^\/[^/]+\/([^/]+)\/?/);
    return m ? m[1] : '';
  },

  // Back-compat shim for older call sites.
  trackEvent(category, action, label) {
    this.track(action, { event_category: category, event_label: label });
  },

  trackPageView(path) {
    if (typeof gtag === 'function' && typeof window.GA_MEASUREMENT_ID === 'string') {
      gtag('config', window.GA_MEASUREMENT_ID, { page_path: path });
    }
  }
};

/**
 * Delegated tool-interaction tracking.
 *
 * Tool pages are generated from ~50 per-tool templates, each with its own
 * inline primary-action handler (calculate / convert / format / decode ...)
 * and a shared shareResult(). Rather than touch every template, we listen for
 * clicks at the document level and map them to GA4 events by convention:
 *   - any <button class="btn-primary"> with an onclick (except the PWA install
 *     button) => `tool_calculate`
 *   - any button whose onclick calls shareResult() => `tool_share`
 * Best-effort by design; missing an exotic tool is acceptable for analytics.
 */
document.addEventListener('click', (e) => {
  const btn = e.target.closest && e.target.closest('button');
  if (!btn) return;
  const slug = Analytics.toolSlug();
  if (!slug) return; // index / hub pages have their own instrumentation
  const onclick = btn.getAttribute('onclick') || '';
  if (/shareResult\s*\(/.test(onclick)) {
    Analytics.track('tool_share', {
      tool_slug: slug,
      method: (typeof navigator !== 'undefined' && navigator.share) ? 'share' : 'copy'
    });
  } else if (btn.classList.contains('btn-primary') && btn.id !== 'pwaInstallBtn' && onclick) {
    Analytics.track('tool_calculate', { tool_slug: slug });
  }
});

/**
 * Favorites Export / Import
 *
 * Favorites live in localStorage (`utilify_favorites`, comma-joined slugs),
 * which is per-device. This lets a user move them between devices: Export
 * downloads a small JSON snapshot (favorites + current theme); Import reads
 * such a file and merges the favorites (union) into this device, optionally
 * adopting the saved theme. Wired up by element id, so the controls can live
 * on the index, the About page, or a future settings page.
 */
const FavoritesData = {
  FAV_KEY: 'utilify_favorites',
  THEME_KEY: 'utilify_theme',

  getFavs() {
    return (localStorage.getItem(this.FAV_KEY) || '').split(',').filter(Boolean);
  },

  exportFile() {
    const favs = this.getFavs();
    const payload = {
      app: 'utilify',
      type: 'favorites-export',
      version: 1,
      exported_at: new Date().toISOString(),
      favorites: favs,
      theme: localStorage.getItem(this.THEME_KEY) || null
    };
    const date = new Date().toISOString().slice(0, 10);
    Utils.downloadFile(
      JSON.stringify(payload, null, 2),
      'utilify-favorites-' + date + '.json',
      'application/json'
    );
    return favs.length;
  },

  // Parse + validate an export payload. Returns the merge result or throws.
  applyImport(text) {
    const data = JSON.parse(text);
    const incoming = Array.isArray(data) ? data : data.favorites;
    if (!Array.isArray(incoming)) {
      throw new Error('No favorites array in file');
    }
    // Keep only plausible slugs and merge as a union with what's here.
    const clean = incoming.filter(s => typeof s === 'string' && /^[a-z0-9-]+$/.test(s));
    const merged = [...new Set([...this.getFavs(), ...clean])];
    localStorage.setItem(this.FAV_KEY, merged.join(','));
    // Adopt a saved theme if the snapshot carried one.
    const theme = data && data.theme;
    if (theme === 'dark' || theme === 'light') {
      localStorage.setItem(this.THEME_KEY, theme);
      document.documentElement.setAttribute('data-theme', theme);
    }
    return { added: clean.length, total: merged.length };
  },

  // Wire the export button, import button, and hidden file input by id.
  init() {
    const exportBtn = document.getElementById('favExportBtn');
    const importBtn = document.getElementById('favImportBtn');
    const fileInput = document.getElementById('favImportInput');
    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        const count = this.exportFile();
        if (count === 0 && exportBtn.dataset.msgEmpty) {
          Utils.showToast(exportBtn.dataset.msgEmpty);
        }
        Analytics.track('favorites_export', { count: count });
      });
    }
    if (importBtn && fileInput) {
      importBtn.addEventListener('click', () => fileInput.click());
      fileInput.addEventListener('change', () => {
        const file = fileInput.files && fileInput.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = () => {
          try {
            const res = this.applyImport(String(reader.result));
            Utils.showToast(
              (importBtn.dataset.msgSuccess || 'Favorites imported') + ' (' + res.added + ')'
            );
            Analytics.track('favorites_import', { added: res.added, total: res.total });
            // Reload so the index re-renders star states from localStorage.
            setTimeout(() => window.location.reload(), 700);
          } catch (e) {
            Utils.showToast(importBtn.dataset.msgError || 'Could not read that file');
          }
        };
        reader.onerror = () => {
          Utils.showToast(importBtn.dataset.msgError || 'Could not read that file');
        };
        reader.readAsText(file);
        fileInput.value = ''; // allow re-importing the same file
      });
    }
  }
};

/**
 * Initialize on DOM ready
 */
document.addEventListener('DOMContentLoaded', () => {
  FavoritesData.init();
  // Render language switcher if container exists
  LanguageSwitcher.renderSwitcher('languageSwitcher');

  // Add smooth scroll behavior to anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Add animation to cards on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
  });
});

// Add CSS for toast animations
const style = document.createElement('style');
style.textContent = `
  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }

  @keyframes slideOut {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(100%);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);

/**
 * PWA Service Worker Registration
 */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registered: ', registration);
      })
      .catch(registrationError => {
        console.log('SW registration failed: ', registrationError);
      });
  });
}

/**
 * PWA Install Prompt
 */
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;

  // Show the install button if it exists
  const installBtn = document.getElementById('pwaInstallBtn');
  if (installBtn) {
    installBtn.style.display = 'inline';
    const sep = installBtn.parentElement?.querySelector('.pwa-install-sep');
    if (sep) sep.style.display = 'inline';

    installBtn.addEventListener('click', (e) => {
      // Hide the app provided install promotion
      installBtn.style.display = 'none';
      // Show the install prompt
      deferredPrompt.prompt();
      // Wait for the user to respond to the prompt
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
    });
  }
});

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
    hi: { name: 'हिन्दी', flag: '🇮🇳' },
    id: { name: 'Bahasa Indonesia', flag: '🇮🇩' },
    vi: { name: 'Tiếng Việt', flag: '🇻🇳' },
    th: { name: 'ภาษาไทย', flag: '🇹🇭' },
    de: { name: 'Deutsch', flag: '🇩🇪' },
    pt: { name: 'Português', flag: '🇧🇷' }
  },

  getCurrentLang() {
    const path = window.location.pathname;
    const match = path.match(/\/(ko|en|ja|hi|id|vi|th|de|pt)\//);
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
      navigator.clipboard.writeText(text).then(() => {
        this.showToast('Copied to clipboard!');
      });
    } else {
      // Fallback for older browsers
      const textarea = document.createElement('textarea');
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      this.showToast('Copied to clipboard!');
    }
  },

  // Show toast notification
  showToast(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    toast.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #0f172a;
      color: white;
      padding: 1rem 1.5rem;
      border-radius: 0.5rem;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
      z-index: 1000;
      animation: slideIn 0.3s ease;
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
 * Analytics Helper (placeholder for Google Analytics)
 */
const Analytics = {
  trackEvent(category, action, label) {
    if (typeof gtag !== 'undefined') {
      gtag('event', action, {
        event_category: category,
        event_label: label
      });
    }
  },

  trackPageView(path) {
    if (typeof gtag !== 'undefined') {
      gtag('config', 'GA_MEASUREMENT_ID', {
        page_path: path
      });
    }
  }
};

/**
 * Initialize on DOM ready
 */
document.addEventListener('DOMContentLoaded', () => {
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
    installBtn.style.display = 'inline-flex';

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

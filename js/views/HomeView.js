/**
 * ============================================
 * HomeView - Home Page Rendering
 * ============================================
 */
class HomeView {
  constructor(container) {
    this.container = container;
    this.onDaySelect = null;
    this.onThemeToggle = null;
  }

  render(lessons, progress) {
    this.container.innerHTML = '';
    this.container.className = 'app-container home-view';

    const html = `
      <!-- Floating Decorations -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
      </div>

      <!-- Header -->
      <header class="app-header glass-card">
        <div class="header-left">
          <div class="logo">
            <span class="logo-icon">🎓</span>
            <span class="logo-text">Thien</span>
          </div>
        </div>
        <div class="header-stats">
          <div class="stat-item stat-xp" title="Điểm kinh nghiệm">
            <span class="stat-icon">⚡</span>
            <span class="stat-value" id="headerXP">${progress.xp}</span>
            <span class="stat-label">XP</span>
          </div>
          <div class="stat-item stat-streak" title="Chuỗi ngày học">
            <span class="stat-icon">🔥</span>
            <span class="stat-value" id="headerStreak">${progress.streak}</span>
            <span class="stat-label">Streak</span>
          </div>
          <div class="stat-item stat-level" title="Cấp độ">
            <span class="stat-icon">🏆</span>
            <span class="stat-value">Lv.${progress.getLevel()}</span>
          </div>
        </div>
        <div class="header-right">
          <button class="btn-icon theme-toggle" id="themeToggle" title="Đổi giao diện">
            <span class="theme-icon-dark">🌙</span>
            <span class="theme-icon-light">☀️</span>
          </button>
        </div>
      </header>

      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-content">
          <h1 class="hero-title">
            <span class="hero-greeting">${this._getGreeting()}</span>
            <span class="hero-main">Học Tiếng Anh Mỗi Ngày</span>
          </h1>
          <p class="hero-subtitle">Hành trình chinh phục tiếng Anh từ con số 0. Mỗi ngày một bước tiến! 🚀</p>
          
          <!-- Level Progress -->
          <div class="level-progress glass-card">
            <div class="level-info">
              <span>Level ${progress.getLevel()}</span>
              <span>${progress.xp % 500}/500 XP</span>
            </div>
            <div class="progress-bar">
              <div class="progress-fill gradient-accent" style="width: ${progress.getLevelProgress()}%"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Overall Stats -->
      <section class="stats-section">
        <div class="stats-grid">
          <div class="stats-card glass-card animate-in" style="--delay: 0.1s">
            <div class="stats-card-icon gradient-primary">📚</div>
            <div class="stats-card-value">${progress.completedDays.size}/${lessons.length}</div>
            <div class="stats-card-label">Bài đã học</div>
          </div>
          <div class="stats-card glass-card animate-in" style="--delay: 0.2s">
            <div class="stats-card-icon gradient-accent">⚡</div>
            <div class="stats-card-value">${progress.xp}</div>
            <div class="stats-card-label">Tổng XP</div>
          </div>
          <div class="stats-card glass-card animate-in" style="--delay: 0.3s">
            <div class="stats-card-icon gradient-success">🔥</div>
            <div class="stats-card-value">${progress.streak}</div>
            <div class="stats-card-label">Ngày liên tiếp</div>
          </div>
          <div class="stats-card glass-card animate-in" style="--delay: 0.4s">
            <div class="stats-card-icon gradient-warning">🏆</div>
            <div class="stats-card-value">Lv.${progress.getLevel()}</div>
            <div class="stats-card-label">Cấp độ</div>
          </div>
        </div>
      </section>

      <!-- Lesson Cards -->
      <section class="lessons-section">
        <h2 class="section-title">
          <span class="section-title-icon">📅</span>
          Lộ trình học tập
        </h2>
        <div class="lessons-grid">
          ${lessons.map((lesson, index) => this._renderDayCard(lesson, progress, index)).join('')}
        </div>
      </section>

      <!-- Footer -->
      <footer class="app-footer">
        <p>Thien — Học Tiếng Anh Mỗi Ngày 💙</p>
      </footer>
    `;

    this.container.innerHTML = html;
    this._bindEvents();
    this._animateCards();
  }

  _getGreeting() {
    const hour = new Date().getHours();
    if (hour < 12) return '🌅 Chào buổi sáng!';
    if (hour < 18) return '☀️ Chào buổi chiều!';
    return '🌙 Chào buổi tối!';
  }

  _renderDayCard(lesson, progress, index) {
    const isUnlocked = progress.isDayUnlocked(lesson.id);
    const isCompleted = progress.isDayCompleted(lesson.id);
    const dayProgress = progress.getDayProgress(lesson.id);
    
    let statusClass = 'locked';
    let statusIcon = '🔒';
    let statusText = 'Chưa mở khóa';

    if (isCompleted) {
      statusClass = 'completed';
      statusIcon = '✅';
      statusText = 'Hoàn thành';
    } else if (isUnlocked) {
      statusClass = 'available';
      statusIcon = '📖';
      statusText = dayProgress > 0 ? `Đang học (${dayProgress}%)` : 'Bắt đầu học';
    }

    return `
      <div class="day-card glass-card ${statusClass} animate-in" 
           style="--delay: ${0.1 + index * 0.1}s"
           data-day-id="${lesson.id}"
           ${!isUnlocked ? 'aria-disabled="true"' : ''}>
        <div class="day-card-header">
          <span class="day-number">Day ${lesson.day}</span>
          <span class="day-status-icon">${statusIcon}</span>
        </div>
        <div class="day-card-icon">${lesson.icon}</div>
        <h3 class="day-card-title">${lesson.title}</h3>
        <p class="day-card-subtitle">${lesson.subtitle}</p>
        <div class="day-card-meta">
          <span class="day-tense">📖 ${lesson.tense.name}</span>
          <span class="day-xp">⚡ ${lesson.xpReward} XP</span>
        </div>
        ${isUnlocked ? `
          <div class="day-card-progress">
            <div class="progress-bar progress-bar-sm">
              <div class="progress-fill ${isCompleted ? 'gradient-success' : 'gradient-primary'}" 
                   style="width: ${isCompleted ? 100 : dayProgress}%"></div>
            </div>
            <span class="progress-text">${isCompleted ? '100' : dayProgress}%</span>
          </div>
        ` : ''}
        <div class="day-card-status">${statusText}</div>
        ${!isUnlocked ? '<div class="day-card-lock-overlay"></div>' : ''}
      </div>
    `;
  }

  _bindEvents() {
    // Day card clicks
    this.container.querySelectorAll('.day-card:not(.locked)').forEach(card => {
      card.addEventListener('click', () => {
        const dayId = parseInt(card.dataset.dayId);
        if (this.onDaySelect) this.onDaySelect(dayId);
      });
    });

    // Locked card clicks - shake
    this.container.querySelectorAll('.day-card.locked').forEach(card => {
      card.addEventListener('click', () => {
        card.classList.add('shake');
        setTimeout(() => card.classList.remove('shake'), 600);
      });
    });

    // Theme toggle
    const toggle = this.container.querySelector('#themeToggle');
    if (toggle) {
      toggle.addEventListener('click', () => {
        if (this.onThemeToggle) this.onThemeToggle();
      });
    }
  }

  _animateCards() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    this.container.querySelectorAll('.animate-in').forEach(el => {
      observer.observe(el);
    });
  }
}

window.HomeView = HomeView;

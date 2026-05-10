/**
 * ============================================
 * AppController - Main Application Controller
 * ============================================
 * Coordinates between Models, Views, and Services.
 * Handles routing (home ↔ lesson) and state management.
 */
class AppController {
  constructor() {
    this.container = document.getElementById('app');

    // Services
    this.storage = new StorageService();
    this.audio = new AudioManager();

    // Models
    this.lessonModel = new LessonModel();
    this.progress = new ProgressModel(this.storage);

    // Views
    this.homeView = new HomeView(this.container);
    this.lessonView = new LessonView(this.container);

    // Theme
    this.theme = this.storage.load('theme', 'dark');
  }

  /** Initialize the application */
  async init() {
    this._applyTheme();
    this._initSpeechVoices();
    await this.lessonModel.init();
    this.showHome();
  }

  /** Show the home page */
  showHome() {
    this.homeView.onDaySelect = (dayId) => this._handleDaySelect(dayId);
    this.homeView.onThemeToggle = () => this._toggleTheme();
    this.homeView.render(this.lessonModel.getAll(), this.progress);
  }

  /** Show a lesson page */
  async showLesson(dayId) {
    if (!this.progress.isDayUnlocked(dayId)) return;
    
    // Add simple loading indicator
    this.container.innerHTML = '<div class="lesson-loading"><div class="spinner"></div><p>Đang tải bài học...</p></div>';

    const lesson = await this.lessonModel.getById(dayId);
    if (!lesson) {
      this.showHome();
      return;
    }

    this.lessonView.onBack = () => this.showHome();
    this.lessonView.onSectionComplete = (id, section) => this._handleSectionComplete(id, section);
    this.lessonView.onLessonComplete = (id) => this._handleLessonComplete(id);
    this.lessonView.render(lesson, this.progress, this.audio);
  }

  // ==================== PRIVATE HANDLERS ====================

  _handleDaySelect(dayId) {
    this.audio.playClick();
    this.showLesson(dayId);
  }

  _handleSectionComplete(dayId, sectionName) {
    this.progress.completeSection(dayId, sectionName);
    this.progress.addXP(20); // 20 XP per section
  }

  _handleLessonComplete(dayId) {
    const lesson = this.lessonModel.getCachedById(dayId);
    if (!lesson) return;

    const nextDay = dayId + 1;
    const hasNextDay = this.lessonModel.exists(nextDay);

    this.progress.completeDay(dayId, hasNextDay);
    this.progress.addXP(lesson.xpReward);
    this.audio.playComplete();

    // Check if next day was unlocked
    if (this.progress.isDayUnlocked(nextDay)) {
      this.audio.playUnlock();
    }
  }

  _toggleTheme() {
    this.theme = this.theme === 'dark' ? 'light' : 'dark';
    this.storage.save('theme', this.theme);
    this._applyTheme();
  }

  _applyTheme() {
    document.documentElement.setAttribute('data-theme', this.theme);
  }

  /** Pre-load speech synthesis voices */
  _initSpeechVoices() {
    if ('speechSynthesis' in window) {
      speechSynthesis.getVoices();
      speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
    }
  }
}

window.AppController = AppController;

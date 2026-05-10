/**
 * ============================================
 * ProgressModel - Tracks user progress
 * ============================================
 */
class ProgressModel {
  constructor(storageService) {
    this.storage = storageService;
    this._load();
  }

  _load() {
    const saved = this.storage.load('progress', null);
    if (saved) {
      this.xp = saved.xp || 0;
      this.streak = saved.streak || 0;
      this.lastActiveDate = saved.lastActiveDate || null;
      this.completedDays = new Set(saved.completedDays || []);
      this.unlockedDays = new Set(saved.unlockedDays || [1]); // Day 1 always unlocked
      this.sectionProgress = saved.sectionProgress || {};
    } else {
      this.xp = 0;
      this.streak = 0;
      this.lastActiveDate = null;
      this.completedDays = new Set();
      this.unlockedDays = new Set([1]);
      this.sectionProgress = {};
    }
    this._updateStreak();
  }

  _save() {
    this.storage.save('progress', {
      xp: this.xp,
      streak: this.streak,
      lastActiveDate: this.lastActiveDate,
      completedDays: [...this.completedDays],
      unlockedDays: [...this.unlockedDays],
      sectionProgress: this.sectionProgress
    });
  }

  _updateStreak() {
    const today = new Date().toDateString();
    if (this.lastActiveDate === today) return;

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    if (this.lastActiveDate === yesterday.toDateString()) {
      this.streak++;
    } else if (this.lastActiveDate !== today) {
      this.streak = this.streak > 0 ? 1 : 0;
    }
    this.lastActiveDate = today;
    this._save();
  }

  /** Mark a section as completed for a day */
  completeSection(dayId, sectionName) {
    const key = `day_${dayId}`;
    if (!this.sectionProgress[key]) {
      this.sectionProgress[key] = {};
    }
    this.sectionProgress[key][sectionName] = true;
    this._save();
  }

  /** Check if a section is completed */
  isSectionCompleted(dayId, sectionName) {
    const key = `day_${dayId}`;
    return !!(this.sectionProgress[key] && this.sectionProgress[key][sectionName]);
  }

  /** Get completed sections count for a day */
  getCompletedSectionsCount(dayId) {
    const key = `day_${dayId}`;
    if (!this.sectionProgress[key]) return 0;
    return Object.values(this.sectionProgress[key]).filter(v => v).length;
  }

  /** Total sections per day */
  get totalSections() {
    return 5; // grammar, vocabulary, listening, writing, quiz
  }

  /** Get day completion percentage */
  getDayProgress(dayId) {
    return Math.round((this.getCompletedSectionsCount(dayId) / this.totalSections) * 100);
  }

  /** Complete a full day */
  completeDay(dayId, hasNextDay = false) {
    this.completedDays.add(dayId);
    // Unlock next day if it exists
    if (hasNextDay) {
      this.unlockedDays.add(dayId + 1);
    }
    if (this.streak === 0) this.streak = 1;
    this._updateStreak();
    this._save();
  }

  /** Add XP points */
  addXP(amount) {
    this.xp += amount;
    this._save();
    return this.xp;
  }

  /** Check if a day is completed */
  isDayCompleted(dayId) {
    return this.completedDays.has(dayId);
  }

  /** Check if a day is unlocked */
  isDayUnlocked(dayId) {
    return this.unlockedDays.has(dayId);
  }

  /** Get level based on XP */
  getLevel() {
    return Math.floor(this.xp / 500) + 1;
  }

  /** Get XP needed for next level */
  getXPToNextLevel() {
    return 500 - (this.xp % 500);
  }

  /** Get level progress percentage */
  getLevelProgress() {
    return Math.round(((this.xp % 500) / 500) * 100);
  }
}

window.ProgressModel = ProgressModel;

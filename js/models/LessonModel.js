/**
 * ============================================
 * LessonModel - Lesson data access layer
 * ============================================
 */
class LessonModel {
  constructor() {
    this.lessonsIndex = [];
    this.loadedLessons = new Map();
  }

  /** Initialize and fetch lesson index */
  async init() {
    try {
      const response = await fetch('./data/lessons-index.json');
      if (!response.ok) throw new Error('Failed to fetch lesson index');
      this.lessonsIndex = await response.json();
    } catch (error) {
      console.error('Error loading lesson index:', error);
      this.lessonsIndex = [];
    }
  }

  /** Get all available lessons index */
  getAll() {
    return this.lessonsIndex;
  }

  /** Fetch a specific lesson by ID */
  async getById(id) {
    if (this.loadedLessons.has(id)) {
      return this.loadedLessons.get(id);
    }
    const lessonInfo = this.lessonsIndex.find(l => l.id === id);
    if (!lessonInfo) return null;

    try {
      const response = await fetch(`./data/lessons/${lessonInfo.file}`);
      if (!response.ok) throw new Error(`Failed to fetch lesson ${id}`);
      const lessonData = await response.json();
      this.loadedLessons.set(id, lessonData);
      return lessonData;
    } catch (error) {
      console.error(`Error loading lesson ${id}:`, error);
      return null;
    }
  }

  /** Get a cached lesson by ID */
  getCachedById(id) {
    return this.loadedLessons.get(id) || null;
  }

  /** Get total number of lessons */
  getTotal() {
    return this.lessonsIndex.length;
  }

  /** Check if a lesson exists */
  exists(id) {
    return this.lessonsIndex.some(l => l.id === id);
  }

  /** Get all section names */
  getSectionNames() {
    return ['grammar', 'vocabulary', 'listening', 'writing', 'quiz'];
  }

  /** Get section labels (Vietnamese) */
  getSectionLabels() {
    return {
      grammar: { icon: '📖', label: 'Ngữ pháp' },
      vocabulary: { icon: '📝', label: 'Từ vựng' },
      listening: { icon: '🎧', label: 'Nghe & Nói' },
      writing: { icon: '✍️', label: 'Viết' },
      quiz: { icon: '✅', label: 'Trắc nghiệm' }
    };
  }
}

window.LessonModel = LessonModel;

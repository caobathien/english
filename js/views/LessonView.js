/**
 * ============================================
 * LessonView - Lesson Page Rendering
 * ============================================
 * Multi-section lesson view with tabs for:
 * Grammar, Vocabulary, Listening, Writing, Quiz
 */
class LessonView {
  constructor(container) {
    this.container = container;
    this.lesson = null;
    this.progress = null;
    this.audioManager = null;
    this.currentSection = 0;
    this.sections = ['grammar', 'vocabulary', 'listening', 'writing', 'quiz'];
    this.quizState = {};
    this.writingState = {};

    // Callbacks
    this.onBack = null;
    this.onSectionComplete = null;
    this.onLessonComplete = null;
  }

  render(lesson, progress, audioManager) {
    this.lesson = lesson;
    this.progress = progress;
    this.audioManager = audioManager;
    this.quizState = { current: 0, score: 0, answered: {} };
    this.writingState = { answered: {} };
    this.container.innerHTML = '';
    this.container.className = 'app-container lesson-view';

    // Determine which section to show first
    this.currentSection = 0;
    for (let i = 0; i < this.sections.length; i++) {
      if (!progress.isSectionCompleted(lesson.id, this.sections[i])) {
        this.currentSection = i;
        break;
      }
      if (i === this.sections.length - 1) this.currentSection = 0;
    }

    const sectionLabels = new LessonModel().getSectionLabels();
    const totalProgress = progress.getDayProgress(lesson.id);

    const html = `
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>

      <header class="lesson-header glass-card">
        <button class="btn-back" id="btnBack">
          <span>←</span> Trang chủ
        </button>
        <div class="lesson-header-info">
          <h2>Day ${lesson.day}</h2>
          <span class="lesson-header-title">${lesson.title}</span>
        </div>
        <div class="lesson-header-progress">
          <div class="progress-bar">
            <div class="progress-fill gradient-primary" id="lessonProgressBar" style="width: ${totalProgress}%"></div>
          </div>
          <span class="progress-text" id="lessonProgressText">${totalProgress}%</span>
        </div>
      </header>

      <nav class="section-tabs glass-card">
        ${this.sections.map((sec, i) => {
          const label = sectionLabels[sec];
          const completed = progress.isSectionCompleted(lesson.id, sec);
          return `
            <button class="section-tab ${i === this.currentSection ? 'active' : ''} ${completed ? 'completed' : ''}" 
                    data-section="${i}">
              <span class="tab-icon">${completed ? '✅' : label.icon}</span>
              <span class="tab-label">${label.label}</span>
            </button>`;
        }).join('')}
      </nav>

      <main class="lesson-content">
        <div class="section-container" id="sectionContainer">
          ${this._renderCurrentSection()}
        </div>
      </main>

      <nav class="section-nav">
        <button class="btn btn-secondary" id="btnPrev" ${this.currentSection === 0 ? 'disabled' : ''}>
          ← Trước
        </button>
        <span class="section-indicator">${this.currentSection + 1} / ${this.sections.length}</span>
        <button class="btn btn-primary" id="btnNext">
          ${this.currentSection === this.sections.length - 1 ? 'Hoàn thành' : 'Tiếp →'}
        </button>
      </nav>
    `;

    this.container.innerHTML = html;
    this._bindEvents();
  }

  _renderCurrentSection() {
    const section = this.sections[this.currentSection];
    switch (section) {
      case 'grammar': return this._renderGrammar();
      case 'vocabulary': return this._renderVocabulary();
      case 'listening': return this._renderListening();
      case 'writing': return this._renderWriting();
      case 'quiz': return this._renderQuiz();
      default: return '';
    }
  }

  // ==================== GRAMMAR ====================
  _renderGrammar() {
    const t = this.lesson.tense;
    return `
      <div class="section-content grammar-section animate-fade-in">
        <div class="section-header">
          <h2 class="section-title">📖 ${t.name}</h2>
          <p class="section-subtitle">${t.nameVi} — ${t.description}</p>
        </div>

        <div class="grammar-rules">
          ${t.rules.map((rule, i) => `
            <div class="grammar-card glass-card animate-in" style="--delay: ${0.1 + i * 0.15}s">
              <h3 class="grammar-card-title">${rule.title}</h3>
              <div class="grammar-formula">${rule.formula}</div>
              <div class="grammar-examples">
                ${rule.examples.map(ex => `
                  <div class="grammar-example">
                    <div class="example-en">
                      <span class="example-label">EN</span>
                      <span>${ex.en}</span>
                      <button class="btn-speak" data-text="${ex.en}" title="Nghe phát âm">🔊</button>
                    </div>
                    <div class="example-vi">
                      <span class="example-label">VI</span>
                      <span>${ex.vi}</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>

        ${t.signals && t.signals.length > 0 ? `
        <div class="grammar-signals glass-card animate-in" style="--delay: 0.5s">
          <h3>🔍 Dấu hiệu nhận biết</h3>
          <div class="signal-tags">
            ${t.signals.map(s => `<span class="signal-tag">${s}</span>`).join('')}
          </div>
        </div>
        ` : ''}

        <button class="btn btn-success btn-complete-section" data-section="grammar">
          ✅ Đã hiểu! Tiếp tục
        </button>
      </div>
    `;
  }

  // ==================== VOCABULARY ====================
  _renderVocabulary() {
    return `
      <div class="section-content vocabulary-section animate-fade-in">
        <div class="section-header">
          <h2 class="section-title">📝 Từ vựng</h2>
          <p class="section-subtitle">Học ${this.lesson.vocabulary.length} từ vựng — Nhấn vào thẻ để lật!</p>
        </div>

        <div class="vocab-grid">
          ${this.lesson.vocabulary.map((v, i) => `
            <div class="vocab-card animate-in" style="--delay: ${i * 0.08}s" data-vocab-id="${v.id}">
              <div class="vocab-card-inner">
                <div class="vocab-card-front">
                  <span class="vocab-word">${v.word}</span>
                  <span class="vocab-phonetic">${v.phonetic}</span>
                  <button class="btn-speak vocab-speak" data-text="${v.word}" title="Nghe phát âm">
                    🔊
                  </button>
                </div>
                <div class="vocab-card-back">
                  <span class="vocab-meaning">${v.meaning}</span>
                  <div class="vocab-example">
                    <p class="vocab-example-en">"${v.example}"</p>
                    <p class="vocab-example-vi">${v.exampleVi}</p>
                  </div>
                  <button class="btn-speak" data-text="${v.example}" title="Nghe ví dụ">
                    🔊 Nghe ví dụ
                  </button>
                </div>
              </div>
            </div>
          `).join('')}
        </div>

        <button class="btn btn-success btn-complete-section" data-section="vocabulary">
          ✅ Đã học xong từ vựng
        </button>
      </div>
    `;
  }

  // ==================== LISTENING ====================
  _renderListening() {
    return `
      <div class="section-content listening-section animate-fade-in">
        <div class="section-header">
          <h2 class="section-title">🎧 Nghe & Nói</h2>
          <p class="section-subtitle">Nghe AI đọc và lặp lại theo</p>
        </div>

        <div class="listening-list">
          ${this.lesson.listening.map((item, i) => `
            <div class="listening-item glass-card animate-in" style="--delay: ${i * 0.1}s">
              <div class="listening-number">${i + 1}</div>
              <div class="listening-content">
                <p class="listening-en">${item.sentence}</p>
                <p class="listening-vi">${item.sentenceVi}</p>
              </div>
              <div class="listening-controls">
                <button class="btn-listen" data-text="${item.sentence}" title="Nghe">
                  <span class="listen-icon">▶️</span>
                  <div class="waveform">
                    <span class="wave-bar"></span>
                    <span class="wave-bar"></span>
                    <span class="wave-bar"></span>
                    <span class="wave-bar"></span>
                    <span class="wave-bar"></span>
                  </div>
                </button>
                <button class="btn-listen-slow" data-text="${item.sentence}" title="Nghe chậm">
                  🐢 Chậm
                </button>
              </div>
            </div>
          `).join('')}
        </div>

        <div class="listening-tip glass-card animate-in" style="--delay: 0.6s">
          <span class="tip-icon">💡</span>
          <p>Mẹo: Hãy lắng nghe cẩn thận rồi đọc lại to theo. Lặp lại ít nhất 3 lần mỗi câu!</p>
        </div>

        <button class="btn btn-success btn-complete-section" data-section="listening">
          ✅ Đã luyện nghe xong
        </button>
      </div>
    `;
  }

  // ==================== WRITING ====================
  _renderWriting() {
    return `
      <div class="section-content writing-section animate-fade-in">
        <div class="section-header">
          <h2 class="section-title">✍️ Luyện viết</h2>
          <p class="section-subtitle">Hoàn thành các bài tập dưới đây</p>
        </div>

        <div class="writing-exercises">
          ${this.lesson.writing.map((w, i) => `
            <div class="writing-item glass-card animate-in" style="--delay: ${i * 0.1}s" data-writing-id="${w.id}">
              <div class="writing-header">
                <span class="writing-number">${i + 1}</span>
                <span class="writing-type">${w.instruction}</span>
              </div>
              <div class="writing-question">
                <p>${this._formatWritingQuestion(w.question)}</p>
              </div>
              <div class="writing-input-group">
                <input type="text" class="writing-input" 
                       placeholder="Nhập đáp án..." 
                       data-answer="${w.type === 'dialog' ? w.answerPattern : w.answer}"
                       data-type="${w.type}"
                       data-id="${w.id}"
                       autocomplete="off">
                <button class="btn btn-primary btn-check-writing" data-id="${w.id}">
                  Kiểm tra
                </button>
              </div>
              <div class="writing-hint">
                <span class="hint-icon">💡</span> ${w.hint}
              </div>
              <div class="writing-feedback" id="feedback-${w.id}"></div>
            </div>
          `).join('')}
        </div>

        <button class="btn btn-success btn-complete-section" data-section="writing" id="btnCompleteWriting" disabled>
          ✅ Hoàn thành luyện viết
        </button>
      </div>
    `;
  }

  _formatWritingQuestion(question) {
    return question.replace(/_____/g, '<span class="blank-space">_____</span>');
  }

  // ==================== QUIZ ====================
  _renderQuiz() {
    const q = this.lesson.quizzes;
    return `
      <div class="section-content quiz-section animate-fade-in">
        <div class="section-header">
          <h2 class="section-title">✅ Trắc nghiệm</h2>
          <p class="section-subtitle">Trả lời ${q.length} câu hỏi</p>
        </div>

        <div class="quiz-progress-bar">
          <div class="progress-bar">
            <div class="progress-fill gradient-accent" id="quizProgressFill" style="width: 0%"></div>
          </div>
          <span class="quiz-progress-text" id="quizProgressText">0/${q.length}</span>
        </div>

        <div class="quiz-container" id="quizContainer">
          ${this._renderQuizQuestion(0)}
        </div>

        <div class="quiz-score glass-card" id="quizScore" style="display:none;">
          <div class="score-icon">🎉</div>
          <h3>Kết quả</h3>
          <div class="score-value" id="scoreValue"></div>
          <p class="score-message" id="scoreMessage"></p>
        </div>
      </div>
    `;
  }

  _renderQuizQuestion(index) {
    if (index >= this.lesson.quizzes.length) return '';
    const q = this.lesson.quizzes[index];
    const answered = this.quizState.answered[index];

    return `
      <div class="quiz-question animate-fade-in" data-quiz-index="${index}">
        <div class="quiz-question-header">
          <span class="quiz-number">Câu ${index + 1}/${this.lesson.quizzes.length}</span>
        </div>
        <h3 class="quiz-question-text">${q.question}</h3>
        <div class="quiz-options">
          ${q.options.map((opt, oi) => `
            <button class="quiz-option ${answered !== undefined ? (oi === q.correct ? 'correct' : (oi === answered ? 'wrong' : '')) : ''}" 
                    data-quiz-index="${index}" 
                    data-option-index="${oi}"
                    ${answered !== undefined ? 'disabled' : ''}>
              <span class="option-letter">${String.fromCharCode(65 + oi)}</span>
              <span class="option-text">${opt}</span>
              ${answered !== undefined && oi === q.correct ? '<span class="option-check">✓</span>' : ''}
              ${answered !== undefined && oi === answered && oi !== q.correct ? '<span class="option-cross">✗</span>' : ''}
            </button>
          `).join('')}
        </div>
        ${answered !== undefined ? `
          <button class="btn btn-primary quiz-next" data-next="${index + 1}">
            ${index + 1 >= this.lesson.quizzes.length ? '🎉 Xem kết quả' : 'Câu tiếp →'}
          </button>
        ` : ''}
      </div>
    `;
  }

  // ==================== EVENT BINDING ====================
  _bindEvents() {
    const container = this.container;

    // Back button
    container.querySelector('#btnBack')?.addEventListener('click', () => {
      if (this.onBack) this.onBack();
    });

    // Section tabs
    container.querySelectorAll('.section-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const idx = parseInt(tab.dataset.section);
        this._switchSection(idx);
      });
    });

    // Previous / Next buttons
    container.querySelector('#btnPrev')?.addEventListener('click', () => {
      if (this.currentSection > 0) this._switchSection(this.currentSection - 1);
    });

    container.querySelector('#btnNext')?.addEventListener('click', () => {
      if (this.currentSection < this.sections.length - 1) {
        this._switchSection(this.currentSection + 1);
      } else {
        this._handleLessonFinish();
      }
    });

    // Delegate all interactive events
    container.addEventListener('click', (e) => {
      const target = e.target.closest('[data-text]');
      if (target) {
        if (target.classList.contains('btn-listen-slow')) {
          this._handleSpeak(target.dataset.text, 0.6);
          target.closest('.listening-item')?.classList.add('playing');
        } else if (target.classList.contains('btn-speak') || target.classList.contains('btn-listen') || target.classList.contains('vocab-speak')) {
          this._handleSpeak(target.dataset.text);
          target.closest('.listening-item')?.classList.add('playing');
        }
      }

      // Vocab card flip
      const vocabCard = e.target.closest('.vocab-card');
      if (vocabCard && !e.target.closest('.btn-speak')) {
        vocabCard.classList.toggle('flipped');
        this.audioManager?.playClick();
      }

      // Complete section
      const completeBtn = e.target.closest('.btn-complete-section');
      if (completeBtn) {
        const section = completeBtn.dataset.section;
        this._handleSectionComplete(section);
      }

      // Check writing
      const checkBtn = e.target.closest('.btn-check-writing');
      if (checkBtn) {
        this._handleWritingCheck(checkBtn.dataset.id);
      }

      // Quiz option
      const quizOpt = e.target.closest('.quiz-option:not([disabled])');
      if (quizOpt) {
        this._handleQuizAnswer(
          parseInt(quizOpt.dataset.quizIndex),
          parseInt(quizOpt.dataset.optionIndex)
        );
      }

      // Quiz next
      const quizNext = e.target.closest('.quiz-next');
      if (quizNext) {
        const nextIdx = parseInt(quizNext.dataset.next);
        this._handleQuizNext(nextIdx);
      }
    });

    // Writing input enter key
    container.querySelectorAll('.writing-input').forEach(input => {
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          this._handleWritingCheck(input.dataset.id);
        }
      });
    });
  }

  // ==================== HANDLERS ====================
  async _handleSpeak(text, rate = 0.9) {
    if (this.audioManager) {
      await this.audioManager.speak(text, 'en-US', rate);
      this.container.querySelectorAll('.listening-item.playing').forEach(el => {
        el.classList.remove('playing');
      });
    }
  }

  _handleWritingCheck(id) {
    const input = this.container.querySelector(`.writing-input[data-id="${id}"]`);
    const feedback = this.container.querySelector(`#feedback-${id}`);
    if (!input || !feedback) return;

    const userAnswer = input.value.trim().toLowerCase();
    const correctAnswer = input.dataset.answer.toLowerCase();
    const type = input.dataset.type;

    let isCorrect = false;
    if (type === 'dialog') {
      isCorrect = userAnswer.includes(correctAnswer);
    } else {
      isCorrect = userAnswer === correctAnswer;
    }

    this.writingState.answered[id] = true;

    if (isCorrect) {
      feedback.innerHTML = '<span class="feedback-correct">✅ Chính xác! Tuyệt vời!</span>';
      feedback.className = 'writing-feedback show correct';
      input.classList.add('input-correct');
      this.audioManager?.playCorrect();
    } else {
      const answer = type === 'dialog' ? `Gợi ý: "${input.dataset.answer}..."` : `Đáp án: "${input.dataset.answer}"`;
      feedback.innerHTML = `<span class="feedback-wrong">❌ Chưa đúng. ${answer}</span>`;
      feedback.className = 'writing-feedback show wrong';
      input.classList.add('input-wrong');
      this.audioManager?.playWrong();
    }

    // Check if all writing exercises answered
    const totalWriting = this.lesson.writing.length;
    const answeredCount = Object.keys(this.writingState.answered).length;
    if (answeredCount >= totalWriting) {
      const btn = this.container.querySelector('#btnCompleteWriting');
      if (btn) btn.disabled = false;
    }
  }

  _handleQuizAnswer(qIndex, optIndex) {
    const q = this.lesson.quizzes[qIndex];
    this.quizState.answered[qIndex] = optIndex;
    if (optIndex === q.correct) {
      this.quizState.score++;
      this.audioManager?.playCorrect();
    } else {
      this.audioManager?.playWrong();
    }

    // Update quiz progress
    const answered = Object.keys(this.quizState.answered).length;
    const total = this.lesson.quizzes.length;
    const fill = this.container.querySelector('#quizProgressFill');
    const text = this.container.querySelector('#quizProgressText');
    if (fill) fill.style.width = `${(answered / total) * 100}%`;
    if (text) text.textContent = `${answered}/${total}`;

    // Re-render question with answer
    const qContainer = this.container.querySelector('#quizContainer');
    if (qContainer) {
      qContainer.innerHTML = this._renderQuizQuestion(qIndex);
    }
  }

  _handleQuizNext(nextIndex) {
    const total = this.lesson.quizzes.length;
    if (nextIndex >= total) {
      // Show results
      this._showQuizResults();
      return;
    }
    const qContainer = this.container.querySelector('#quizContainer');
    if (qContainer) {
      qContainer.innerHTML = this._renderQuizQuestion(nextIndex);
    }
  }

  _showQuizResults() {
    const total = this.lesson.quizzes.length;
    const score = this.quizState.score;
    const pct = Math.round((score / total) * 100);
    const qContainer = this.container.querySelector('#quizContainer');
    const scoreDiv = this.container.querySelector('#quizScore');

    if (qContainer) qContainer.style.display = 'none';
    if (scoreDiv) {
      scoreDiv.style.display = 'block';
      scoreDiv.querySelector('#scoreValue').textContent = `${score}/${total} (${pct}%)`;
      let msg = '';
      if (pct === 100) msg = '🏆 Xuất sắc! Bạn đã trả lời đúng tất cả!';
      else if (pct >= 70) msg = '👍 Tốt lắm! Hãy tiếp tục cố gắng!';
      else msg = '💪 Cần ôn lại thêm. Đừng bỏ cuộc nhé!';
      scoreDiv.querySelector('#scoreMessage').textContent = msg;
    }

    this.audioManager?.playComplete();
    this._handleSectionComplete('quiz');
  }

  _handleSectionComplete(sectionName) {
    if (this.onSectionComplete) {
      this.onSectionComplete(this.lesson.id, sectionName);
    }

    // Update tab UI
    const idx = this.sections.indexOf(sectionName);
    const tabs = this.container.querySelectorAll('.section-tab');
    if (tabs[idx]) {
      tabs[idx].classList.add('completed');
      tabs[idx].querySelector('.tab-icon').textContent = '✅';
    }

    // Update progress bar
    const newProgress = this.progress.getDayProgress(this.lesson.id);
    const bar = this.container.querySelector('#lessonProgressBar');
    const text = this.container.querySelector('#lessonProgressText');
    if (bar) bar.style.width = `${newProgress}%`;
    if (text) text.textContent = `${newProgress}%`;

    // Check if all sections completed
    if (newProgress >= 100) {
      setTimeout(() => this._handleLessonFinish(), 500);
    }
  }

  _handleLessonFinish() {
    const allComplete = this.sections.every(s => 
      this.progress.isSectionCompleted(this.lesson.id, s)
    );

    if (allComplete && !this.progress.isDayCompleted(this.lesson.id)) {
      if (this.onLessonComplete) {
        this.onLessonComplete(this.lesson.id);
      }
      this._showCompletionScreen();
    }
  }

  _showCompletionScreen() {
    this.audioManager?.playComplete();
    
    const overlay = document.createElement('div');
    overlay.className = 'completion-overlay animate-fade-in';
    overlay.innerHTML = `
      <div class="completion-modal glass-card animate-scale-in">
        <div class="completion-confetti">🎉</div>
        <h2 class="completion-title">Chúc mừng!</h2>
        <p class="completion-subtitle">Bạn đã hoàn thành Day ${this.lesson.day}!</p>
        <div class="completion-stats">
          <div class="completion-stat">
            <span class="completion-stat-value">+${this.lesson.xpReward}</span>
            <span class="completion-stat-label">XP earned</span>
          </div>
          <div class="completion-stat">
            <span class="completion-stat-value">⚡</span>
            <span class="completion-stat-label">Level Up!</span>
          </div>
        </div>
        <button class="btn btn-primary btn-lg" id="btnGoHome">
          🏠 Về trang chủ
        </button>
      </div>
    `;

    this.container.appendChild(overlay);

    overlay.querySelector('#btnGoHome')?.addEventListener('click', () => {
      overlay.remove();
      if (this.onBack) this.onBack();
    });
  }

  _switchSection(index) {
    if (index === this.currentSection) return;
    this.currentSection = index;
    this.audioManager?.playClick();

    // Update tabs
    this.container.querySelectorAll('.section-tab').forEach((tab, i) => {
      tab.classList.toggle('active', i === index);
    });

    // Update content
    const sectionContainer = this.container.querySelector('#sectionContainer');
    if (sectionContainer) {
      sectionContainer.innerHTML = this._renderCurrentSection();
    }

    // Update nav buttons
    const prev = this.container.querySelector('#btnPrev');
    const next = this.container.querySelector('#btnNext');
    const indicator = this.container.querySelector('.section-indicator');
    if (prev) prev.disabled = index === 0;
    if (next) next.textContent = index === this.sections.length - 1 ? 'Hoàn thành' : 'Tiếp →';
    if (indicator) indicator.textContent = `${index + 1} / ${this.sections.length}`;

    // Rebind events for new section
    this._bindSectionEvents();

    // Scroll to top
    this.container.querySelector('.lesson-content')?.scrollTo(0, 0);
  }

  _bindSectionEvents() {
    // Re-delegate writing enter keys
    this.container.querySelectorAll('.writing-input').forEach(input => {
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          this._handleWritingCheck(input.dataset.id);
        }
      });
    });

    // Animate new cards
    this.container.querySelectorAll('.animate-in').forEach(el => {
      setTimeout(() => el.classList.add('visible'), 50);
    });
  }
}

window.LessonView = LessonView;

/**
 * ============================================
 * App Entry Point - English Every Day
 * ============================================
 */
document.addEventListener('DOMContentLoaded', async () => {
  const app = new AppController();
  await app.init();
});

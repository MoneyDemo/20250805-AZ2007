// main.js
// Handles theme toggling and global event bindings

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    setTheme(currentTheme);
    
    themeToggleBtn.addEventListener('click', () => {
        const newTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
        setTheme(newTheme);
    });

    // Enter key triggers search
    const stockInput = document.getElementById('stock-code-input');
    stockInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            document.getElementById('search-btn').click();
        }
    });
});

/**
 * Set application theme
 * @param {string} theme - 'light' or 'dark'
 */
function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    // Update icon
    const icon = document.querySelector('#theme-toggle i');
    if (theme === 'dark') {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    }
}

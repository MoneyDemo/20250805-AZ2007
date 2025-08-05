// stock-display.js
// Handles stock data fetching and dynamic UI updates

let refreshTimer = null;

/**
 * Fetch stock data from API and update UI.
 * @param {string} code - Stock code to query.
 */
async function fetchAndDisplay(code) {
    const infoDiv = document.getElementById('stock-info');
    // Clear previous content
    infoDiv.innerHTML = '';

    // Show loading spinner
    const spinner = document.createElement('div');
    spinner.className = 'spinner-container';
    spinner.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';
    infoDiv.appendChild(spinner);

    try {
        const response = await fetch(`/api/stock/${encodeURIComponent(code)}`);
        if (!response.ok) {
            const error = await response.json();
            infoDiv.innerHTML = `<div class="alert alert-danger">${error.error}</div>`;
            return;
        }
        const data = await response.json();
        infoDiv.innerHTML = generateCard(data);
    } catch (err) {
        infoDiv.innerHTML = `<div class="alert alert-danger">${err.message}</div>`;
    }
}

/**
 * Generate HTML card for stock data.
 * @param {object} data - Stock data object.
 * @returns {string} HTML string.
 */
function generateCard(data) {
    return `
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">${data.code}</h5>
            <p class="card-text fs-3">價格：${data.price}</p>
            <p class="card-text"><small class="text-muted">時間：${new Date(data.timestamp).toLocaleTimeString()}</small></p>
        </div>
    </div>`;
}

/**
 * Setup search and refresh controls.
 */
function setupControls() {
    const searchBtn = document.getElementById('search-btn');
    const stockInput = document.getElementById('stock-code-input');
    const refreshSelect = document.getElementById('refresh-interval');

    searchBtn.addEventListener('click', () => {
        const code = stockInput.value.trim();
        if (code) fetchAndDisplay(code);
        resetTimer(code);
    });

    refreshSelect.addEventListener('change', () => {
        const code = stockInput.value.trim();
        resetTimer(code);
    });
}

/**
 * Reset the auto-refresh timer based on selected interval.
 * @param {string} code - Stock code to refresh.
 */
function resetTimer(code) {
    const interval = parseInt(document.getElementById('refresh-interval').value, 10);
    if (refreshTimer) clearInterval(refreshTimer);
    if (interval > 0 && code) {
        refreshTimer = setInterval(() => fetchAndDisplay(code), interval * 1000);
    }
}

// Initialize controls on DOM loaded
document.addEventListener('DOMContentLoaded', () => {
    setupControls();
    // Note: default code initialization moved to template
});

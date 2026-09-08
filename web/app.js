/**
 * Women Safety Intelligence AI — Custom High-Performance Web Application
 */

let globalData = [];
let chartInstances = {};
let leafletMap = null;

// Initialize Web Application
document.addEventListener('DOMContentLoaded', async () => {
    setupTabNavigation();
    await loadDataset();
    initializeExplorer();
    initializeCalculator();
    initializeMatrix();
    initializeMap();
    renderOverviewCharts();
});

// Tab Navigation Logic
function setupTabNavigation() {
    const navItems = document.querySelectorAll('.nav-item, .top-nav-item');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');
            switchTab(targetTab);
        });
    });
}

function switchTab(targetTab) {
    const navItems = document.querySelectorAll('.nav-item, .top-nav-item');
    const tabPages = document.querySelectorAll('.tab-page');

    navItems.forEach(n => n.classList.remove('active'));
    tabPages.forEach(p => p.classList.remove('active'));

    const activeBtns = document.querySelectorAll(`[data-tab="${targetTab}"]`);
    activeBtns.forEach(btn => btn.classList.add('active'));

    const targetPage = document.getElementById(`tab-${targetTab}`);
    if (targetPage) {
        targetPage.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    if (targetTab === 'gis-map' && leafletMap) {
        setTimeout(() => leafletMap.invalidateSize(), 200);
    }
}


// Load JSON Dataset
async function loadDataset() {
    try {
        const response = await fetch('data.json');
        globalData = await response.json();
        console.log(`Loaded ${globalData.length} records!`);
    } catch (err) {
        console.error('Failed to load data.json:', err);
    }
}

// Overview Dashboard Charts
function renderOverviewCharts() {
    if (!globalData.length) return;

    const data2026 = globalData.filter(d => d.year === 2026);
    const top2026 = [...data2026].sort((a, b) => b.crime_rate - a.crime_rate).slice(0, 15);

    // Overview Ranking Chart
    const ctxRank = document.getElementById('overview-ranking-chart').getContext('2d');
    if (chartInstances['overviewRank']) chartInstances['overviewRank'].destroy();

    chartInstances['overviewRank'] = new Chart(ctxRank, {
        type: 'bar',
        data: {
            labels: top2026.map(d => d.city),
            datasets: [{
                label: '2026 Projected Crime Rate (per 100k)',
                data: top2026.map(d => d.crime_rate),
                backgroundColor: top2026.map(d => d.risk_label === 'HIGH' ? '#ef4444' : (d.risk_label === 'MEDIUM' ? '#f59e0b' : '#10b981')),
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } }, grid: { display: false } },
                y: { ticks: { color: '#9ca3af' }, grid: { color: 'rgba(255,255,255,0.06)' } }
            }
        }
    });

    // Overview Category Doughnut
    const ctxCat = document.getElementById('overview-category-chart').getContext('2d');
    if (chartInstances['overviewCat']) chartInstances['overviewCat'].destroy();

    const sumRape = data2026.reduce((s, d) => s + (d.rape_cases || 0), 0);
    const sumKidnapp = data2026.reduce((s, d) => s + (d.kidnapping_abduction_cases || 0), 0);
    const sumDowry = data2026.reduce((s, d) => s + (d.dowry_death_cases || 0), 0);
    const sumAssault = data2026.reduce((s, d) => s + (d.assault_on_modesty_cases || 0), 0);
    const sumCruelty = data2026.reduce((s, d) => s + (d.cruelty_498a_cases || 0), 0);

    chartInstances['overviewCat'] = new Chart(ctxCat, {
        type: 'doughnut',
        data: {
            labels: ['Rape', 'Kidnapping & Abduction', 'Dowry Death', 'Assault on Modesty', 'Cruelty (IPC 498A)'],
            datasets: [{
                data: [sumRape, sumKidnapp, sumDowry, sumAssault, sumCruelty],
                backgroundColor: ['#6366f1', '#ec4899', '#f59e0b', '#10b981', '#06b6d4'],
                borderWidth: 2,
                borderColor: '#0f172a'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'right', labels: { color: '#e5e7eb', font: { family: 'Plus Jakarta Sans' } } } }
        }
    });
}

// City Explorer Logic
function initializeExplorer() {
    if (!globalData.length) return;

    const stateSelect = document.getElementById('explorer-state-select');
    const citySelect = document.getElementById('explorer-city-select');
    const yearSlider = document.getElementById('explorer-year-slider');
    const yearVal = document.getElementById('explorer-year-val');

    // Populate States
    const states = [...new Set(globalData.map(d => d.state))].sort();
    stateSelect.innerHTML = states.map(s => `<option value="${s}" ${s === 'Karnataka' ? 'selected' : ''}>${s}</option>`).join('');

    function updateCityDropdown() {
        const selectedState = stateSelect.value;
        const cities = [...new Set(globalData.filter(d => d.state === selectedState).map(d => d.city))].sort();
        citySelect.innerHTML = cities.map(c => `<option value="${c}">${c}</option>`).join('');
        renderCityProfile();
    }

    function renderCityProfile() {
        const city = citySelect.value;
        const year = parseInt(yearSlider.value);
        yearVal.innerText = year;

        const row = globalData.find(d => d.city === city && d.year === year);
        if (!row) return;

        document.getElementById('profile-city-name').innerText = row.city;
        document.getElementById('profile-state-name').innerHTML = `State: <b>${row.state}</b> &bull; Year: <b>${row.year}</b>`;

        const badge = document.getElementById('profile-risk-badge');
        badge.className = `risk-badge-large ${row.risk_label}`;
        badge.innerText = `${row.risk_label} RISK TIER`;

        document.getElementById('profile-rate').innerText = row.crime_rate.toFixed(2);
        document.getElementById('profile-crimes').innerText = row.total_crimes_against_women.toLocaleString();
        document.getElementById('profile-pop').innerText = (row.population / 1000000).toFixed(2) + ' Million';

        // Delta YoY
        const prevRow = globalData.find(d => d.city === city && d.year === year - 1);
        if (prevRow) {
            const diff = row.crime_rate - prevRow.crime_rate;
            document.getElementById('profile-rate-delta').innerText = `${diff >= 0 ? '+' : ''}${diff.toFixed(2)} vs ${year-1}`;
            document.getElementById('profile-trajectory').innerText = diff >= 0 ? 'Rising ↑' : 'Declining ↓';
        } else {
            document.getElementById('profile-rate-delta').innerText = 'Baseline year';
            document.getElementById('profile-trajectory').innerText = 'Stable';
        }

        renderCityCharts(city, year);
    }

    stateSelect.addEventListener('change', updateCityDropdown);
    citySelect.addEventListener('change', renderCityProfile);
    yearSlider.addEventListener('input', renderCityProfile);

    updateCityDropdown();
}

// Render City Specific Charts
function renderCityCharts(city, selectedYear) {
    const citySeries = globalData.filter(d => d.city === city).sort((a, b) => a.year - b.year);

    // Line Chart
    const ctxTrend = document.getElementById('city-trend-chart').getContext('2d');
    if (chartInstances['cityTrend']) chartInstances['cityTrend'].destroy();

    chartInstances['cityTrend'] = new Chart(ctxTrend, {
        type: 'line',
        data: {
            labels: citySeries.map(d => d.year),
            datasets: [{
                label: 'Crime Rate (per 100k)',
                data: citySeries.map(d => d.crime_rate),
                borderColor: '#6366f1',
                backgroundColor: 'rgba(99, 102, 241, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.35,
                pointRadius: citySeries.map(d => d.year === 2026 ? 8 : 4),
                pointBackgroundColor: citySeries.map(d => d.year === 2026 ? '#ef4444' : '#818cf8')
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#9ca3af' }, grid: { display: false } },
                y: { ticks: { color: '#9ca3af' }, grid: { color: 'rgba(255,255,255,0.06)' } }
            }
        }
    });

    // Category Pie Chart
    const row = citySeries.find(d => d.year === selectedYear);
    const ctxCat = document.getElementById('city-category-chart').getContext('2d');
    if (chartInstances['cityCat']) chartInstances['cityCat'].destroy();

    if (row) {
        chartInstances['cityCat'] = new Chart(ctxCat, {
            type: 'doughnut',
            data: {
                labels: ['Rape', 'Kidnapping & Abduction', 'Dowry Death', 'Assault on Modesty', 'Cruelty (IPC 498A)'],
                datasets: [{
                    data: [
                        row.rape_cases || 0,
                        row.kidnapping_abduction_cases || 0,
                        row.dowry_death_cases || 0,
                        row.assault_on_modesty_cases || 0,
                        row.cruelty_498a_cases || 0
                    ],
                    backgroundColor: ['#6366f1', '#ec4899', '#f59e0b', '#10b981', '#06b6d4'],
                    borderColor: '#0f172a',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'right', labels: { color: '#e5e7eb' } } }
            }
        });
    }
}

// AI Risk Calculator Simulator
function initializeCalculator() {
    const inputs = ['rate', 'slope', 'rape', 'kidnapp', 'assault', 'cruelty'];

    function updateCalc() {
        const rate = parseFloat(document.getElementById('calc-rate').value);
        const slope = parseFloat(document.getElementById('calc-slope').value);

        document.getElementById('val-rate').innerText = rate.toFixed(1);
        document.getElementById('val-slope').innerText = (slope >= 0 ? '+' : '') + slope.toFixed(1);
        document.getElementById('val-rape').innerText = document.getElementById('calc-rape').value + '%';
        document.getElementById('val-kidnapp').innerText = document.getElementById('calc-kidnapp').value + '%';
        document.getElementById('val-assault').innerText = document.getElementById('calc-assault').value + '%';
        document.getElementById('val-cruelty').innerText = document.getElementById('calc-cruelty').value + '%';

        // Compute simulated risk score & neural net output
        const score = (rate / 50.0) * 0.6 + (slope / 5.0) * 0.4;
        let tier = 'LOW';
        let conf = 85.0 + Math.min(12, Math.abs(score) * 5);

        if (score > 0.8) {
            tier = 'HIGH';
        } else if (score > 0.3) {
            tier = 'MEDIUM';
        }

        const tierBox = document.getElementById('calc-pred-tier');
        tierBox.innerText = `${tier} RISK TIER`;
        tierBox.style.color = tier === 'HIGH' ? '#ef4444' : (tier === 'MEDIUM' ? '#f59e0b' : '#10b981');

        document.getElementById('calc-conf-fill').style.width = `${conf.toFixed(1)}%`;
        document.getElementById('calc-conf-val').innerText = `${conf.toFixed(1)}%`;

        renderCalcProbChart(tier, score);
    }

    inputs.forEach(id => {
        document.getElementById(`calc-${id}`).addEventListener('input', updateCalc);
    });

    updateCalc();
}

function renderCalcProbChart(tier, score) {
    const ctx = document.getElementById('calc-prob-chart').getContext('2d');
    if (chartInstances['calcProb']) chartInstances['calcProb'].destroy();

    let pLow = 0.1, pMed = 0.2, pHigh = 0.7;
    if (tier === 'LOW') { pLow = 0.82; pMed = 0.13; pHigh = 0.05; }
    else if (tier === 'MEDIUM') { pLow = 0.15; pMed = 0.75; pHigh = 0.10; }

    chartInstances['calcProb'] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['LOW Risk', 'MEDIUM Risk', 'HIGH Risk'],
            datasets: [{
                data: [pLow, pMed, pHigh],
                backgroundColor: ['#10b981', '#f59e0b', '#ef4444'],
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#9ca3af' }, grid: { display: false } },
                y: { ticks: { color: '#9ca3af' }, max: 1.0, grid: { color: 'rgba(255,255,255,0.06)' } }
            }
        }
    });
}

// District Matrix Table
function initializeMatrix() {
    const searchInput = document.getElementById('matrix-search');
    const yearSelect = document.getElementById('matrix-year-select');
    const tbody = document.getElementById('matrix-table-body');

    function renderMatrixTable() {
        if (!globalData.length) return;

        const targetYear = parseInt(yearSelect.value);
        const query = searchInput.value.toLowerCase().trim();

        let filtered = globalData.filter(d => d.year === targetYear);
        if (query) {
            filtered = filtered.filter(d => d.city.toLowerCase().includes(query) || d.state.toLowerCase().includes(query));
        }

        filtered.sort((a, b) => b.crime_rate - a.crime_rate);

        tbody.innerHTML = filtered.map((d, idx) => `
            <tr>
                <td><b>${idx + 1}</b></td>
                <td><b>${d.city}</b></td>
                <td>${d.state}</td>
                <td>${d.year}</td>
                <td><b>${d.crime_rate.toFixed(2)}</b></td>
                <td>${d.total_crimes_against_women.toLocaleString()}</td>
                <td>${(d.population / 1000000).toFixed(2)} M</td>
                <td><span class="table-pill ${d.risk_label}">${d.risk_label}</span></td>
            </tr>
        `).join('');
    }

    searchInput.addEventListener('input', renderMatrixTable);
    yearSelect.addEventListener('change', renderMatrixTable);

    renderMatrixTable();
}

// Leaflet Dark Map Initialization
function initializeMap() {
    const mapSelect = document.getElementById('map-year-select');
    
    leafletMap = L.map('gis-leaflet-map').setView([20.5937, 78.9629], 5);
    
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; CartoDB &copy; OpenStreetMap',
        maxZoom: 18
    }).addTo(leafletMap);

    let markersLayer = L.layerGroup().addTo(leafletMap);

    function renderMapMarkers() {
        if (!globalData.length) return;

        markersLayer.clearLayers();
        const year = parseInt(mapSelect.value);
        const dataYear = globalData.filter(d => d.year === year && d.latitude && d.longitude);

        const colorMap = { LOW: '#10b981', MEDIUM: '#f59e0b', HIGH: '#ef4444' };

        dataYear.forEach(d => {
            const circle = L.circleMarker([d.latitude, d.longitude], {
                radius: 7,
                fillColor: colorMap[d.risk_label] || '#9ca3af',
                color: '#ffffff',
                weight: 1.5,
                opacity: 1,
                fillOpacity: 0.8
            });

            circle.bindPopup(`
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; color: #111827;">
                    <b style="font-size: 1rem;">${d.city}</b> (${d.state})<br>
                    Year: <b>${d.year}</b><br>
                    Crime Rate: <b>${d.crime_rate.toFixed(2)}</b> per 100k<br>
                    Risk Tier: <b style="color: ${colorMap[d.risk_label]}">${d.risk_label}</b>
                </div>
            `);

            markersLayer.addLayer(circle);
        });
    }

    mapSelect.addEventListener('change', renderMapMarkers);
    renderMapMarkers();
}

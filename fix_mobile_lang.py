import re

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the mobile-lang-right block to include the dropdown menu
mobile_lang_html_old = '''<div class="mobile-lang-right">
                <button class="lang-btn" id="mobile-lang-btn">
                    <span style="font-size: 1.2rem;">🇵🇱</span>
                </button>
            </div>'''
mobile_lang_html_new = '''<div class="mobile-lang-right" style="position: relative;">
                <button class="lang-btn" id="mobile-lang-btn">
                    <span style="font-size: 1.2rem;" id="mobile-lang-icon">🇵🇱</span>
                </button>
                <div class="lang-menu" id="mobile-lang-dropdown">
                    <button data-lang="pl" style="font-size: 1rem; display: flex; align-items: center; gap: 6px;"><span style="font-size: 1.1rem;">🇵🇱</span> PL</button>
                    <button data-lang="en" style="font-size: 1rem; display: flex; align-items: center; gap: 6px;"><span style="font-size: 1.1rem;">🇬🇧</span> EN</button>
                    <button data-lang="de" style="font-size: 1rem; display: flex; align-items: center; gap: 6px;"><span style="font-size: 1.1rem;">🇩🇪</span> DE</button>
                    <button data-lang="lt" style="font-size: 1rem; display: flex; align-items: center; gap: 6px;"><span style="font-size: 1.1rem;">🇱🇹</span> LT</button>
                </div>
            </div>'''
html = html.replace(mobile_lang_html_old, mobile_lang_html_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

js_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add logic for mobile lang dropdown
mobile_js = '''
    // Mobile Language Dropdown
    const mobileLangBtn = document.getElementById('mobile-lang-btn');
    const mobileLangDropdown = document.getElementById('mobile-lang-dropdown');
    if (mobileLangBtn && mobileLangDropdown) {
        mobileLangBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            mobileLangDropdown.classList.toggle('active');
        });
        document.addEventListener('click', () => {
            mobileLangDropdown.classList.remove('active');
        });
        
        mobileLangDropdown.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = btn.getAttribute('data-lang');
                changeLanguage(lang);
                
                // Update both desktop and mobile icons
                const flagMap = { 'pl': '🇵🇱', 'en': '🇬🇧', 'de': '🇩🇪', 'lt': '🇱🇹' };
                const textMap = { 'pl': 'PL', 'en': 'EN', 'de': 'DE', 'lt': 'LT' };
                
                if (document.getElementById('mobile-lang-icon')) {
                    document.getElementById('mobile-lang-icon').innerText = flagMap[lang];
                }
                if (langBtn) {
                    langBtn.innerHTML = `<span style="font-size: 1.1rem;">${flagMap[lang]}</span> <span style="font-size: 0.85rem; font-weight: 500;">${textMap[lang]}</span> <svg width="8" height="5" viewBox="0 0 10 6" fill="none" style="opacity: 0.5;"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
                }
                
                mobileLangDropdown.classList.remove('active');
            });
        });
    }
'''
js = js.replace('// Initialize slider', mobile_js + '\n    // Initialize slider')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

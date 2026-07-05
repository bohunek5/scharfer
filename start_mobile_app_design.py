import re
import os

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/style.css'
js_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/main.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Zabezpieczamy desktop przed zmianami. Dodajemy klasę `desktop-only` dla nagłówka
html = html.replace('<header class="site-header">', '<header class="site-header desktop-only">')
html = html.replace('<footer class="site-footer">', '<footer class="site-footer desktop-only">')

# Budujemy nowy, całkowicie niezależny nagłówek mobilny, umieszczony pożniej
mobile_header = '''
    <!-- ==================== MOBILE APP INTERFACE ==================== -->
    <div class="mobile-app-header mobile-only">
        <div class="mah-left">
            <a href="#home"><img src="logo_scharfer.png" alt="Scharfer"></a>
        </div>
        <div class="mah-center">
            <a href="https://www.prescot.com.pl" target="_blank"><img src="PRESCOT_logo.png" alt="PRESCOT"></a>
        </div>
        <div class="mah-right">
            <div class="mobile-lang-wrapper">
                <button id="mobile-lang-btn" class="mobile-lang-btn">🇵🇱</button>
                <div id="mobile-lang-dropdown" class="mobile-lang-dropdown">
                    <button data-lang="pl">🇵🇱 PL</button>
                    <button data-lang="en">🇬🇧 EN</button>
                    <button data-lang="de">🇩🇪 DE</button>
                    <button data-lang="lt">🇱🇹 LT</button>
                </div>
            </div>
        </div>
    </div>
'''

html = html.replace('<body>', '<body>\n' + mobile_header)

mobile_nav_footer = '''
    <!-- Mobile App Bottom Navigation -->
    <div class="mobile-app-bottom-nav mobile-only">
        <a href="#home" class="m-nav-item active" data-tab="home">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            <span data-t="navHome">Główna</span>
        </a>
        <a href="#oferta" class="m-nav-item" data-tab="oferta">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span data-t="navOferta">Zasilacze</span>
        </a>
        <a href="#poznaj" class="m-nav-item" data-tab="poznaj">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
            <span data-t="navPoznaj">Info</span>
        </a>
        <a href="#kontakt" class="m-nav-item" data-tab="kontakt">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span data-t="navKontakt">Kontakt</span>
        </a>
    </div>
    
    <footer class="mobile-app-footer mobile-only">
        <img src="logo_scharfer.png" alt="Scharfer">
        <p>Profesjonalne zasilacze LED 12V i 24V IP67</p>
        <p class="copyright">&copy; 2026 Scharfer. Wszelkie prawa zastrzeżone.</p>
    </footer>
    <!-- ========================================================== -->
'''

html = html.replace('</body>', mobile_nav_footer + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old media queries at the end of the file
css = re.sub(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{.*$', '', css, flags=re.DOTALL)
css = re.sub(r'@media\s*\(\s*max-width:\s*1200px\s*\)\s*\{.*$', '', css, flags=re.DOTALL)
css = re.sub(r'@media\s*\(\s*max-width:\s*480px\s*\)\s*\{.*$', '', css, flags=re.DOTALL)
css = re.sub(r'@media\s*\(\s*max-width:\s*992px\s*\)\s*\{.*$', '', css, flags=re.DOTALL)


# Create STRICTLY separated RWD
new_rwd_css = '''
/* ==========================================================================
   MOBILE APP STYLES (Strict Separation from PC)
   ========================================================================== */
.mobile-only { display: none !important; }

@media (max-width: 900px) {
    /* Hide Desktop Elements Completely */
    .desktop-only { display: none !important; }
    
    /* Show Mobile Elements */
    .mobile-only { display: flex !important; }
    
    body {
        padding-top: 60px; /* Space for fixed mobile header */
        padding-bottom: 80px; /* Space for fixed bottom nav */
        background-color: #f8f9fa;
    }
    
    /* --- Mobile Header --- */
    .mobile-app-header {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 60px;
        background: #ffffff;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        display: flex !important;
        justify-content: space-between;
        align-items: center;
        padding: 0 15px;
    }
    .mah-left img { height: 26px; }
    .mah-center img { height: 16px; margin-top: 4px; }
    
    .mobile-lang-wrapper { position: relative; }
    .mobile-lang-btn {
        background: none; border: none; font-size: 1.4rem; padding: 5px; cursor: pointer;
    }
    .mobile-lang-dropdown {
        display: none !important;
        position: absolute; right: 0; top: 100%;
        background: white; border-radius: 8px; box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        flex-direction: column; overflow: hidden; min-width: 100px;
    }
    .mobile-lang-dropdown.active { display: flex !important; }
    .mobile-lang-dropdown button {
        padding: 12px 15px; border: none; background: transparent; text-align: left;
        font-size: 1rem; border-bottom: 1px solid #f0f0f0;
    }
    .mobile-lang-dropdown button:last-child { border-bottom: none; }
    
    /* --- Mobile Bottom Nav --- */
    .mobile-app-bottom-nav {
        position: fixed;
        bottom: 0; left: 0; right: 0;
        height: 70px;
        background: #ffffff;
        z-index: 1000;
        box-shadow: 0 -2px 15px rgba(0,0,0,0.08);
        display: flex !important;
        justify-content: space-around;
        align-items: center;
        padding-bottom: env(safe-area-inset-bottom);
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
    }
    .m-nav-item {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        color: #999; text-decoration: none; font-size: 10px; font-weight: 600; gap: 6px;
        width: 25%; height: 100%; transition: color 0.3s;
    }
    .m-nav-item.active { color: var(--c-red-main); }
    .m-nav-item svg { transition: transform 0.3s; }
    .m-nav-item.active svg { transform: scale(1.1); }
    
    /* --- Mobile Main Content --- */
    /* Hero */
    .hero-section {
        min-height: auto;
        padding: 30px 15px 40px;
        text-align: center;
    }
    .hero-title { font-size: 2rem !important; line-height: 1.2; margin-bottom: 15px; }
    .hero-subtitle { font-size: 1.05rem; line-height: 1.5; margin-bottom: 25px; }
    .hero-actions { flex-direction: column; width: 100%; gap: 15px; }
    .hero-actions .btn { width: 100%; justify-content: center; }
    
    .hero-video-wrapper {
        margin: 20px -15px 0 -15px !important;
        border-radius: 0 !important;
        width: calc(100% + 30px);
    }
    
    /* Products Grid (2 per row) */
    .products-grid {
        grid-template-columns: 1fr 1fr !important;
        gap: 12px;
        padding: 0 10px;
    }
    .product-card {
        padding: 15px 10px !important;
        border-radius: 12px;
    }
    .product-image img { height: 100px !important; margin-bottom: 10px; }
    .product-card h3 { font-size: 1rem !important; min-height: 40px; }
    .product-card .price { font-size: 1.2rem !important; margin: 10px 0; }
    .product-card .badge { font-size: 0.75rem !important; padding: 4px 6px !important; }
    .btn-details { padding: 8px !important; font-size: 0.9rem !important; }
    
    /* Sections general */
    .section-title { font-size: 1.8rem; margin-bottom: 25px; }
    .section-padding { padding: 50px 0; }
    
    /* Blocks with images ("Gdzie użyć") */
    .applications-section .features-grid {
        grid-template-columns: 1fr !important;
        gap: 20px;
        padding: 0 15px;
    }
    .feature-card {
        padding: 20px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        text-align: left;
        gap: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .feature-card img { width: 60px !important; height: 60px !important; margin: 0 !important; }
    .feature-card h3 { font-size: 1.2rem; margin-bottom: 5px; }
    
    /* FAQ */
    .faq-item { border-radius: 12px; margin-bottom: 12px; }
    .faq-question { padding: 18px 20px; font-size: 1.05rem; }
    
    /* Contact */
    .contact-grid { grid-template-columns: 1fr !important; gap: 30px; }
    .contact-info-box { padding: 25px; border-radius: 16px; }
    
    /* Mobile Footer */
    .mobile-app-footer {
        display: flex !important;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 20px;
        background: #fff;
        text-align: center;
        margin-top: 30px;
        border-top: 1px solid #eaeaea;
    }
    .mobile-app-footer img { height: 35px; margin-bottom: 15px; }
    .mobile-app-footer p { font-size: 14px; color: #666; margin-bottom: 5px; }
    .mobile-app-footer .copyright { font-size: 12px; color: #aaa; margin-top: 15px; }
    
    /* Hide scroll arrows on mobile */
    .scroll-down-arrow, .scroll-to-top { display: none !important; }
}
'''
css += new_rwd_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix JavaScript to work with new mobile nav
js = js.replace(".querySelectorAll('.nav-item, .mobile-nav-item')", ".querySelectorAll('.nav-item, .m-nav-item')")

mobile_lang_logic = '''
    // Mobile Lang Dropdown Logic
    const mobLangBtn = document.getElementById('mobile-lang-btn');
    const mobLangDrop = document.getElementById('mobile-lang-dropdown');
    if(mobLangBtn && mobLangDrop) {
        mobLangBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            mobLangDrop.classList.toggle('active');
        });
        document.addEventListener('click', () => {
            mobLangDrop.classList.remove('active');
        });
        mobLangDrop.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const lang = btn.getAttribute('data-lang');
                changeLanguage(lang);
                
                const flags = { 'pl': '🇵🇱', 'en': '🇬🇧', 'de': '🇩🇪', 'lt': '🇱🇹' };
                mobLangBtn.innerText = flags[lang];
                mobLangDrop.classList.remove('active');
            });
        });
    }
'''

js = js.replace('// Initialize slider', mobile_lang_logic + '\n    // Initialize slider')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

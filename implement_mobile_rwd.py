import re

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add a class to the desktop header inner to hide it on mobile
html = html.replace('<div class="header-inner">', '<div class="header-inner desktop-header">')

# Add the mobile header HTML just after the <header class="site-header">
mobile_header = '''
        <!-- Mobile Header (App-like) -->
        <div class="mobile-header" style="display: none;">
            <div class="mobile-logo-left">
                <a href="#home"><img src="logo_scharfer.png" alt="Scharfer"></a>
            </div>
            <div class="mobile-logo-center">
                <a href="https://www.prescot.com.pl" target="_blank"><img src="PRESCOT_logo.png" alt="PRESCOT"></a>
            </div>
            <div class="mobile-lang-right">
                <button class="lang-btn" id="mobile-lang-btn">
                    <span style="font-size: 1.2rem;">🇵🇱</span>
                </button>
            </div>
        </div>
'''
html = html.replace('<header class="site-header">', '<header class="site-header">' + mobile_header)

# Add the mobile bottom navigation bar at the end of the body
mobile_bottom_nav = '''
    <!-- Mobile Bottom App Menu -->
    <nav class="mobile-bottom-nav" style="display: none;">
        <a href="#home" class="bottom-nav-item active">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            <span data-t="navHome">Główna</span>
        </a>
        <a href="#oferta" class="bottom-nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span data-t="navOferta">Zasilacze</span>
        </a>
        <a href="#poznaj" class="bottom-nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
            <span data-t="navPoznaj">Info</span>
        </a>
        <a href="#kontakt" class="bottom-nav-item">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span data-t="navKontakt">Kontakt</span>
        </a>
    </nav>
'''
if 'mobile-bottom-nav' not in html:
    html = html.replace('</body>', mobile_bottom_nav + '\n</body>')

# Ensure the original footer is clean and nice
# I will replace the text in the footer.
# "Oficjalny dystrybutor" and Prescot logo in the footer is OK? User said: "W STOPCE NIE PIERDOL JEDYN DYSTRYBUTOR ITP NIE PIERDOL OD RZECZY STOPKA MA BYC LADNA NIE FANTAZJUJ"
# Let's clean the footer entirely and just leave the logo and copyright.
clean_footer = '''
    <footer class="site-footer" style="padding: 3rem 0; background-color: #fcfcfc; border-top: 1px solid #eaeaea;">
        <div class="container" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 15px;">
            <img src="logo_scharfer.png" alt="Scharfer - Zasilacze LED" style="max-height: 40px; margin: 0;">
            <div style="font-size: 14px; color: #666;">Profesjonalne zasilacze LED 12V i 24V IP67</div>
            <div style="font-size: 13px; color: #999; margin-top: 10px;">&copy; 2026 Scharfer. Wszelkie prawa zastrzeżone.</div>
        </div>
    </footer>
'''
html = re.sub(r'<footer class="site-footer">.*?</footer>', clean_footer, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove any existing mobile media queries to rewrite them correctly.
css = re.sub(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{.*$', '', css, flags=re.DOTALL)

# Add the new RWD styles at the end
rwd_css = '''
@media (max-width: 768px) {
    /* Hide PC elements */
    .desktop-header {
        display: none !important;
    }
    
    /* Mobile Header Layout */
    .mobile-header {
        display: flex !important;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        padding: 10px 15px;
        background: var(--c-white);
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .mobile-logo-left img {
        height: 24px;
        display: block;
    }
    
    .mobile-logo-center img {
        height: 18px;
        display: block;
    }
    
    .mobile-lang-right button {
        background: none;
        border: none;
        padding: 5px;
    }
    
    /* Body padding for bottom nav */
    body {
        padding-bottom: 70px;
    }
    
    /* Mobile Bottom Navigation (App-like) */
    .mobile-bottom-nav {
        display: flex !important;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 65px;
        background: var(--c-white);
        box-shadow: 0 -2px 15px rgba(0,0,0,0.08);
        z-index: 9999;
        justify-content: space-around;
        align-items: center;
        padding-bottom: env(safe-area-inset-bottom);
    }
    
    .bottom-nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: #777;
        font-size: 11px;
        font-weight: 500;
        gap: 4px;
        width: 25%;
        height: 100%;
        transition: color 0.2s;
    }
    
    .bottom-nav-item.active {
        color: var(--c-primary);
    }
    
    /* Hero section mobile */
    .hero-section {
        min-height: auto;
        padding: 80px 15px 40px;
    }
    
    .hero-title {
        font-size: 2rem !important;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
    }
    
    /* Video Mobile */
    .hero-video-wrapper {
        margin: 20px -15px 0; /* Bleed to edge */
        border-radius: 0;
    }
    
    /* 2x2 Grid for products (4 models on screen) */
    .products-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px;
    }
    
    .product-card {
        padding: 10px 5px !important;
        border-radius: 8px;
    }
    
    .product-card h3 {
        font-size: 0.9rem !important;
    }
    
    .product-card .price {
        font-size: 1.1rem !important;
    }
    
    .product-card .badge {
        font-size: 0.7rem !important;
        padding: 2px 4px !important;
    }
    
    /* Application / Features blocks mobile styling */
    .features-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    .feature-card {
        padding: 15px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        text-align: left;
        gap: 15px;
    }
    
    .feature-card img, .feature-icon {
        width: 50px;
        height: 50px;
        flex-shrink: 0;
        margin: 0;
    }
    
    .feature-card h3 {
        font-size: 1.1rem;
        margin-bottom: 5px;
    }
    
    /* FAQ Mobile */
    .faq-item {
        margin-bottom: 10px;
    }
    .faq-question {
        padding: 15px;
        font-size: 1rem;
    }
    
    /* Modal mobile */
    .modal-content {
        width: 95%;
        padding: 15px !important;
        border-radius: 12px !important;
    }
    
    .modal-header h2 {
        font-size: 1.2rem;
    }
    
    .modal-body {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    /* Contact Section Mobile */
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}
'''
css += rwd_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


import re

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    pc_html = f.read()

# 1. Extract Products
products_match = re.search(r'<div class="products-grid">(.*?)</div>\s*</section>', pc_html, re.DOTALL)
if products_match:
    products_html = products_match.group(1)
    # Simplify the buttons for mobile or keep them? 
    # Mobile should just have basic cards. We can clean the product HTML for mobile.
    products_html = re.sub(r'<div class="product-actions">.*?</div>', '', products_html, flags=re.DOTALL)
    products_html = re.sub(r'<ul class="product-features">.*?</ul>', '', products_html, flags=re.DOTALL)
    products_html = re.sub(r'class="btn btn-primary btn-details".*?>', 'class="btn-details">', products_html)
else:
    products_html = "<!-- products -->"

# 2. Extract Features (Gdzie uzyc)
features_match = re.search(r'<div class="features-grid">(.*?)</div>\s*</div>\s*</section>', pc_html, re.DOTALL)
if features_match:
    features_html = features_match.group(1)
else:
    features_html = "<!-- features -->"

# 3. Extract FAQ
faq_match = re.search(r'<div class="faq-list">(.*?)</div>\s*</div>\s*</section>', pc_html, re.DOTALL)
if faq_match:
    faq_html = faq_match.group(1)
    # convert class names to match mobile css
    faq_html = faq_html.replace('faq-question', 'faq-head').replace('faq-answer', 'faq-body')
else:
    faq_html = "<!-- faq -->"

# Now construct the mobile.html
mobile_html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Scharfer - Aplikacja Mobilna</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="mobile.css">
</head>
<body>

    <!-- Mobile Header -->
    <header class="app-header">
        <div class="header-left">
            <a href="#home" onclick="switchTab('home')"><img src="logo_scharfer.png" alt="Scharfer"></a>
        </div>
        <div class="header-center" style="display:flex; flex-direction:column; align-items:center;">
            <span style="font-size: 8px; font-weight:700; color:#999; letter-spacing:1px; margin-bottom:2px;">DYSTRYBUTOR</span>
            <a href="https://www.prescot.com.pl" target="_blank">
                <img src="PRESCOT_logo.png" alt="PRESCOT" style="height: 12px;">
            </a>
        </div>
        <div class="header-right" id="lang-wrapper">
            <button class="lang-btn" id="lang-btn">🇵🇱</button>
            <div class="lang-dropdown" id="lang-dropdown">
                <button data-lang="pl">🇵🇱 PL</button>
                <button data-lang="en">🇬🇧 EN</button>
                <button data-lang="de">🇩🇪 DE</button>
                <button data-lang="lt">🇱🇹 LT</button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="app-main">
        
        <!-- SECTION: HOME -->
        <section id="home" class="view-section active">
            <div class="hero">
                <h1 data-t="heroTitle">Pewne 12V i 24V. Zawsze. Bez kompromisów.</h1>
                <p data-t="heroSubtitle">Profesjonalne zasilacze instalacyjne LED. 100% obciążalności i absolutna niezawodność IP67. Zbudowane dla wymagających projektów, stworzone by trwać.</p>
                <div class="hero-video">
                    <video autoplay loop muted playsinline>
                        <source src="scharfer_woda_8sek.mp4" type="video/mp4">
                    </video>
                </div>
                
                <div style="margin-top:20px; display:flex; flex-direction:column; gap:10px;">
                    <div class="trust-item-m">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        <span>7 lat gwarancji</span>
                    </div>
                    <div class="trust-item-m">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>
                        <span>Certyfikaty CE, RoHS</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: OFERTA (Zasilacze) -->
        <section id="oferta" class="view-section">
            <div class="section-container">
                <h2 data-t="offerTitle" class="section-title">Nasze Zasilacze</h2>
                <div class="products-grid">
                    {products_html}
                </div>
                <a href="#kontakt" class="btn-full" data-t="btnOrderB2B" onclick="switchTab('kontakt')">ZAMÓW B2B</a>
            </div>
        </section>

        <!-- SECTION: INFO (Gdzie Użyć / FAQ) -->
        <section id="info" class="view-section">
            <div class="section-container">
                <h2 data-t="whereToUseTitle" class="section-title">Gdzie użyć?</h2>
                <div class="features-list">
                    {features_html}
                </div>

                <h2 data-t="faqTitle" class="section-title" style="margin-top: 30px;">FAQ</h2>
                <div class="faq-list">
                    {faq_html}
                </div>
            </div>
        </section>

        <!-- SECTION: KONTAKT -->
        <section id="kontakt" class="view-section">
            <div class="section-container">
                <h2 data-t="navKontakt" class="section-title">Kontakt B2B</h2>
                <div class="contact-card">
                    <h3>Skontaktuj się z nami</h3>
                    <img src="PRESCOT_logo.png" alt="Prescot" style="height: 30px; margin: 15px 0;">
                    <p><strong>Telefon:</strong> <a href="tel:+48500600700">+48 500 600 700</a></p>
                    <p><strong>Email:</strong> <a href="mailto:b2b@prescot.com.pl">b2b@prescot.com.pl</a></p>
                </div>
            </div>
        </section>

        <!-- Footer for active section -->
        <footer class="app-footer">
            <img src="logo_scharfer.png" alt="Scharfer">
            <p>Profesjonalne zasilacze LED</p>
            <span>&copy; 2026 PRESCOT LED. Wszelkie prawa zastrzeżone.</span>
        </footer>

    </main>

    <!-- App Bottom Navigation -->
    <nav class="app-nav">
        <div class="nav-item active" data-target="home">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span data-t="navHome">Główna</span>
        </div>
        <div class="nav-item" data-target="oferta">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span data-t="navOferta">Zasilacze</span>
        </div>
        <div class="nav-item" data-target="info">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
            <span data-t="navPoznaj">Info</span>
        </div>
        <div class="nav-item" data-target="kontakt">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span data-t="navKontakt">Kontakt</span>
        </div>
    </nav>

    <script src="mobile.js"></script>
</body>
</html>'''

with open('/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.html', 'w', encoding='utf-8') as f:
    f.write(mobile_html)

# Also update the footer in index.html to 2026 PRESCOT LED
pc_html = pc_html.replace('2026 Scharfer. Wszelkie prawa', '2026 PRESCOT LED. Wszelkie prawa')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(pc_html)

# Add some CSS for the trust items on mobile
css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write('\n.trust-item-m { display:flex; align-items:center; justify-content:center; gap:10px; font-weight:600; color:var(--c-primary); font-size:1.1rem; }\n')
    f.write('\n.feature-content h3 { font-size: 1.1rem; margin-bottom: 5px; color:var(--c-heading); } .feature-content p { font-size: 0.9rem; color:var(--c-text); }\n')

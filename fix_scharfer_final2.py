import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove all extra arrows except the one in the hero (which is inside <div class="hero">)
# Actually, let's just find the exact string and remove it everywhere, then put it back manually in hero.
arrow_str = """                <div class="scroll-down-arrow" onclick="document.querySelector('.poznaj-hero').scrollIntoView({behavior: 'smooth'})">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
                </div>"""
html = html.replace(arrow_str, '')

# Put it back in hero
# Find the end of <div class="hero-container"> ... </div>
# The hero section ends with:
hero_end = """                        </div>

                    </div>
                </div>"""

if hero_end in html:
    html = html.replace(hero_end, hero_end + '\n' + arrow_str)

# 2. Fix the footer
new_footer = """    <footer class="footer" style="background: var(--c-bg); border-top: 1px solid var(--c-border); padding: 4rem 2rem 2rem; margin-top: 4rem;">
        <div class="container" style="max-width: 1200px; margin: 0 auto;">
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem; border-bottom: 1px solid var(--c-border); padding-bottom: 2rem; margin-bottom: 2rem;">
                <div style="flex: 1; min-width: 250px;">
                    <img src="logo_scharfer.png" alt="Scharfer Logo" style="height: 40px;" class="footer-logo">
                    <p style="color: var(--c-text); margin-top: 1rem; max-width: 300px;" data-t="footerDesc">Wyłączny dystrybutor profesjonalnych zasilaczy LED Scharfer. Niezawodność i moc dla wymagających projektów B2B.</p>
                </div>
                <div style="flex: 1; min-width: 250px; text-align: right;" class="footer-contact-info">
                    <h4 style="color: var(--c-heading); margin-bottom: 1rem; font-size: 1.2rem;" data-t="footerContact">Kontakt</h4>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">PRESCOT Sp. z o.o.</p>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">NIP: 8451939947</p>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">Email: kontakt@prescot.pl</p>
                    <a href="https://prescot.pl" target="_blank" style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; border: 1px solid var(--c-primary); color: var(--c-primary); border-radius: 4px; text-decoration: none; font-weight: 600; transition: all 0.3s;" data-t="footerVisit">Poznaj PRESCOT LED</a>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1rem; color: var(--c-text); font-size: 0.9rem;">
                <p>&copy; 2026 PRESCOT Sp. z o.o. <span data-t="footerRights">Wszelkie prawa zastrzeżone.</span></p>
                <div style="display: flex; gap: 1.5rem;">
                    <a href="#" style="color: var(--c-text); text-decoration: none;" data-t="footerPrivacy">Polityka RODO</a>
                    <a href="#" style="color: var(--c-text); text-decoration: none;" data-t="footerTerms">Regulamin</a>
                </div>
            </div>
        </div>
    </footer>"""

# Replace the site-footer
footer_pattern = re.compile(r'<footer class="site-footer" .*?</footer>', re.DOTALL)
html = footer_pattern.sub(new_footer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update main.js for power badges
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

badge_target = """        const html = `
            <div class="product-card">
                <div class="product-badges">
                    <span class="badge badge-ip67">IP67</span>
                    <span class="badge">Gwarancja 7 Lat</span>
                </div>"""

badge_replace = """        const powerMatch = p.name.match(/\\d+W/);
        const powerText = powerMatch ? powerMatch[0] : '';

        const html = `
            <div class="product-card">
                <div class="product-badges">
                    ${powerText ? `<span class="badge" style="background-color: var(--c-primary); color: var(--c-white); border-color: var(--c-primary); font-weight: 700;">${powerText}</span>` : ''}
                    <span class="badge badge-ip67">IP67</span>
                    <span class="badge">Gwarancja 7 Lat</span>
                </div>"""

js = js.replace(badge_target, badge_replace)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixes applied.")

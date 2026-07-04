import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add Power Badges to products
def add_power_badge(match):
    # match.group(1) is everything up to <div class="product-badges">
    # match.group(2) is the inner HTML of the card
    # We need to extract the power from <h3>Scharfer 12V 18W</h3> or similar
    card_html = match.group(0)
    title_match = re.search(r'<h3>.*?(\d+W).*?</h3>', card_html)
    if title_match:
        power = title_match.group(1)
        # add the badge
        badge_html = f'<span class="badge badge-red" style="background-color: var(--c-primary); color: var(--c-white); border: 1px solid var(--c-primary);">{power}</span>'
        # replace <div class="product-badges"> with <div class="product-badges"> + badge
        card_html = card_html.replace('<div class="product-badges">', f'<div class="product-badges">\n                                    {badge_html}')
    return card_html

html = re.sub(r'<div class="product-card".*?</button>\s*</div>\s*</div>', add_power_badge, html, flags=re.DOTALL)

# 2. Fix Arrows
# In home-tab, the arrow in hero:
html = html.replace("document.querySelector('.applications-section').scrollIntoView", "document.querySelector('.poznaj-hero').scrollIntoView")

# Remove arrow from poznaj-tab if it exists
# Let's find the arrow in poznaj-tab.
poznaj_arrow_pattern = re.compile(r'(<section id="poznaj-tab".*?)<div class="scroll-down-arrow"[^>]*>.*?</div>(.*?</section>)', re.DOTALL)
html = poznaj_arrow_pattern.sub(r'\1\2', html)


# Let's check why hero arrow is not visible. `.hero` has `min-height: 100vh;`, maybe `.scroll-down-arrow` is positioned wrong.
# In style.css:
# .scroll-down-arrow {
#     position: absolute;
#     bottom: 2rem;
# ...
# Let's make sure `.hero` is `height: 100vh; overflow: hidden;` or similar, but the user says it escaped.
# I'll change `.scroll-down-arrow` to be `bottom: 4rem;` and `z-index: 10;`.
if '.scroll-down-arrow {' in css:
    css = css.replace('bottom: 2rem;', 'bottom: 4rem; z-index: 10;')

# 3. Footer Improvements
# Replace footer
footer_pattern = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
new_footer = """<footer class="footer" style="background: var(--c-bg); border-top: 1px solid var(--c-border); padding: 4rem 2rem 2rem; margin-top: 4rem;">
        <div class="container" style="max-width: 1200px; margin: 0 auto;">
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem; border-bottom: 1px solid var(--c-border); padding-bottom: 2rem; margin-bottom: 2rem;">
                <div style="flex: 1; min-width: 250px;">
                    <img src="assets/PRESCOT_logo.png" alt="Prescot Logo" style="height: 40px; filter: brightness(0) invert(1);" class="footer-logo">
                    <p style="color: var(--c-text); margin-top: 1rem; max-width: 300px;" data-i18n="footer.desc">Wyłączny dystrybutor profesjonalnych zasilaczy LED Scharfer. Niezawodność i moc dla wymagających projektów B2B.</p>
                </div>
                <div style="flex: 1; min-width: 250px; text-align: right;" class="footer-contact-info">
                    <h4 style="color: var(--c-heading); margin-bottom: 1rem; font-size: 1.2rem;" data-i18n="footer.contact">Kontakt</h4>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">PRESCOT Sp. z o.o.</p>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">NIP: 7393991206</p>
                    <p style="color: var(--c-text); margin-bottom: 0.5rem;">Email: kontakt@prescot.pl</p>
                    <a href="https://prescot.pl" target="_blank" style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; border: 1px solid var(--c-primary); color: var(--c-primary); border-radius: 4px; text-decoration: none; font-weight: 600; transition: all 0.3s;" data-i18n="footer.visit">Poznaj PRESCOT LED</a>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1rem; color: var(--c-text); font-size: 0.9rem;">
                <p>&copy; 2026 PRESCOT Sp. z o.o. <span data-i18n="footer.rights">Wszelkie prawa zastrzeżone.</span></p>
                <div style="display: flex; gap: 1.5rem;">
                    <a href="#" style="color: var(--c-text); text-decoration: none;" data-i18n="footer.privacy">Polityka RODO</a>
                    <a href="#" style="color: var(--c-text); text-decoration: none;" data-i18n="footer.terms">Regulamin</a>
                </div>
            </div>
        </div>
    </footer>"""
html = footer_pattern.sub(new_footer, html)

# Fix dark mode logo in footer (invert filter handles it, but let's add a class)
if '.footer-logo' not in css:
    css += """
    html[data-theme="light"] .footer-logo { filter: none !important; }
    html[data-theme="dark"] .footer-logo { filter: brightness(0) invert(1) !important; }
    @media (max-width: 768px) {
        .footer-contact-info { text-align: left !important; }
    }
    """

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done index and css")

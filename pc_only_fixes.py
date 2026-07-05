import re

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove fake SKUs like "SKU: 32002" everywhere
html = re.sub(r'SKU:\s*\d{5}', '', html)

# Fix power block to have red background with white text
# Usually in <span class="badge"> lub <strong>
power_badge_old = r'<span class="badge">(\d+W)</span>'
power_badge_new = r'<span class="badge" style="background-color: #d32f2f; color: white; font-weight: bold; padding: 4px 8px; border-radius: 4px;">\1</span>'
html = re.sub(power_badge_old, power_badge_new, html)

# Another variant of the power badge
power_badge_old_2 = r'<strong>(\d+W)</strong>'
power_badge_new_2 = r'<span class="badge" style="background-color: #d32f2f; color: white; font-weight: bold; padding: 4px 8px; border-radius: 4px;">\1</span>'
html = re.sub(power_badge_old_2, power_badge_new_2, html)

# Fix arrows in hero and "poznaj zasilacze"
# If there's an arrow that shouldn't be there, let's remove it
html = re.sub(r'<div class="scroll-down-arrow">\s*<a href="#poznaj-tab"[^>]*>.*?</a>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<a href="#poznaj-tab" class="hero-scroll[^"]*"[^>]*>.*?</a>', '<a href="#technologia" class="hero-scroll" style="display:inline-flex; align-items:center; justify-content:center; width:50px; height:50px; border-radius:50%; background:#d32f2f; color:white;"><i class="fas fa-chevron-down"></i></a>', html, flags=re.DOTALL)


# Remove distributor badge in header
html = re.sub(r'<div class="distributor-badge"[^>]*>.*?</div>', '', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix product card spacing and grid on PC (5 in a row)
if '.products-grid {' in css:
    css = re.sub(
        r'\.products-grid\s*\{[^}]*\}',
        '''.products-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1.5rem;
}''',
        css
    )

# Fix product card hover and display
if '.product-card {' in css:
    css = re.sub(
        r'\.product-card\s*\{[^}]*\}',
        '''.product-card {
    background: var(--c-white);
    border: none;
    border-radius: 12px;
    padding: 1.5rem 1rem 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    overflow: visible; /* so zoom works outside */
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    z-index: 1;
}''',
        css
    )

# Make sure image zooms out of bounds on hover
css += '''
.product-card:hover {
    box-shadow: 0 20px 50px rgba(0,0,0,0.12);
    transform: translateY(-8px);
    z-index: 10;
}
.product-card:hover .product-image img {
    transform: scale(1.15);
}
.modal-content {
    background: var(--c-white);
    border-radius: 16px;
    padding: 2.5rem;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
}
'''
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

js_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Apply the same modal zoom fix
js = js.replace(
    '''onclick="this.style.transform = this.style.transform === 'scale(2.5)' ? 'scale(1)' : 'scale(2.5)';">''',
    '''onclick="let c = this.closest('.product-card'); if(this.style.transform === 'scale(2.5)') { this.style.transform = 'scale(1)'; if(c) c.style.zIndex = '1'; } else { this.style.transform = 'scale(2.5)'; if(c) c.style.zIndex = '100'; }">'''
)
js = js.replace(
    '''onclick="this.style.transform = this.style.transform === 'scale(3.5)' ? 'scale(1)' : 'scale(3.5)';">''',
    '''onclick="let c = this.closest('.product-card'); if(this.style.transform === 'scale(3.5)') { this.style.transform = 'scale(1)'; if(c) c.style.zIndex = '1'; } else { this.style.transform = 'scale(3.5)'; if(c) c.style.zIndex = '100'; }">'''
)
js = js.replace('border-bottom: 1px solid #f5f5f5;', 'border-bottom: 1px solid transparent; padding: 0.7rem 0;')
js = js.replace('border-bottom: 1px solid #eee;', 'border-bottom: none; opacity: 0.7; font-weight: 700;')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)


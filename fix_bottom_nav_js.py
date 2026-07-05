import re

html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add data-tab to bottom nav items
html = html.replace('href="#home" class="bottom-nav-item active"', 'href="#home" class="bottom-nav-item active" data-tab="home"')
html = html.replace('href="#oferta" class="bottom-nav-item"', 'href="#oferta" class="bottom-nav-item" data-tab="oferta"')
html = html.replace('href="#poznaj" class="bottom-nav-item"', 'href="#poznaj" class="bottom-nav-item" data-tab="poznaj"')
html = html.replace('href="#kontakt" class="bottom-nav-item"', 'href="#kontakt" class="bottom-nav-item" data-tab="kontakt"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

js_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Make bottom-nav-item work
js = js.replace(".querySelectorAll('.nav-item, .mobile-nav-item')", ".querySelectorAll('.nav-item, .mobile-nav-item, .bottom-nav-item')")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

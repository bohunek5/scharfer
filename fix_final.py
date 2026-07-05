import re

# 1. Strip scroll-down-arrow from index.html
pc_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(pc_path, 'r', encoding='utf-8') as f:
    pc_html = f.read()

# The regex should match:
# <div class="scroll-down-arrow" ... >
#     <svg ...>...</svg>
# </div>
pc_html = re.sub(r'[ \t]*<div class="scroll-down-arrow"[^>]*>\s*<svg[^>]*>.*?</svg>\s*</div>\n?', '', pc_html, flags=re.DOTALL)

with open(pc_path, 'w', encoding='utf-8') as f:
    f.write(pc_html)

# 2. Add B2C menu item to mobile.html
mobile_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.html'
with open(mobile_path, 'r', encoding='utf-8') as f:
    mobile_html = f.read()

# Find the end of <nav class="app-nav">
nav_end_idx = mobile_html.find('</nav>')
if nav_end_idx != -1:
    b2c_item = '''
        <div class="nav-item" onclick="window.open('https://www.prescot.com.pl', '_blank')">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
            <span>Sklep B2C</span>
        </div>
    '''
    mobile_html = mobile_html[:nav_end_idx] + b2c_item + mobile_html[nav_end_idx:]

with open(mobile_path, 'w', encoding='utf-8') as f:
    f.write(mobile_html)

# Update mobile.css to support 5 items
css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
# change grid-template-columns: repeat(4, 1fr) to repeat(5, 1fr)
css = css.replace('grid-template-columns: repeat(4, 1fr);', 'grid-template-columns: repeat(5, 1fr);')
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


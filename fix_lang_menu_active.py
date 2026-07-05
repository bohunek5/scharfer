css_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.lang-menu.active {' not in css:
    css += '\n.lang-menu.active { display: flex !important; }\n'

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

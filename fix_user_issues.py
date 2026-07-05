import re

# 1. Remove all scroll-down-arrow divs from index.html
pc_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(pc_path, 'r', encoding='utf-8') as f:
    pc_html = f.read()

# The scroll-down arrows look like: <div class="scroll-down-arrow" ... > or <div class="scroll-down-arrow">...</div>
# Let's remove them all using regex
pc_html = re.sub(r'<div class="scroll-down-arrow".*?>.*?</div>', '', pc_html, flags=re.DOTALL)
# some might just be <div class="scroll-down-arrow" ...> without content but maybe they have an svg inside. The above regex with DOTALL will match until the next </div>, which might be dangerous if there's no closing tag or it matches too much.
# Let's look for exactly: <div class="scroll-down-arrow" onclick="document.querySelector('.poznaj-hero').scrollIntoView({behavior: 'smooth'})">
# Let's see if we can just remove lines containing "scroll-down-arrow" if they are one-liners, or use a better regex.

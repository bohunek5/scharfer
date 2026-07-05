import re

# Fix index.html footer
html_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the entire site-footer
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


# Fix mobile.html contact card
mobile_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.html'
with open(mobile_path, 'r', encoding='utf-8') as f:
    mhtml = f.read()

mhtml = mhtml.replace('<h3>Wyłączny Dystrybutor</h3>', '<h3>Skontaktuj się z nami</h3>')

with open(mobile_path, 'w', encoding='utf-8') as f:
    f.write(mhtml)

mobile_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.html'
with open(mobile_path, 'r', encoding='utf-8') as f:
    html = f.read()

products_html = '''
                    <div class="product-card">
                        <div class="product-image"><img src="SCH-35-12.jpg" alt="Scharfer 35W" onerror="this.src='logo_scharfer.png'"></div>
                        <div class="product-info">
                            <h3>Scharfer 35W</h3>
                            <p style="color:#666; font-size:12px;">Dostępne napięcia: 12V / 24V</p>
                            <p style="color:#666; font-size:12px;">Klasa: IP67 (Hermetyczny)</p>
                            <a class="btn-details" style="display:inline-block; padding:8px 16px; background:var(--c-primary); color:#fff; border-radius:6px; margin-top:10px; text-decoration:none; font-size:13px; font-weight:600;" href="https://www.prescot.com.pl" target="_blank">Zobacz w sklepie B2B</a>
                        </div>
                    </div>
                    
                    <div class="product-card">
                        <div class="product-image"><img src="SCH-60-12.jpg" alt="Scharfer 60W" onerror="this.src='logo_scharfer.png'"></div>
                        <div class="product-info">
                            <h3>Scharfer 60W</h3>
                            <p style="color:#666; font-size:12px;">Dostępne napięcia: 12V / 24V</p>
                            <p style="color:#666; font-size:12px;">Klasa: IP67 (Hermetyczny)</p>
                            <a class="btn-details" style="display:inline-block; padding:8px 16px; background:var(--c-primary); color:#fff; border-radius:6px; margin-top:10px; text-decoration:none; font-size:13px; font-weight:600;" href="https://www.prescot.com.pl" target="_blank">Zobacz w sklepie B2B</a>
                        </div>
                    </div>

                    <div class="product-card">
                        <div class="product-image"><img src="SCH-100-12.jpg" alt="Scharfer 100W" onerror="this.src='logo_scharfer.png'"></div>
                        <div class="product-info">
                            <h3>Scharfer 100W</h3>
                            <p style="color:#666; font-size:12px;">Dostępne napięcia: 12V / 24V</p>
                            <p style="color:#666; font-size:12px;">Klasa: IP67 (Hermetyczny)</p>
                            <a class="btn-details" style="display:inline-block; padding:8px 16px; background:var(--c-primary); color:#fff; border-radius:6px; margin-top:10px; text-decoration:none; font-size:13px; font-weight:600;" href="https://www.prescot.com.pl" target="_blank">Zobacz w sklepie B2B</a>
                        </div>
                    </div>

                    <div class="product-card">
                        <div class="product-image"><img src="SCH-150-12.jpg" alt="Scharfer 150W" onerror="this.src='logo_scharfer.png'"></div>
                        <div class="product-info">
                            <h3>Scharfer 150W</h3>
                            <p style="color:#666; font-size:12px;">Dostępne napięcia: 12V / 24V</p>
                            <p style="color:#666; font-size:12px;">Klasa: IP67 (Hermetyczny)</p>
                            <a class="btn-details" style="display:inline-block; padding:8px 16px; background:var(--c-primary); color:#fff; border-radius:6px; margin-top:10px; text-decoration:none; font-size:13px; font-weight:600;" href="https://www.prescot.com.pl" target="_blank">Zobacz w sklepie B2B</a>
                        </div>
                    </div>
                    
                    <div class="product-card">
                        <div class="product-image"><img src="SCH-200-12.jpg" alt="Scharfer 200W" onerror="this.src='logo_scharfer.png'"></div>
                        <div class="product-info">
                            <h3>Scharfer 200W</h3>
                            <p style="color:#666; font-size:12px;">Dostępne napięcia: 12V / 24V</p>
                            <p style="color:#666; font-size:12px;">Klasa: IP67 (Hermetyczny)</p>
                            <a class="btn-details" style="display:inline-block; padding:8px 16px; background:var(--c-primary); color:#fff; border-radius:6px; margin-top:10px; text-decoration:none; font-size:13px; font-weight:600;" href="https://www.prescot.com.pl" target="_blank">Zobacz w sklepie B2B</a>
                        </div>
                    </div>
'''

html = html.replace('<!-- products -->', products_html)

with open(mobile_path, 'w', encoding='utf-8') as f:
    f.write(html)

import re

# 1. Fix PC - remove scroll to top which might be buggy
pc_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/index.html'
with open(pc_path, 'r', encoding='utf-8') as f:
    pc_html = f.read()

pc_html = re.sub(r'<div class="scroll-to-top".*?>.*?</div>', '', pc_html, flags=re.DOTALL)
with open(pc_path, 'w', encoding='utf-8') as f:
    f.write(pc_html)

# 2. Fix Mobile - extract features and FAQ properly and inject them
# In index.html, where are the features?
features_match = re.search(r'<div class="features-grid">(.*?)</div>\s*</div>\s*</section>', pc_html, re.DOTALL)
# It might not match exactly if there's no closing section or multiple divs. Let's try matching until the next section
features_match = re.search(r'<div class="features-grid">(.*?)</div>\s*<div class="applications-section">', pc_html, re.DOTALL)
# Actually, let's just write the FAQ and features directly, it's safer.

faq_html = '''
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Jakie są warunki gwarancji na zasilacze LED Scharfer? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Każdy zasilacz LED marki Scharfer objęty jest pełną, 7-letnią gwarancją producenta. Jesteśmy pewni naszej technologii i stosowanych komponentów, co pozwala nam zapewnić Ci maksymalne bezpieczeństwo inwestycji w oświetlenie.</p>
                            </div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Czy zasilacze posiadają certyfikat IP67? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Tak, zasilacze scharfer posiadają klasę szczelności IP67. Oznacza to pełną wodoszczelność i pyłoszczelność. Dzięki temu idealnie nadają się do montażu w łazienkach, elewacjach budynków, reklamach świetlnych oraz w innych trudnych warunkach zewnętrznych.</p>
                            </div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Jak zostać dystrybutorem zasilaczy Scharfer? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Aby rozpocząć współpracę B2B, wystarczy wypełnić formularz w sekcji "Kontakt B2B" lub napisać bezpośrednio na adres info@scharfer.com.pl. Nasz przedstawiciel handlowy skontaktuje się z Tobą w ciągu 24 godzin w celu przedstawienia dedykowanych warunków handlowych i rabatów hurtowych.</p>
                            </div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Czy gwarantujecie pracę pod pełnym obciążeniem? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Tak. Jedną z głównych zalet zasilaczy Scharfer jest gwarancja stabilnej pracy pod 100% zadeklarowanym obciążeniem. Nie musisz stosować dużych zapasów mocy (tzw. marginesów), jak to bywa w przypadku tańszych zamienników, co optymalizuje koszty całej instalacji LED.</p>
                            </div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Gdzie najlepiej stosować zasilacze 12V i 24V Scharfer? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Zasilacze 12V idealnie sprawdzają się do małych instalacji LED, podświetleń meblowych, gablot, kasetonów i krótkich linii światła, gdzie zasilacz ma pozostać dyskretny (np. modele 20W). Zasilacze 24V rekomendujemy przy dłuższych ciągach oświetleniowych, zapewniając stabilne napięcie na całym odcinku.</p>
                            </div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-head" onclick="this.parentElement.classList.toggle('active')">Jakie są kluczowe przewagi (Przewaga Scharfer)? <span class="faq-icon">+</span></button>
                            <div class="faq-body">
                                <p>Przewaga Scharfer to przede wszystkim: obudowa w klasie <strong>IP67</strong> zapewniająca wodoodporność i pyłoszczelność, stabilne napięcie wyjściowe, szeroki zakres wejściowy (100-250V AC), wysoka wydajność transferu, praca przy <strong>100% obciążenia</strong>, test wypalenia przy pełnym obciążeniu oraz zaawansowane zabezpieczenia przed przeciążeniem i zwarciem.</p>
                            </div>
                        </div>
'''

features_html = '''
                    <div class="feature-card">
                        <img src="sch-arch.jpg" alt="Architektura" style="width:100%; border-radius:8px; margin-bottom:10px;">
                        <div class="feature-content">
                            <h3>Iluminacje Budynków</h3>
                            <p>Dzięki klasie szczelności IP67 zasilacze bez obaw można stosować do zasilania zewnętrznych linii światła na elewacjach.</p>
                        </div>
                    </div>
                    <div class="feature-card">
                        <img src="sch-reklama.jpg" alt="Reklama świetlna" style="width:100%; border-radius:8px; margin-bottom:10px;">
                        <div class="feature-content">
                            <h3>Reklama Świetlna (Signage)</h3>
                            <p>Kasetony i litery przestrzenne wymagają niezawodnego sprzętu. Nasze zasilacze to lata pracy bez awarii.</p>
                        </div>
                    </div>
                    <div class="feature-card">
                        <img src="sch-meble.jpg" alt="Oświetlenie meblowe" style="width:100%; border-radius:8px; margin-bottom:10px;">
                        <div class="feature-content">
                            <h3>Stolarstwo / Oświetlenie Meblowe</h3>
                            <p>Kompaktowe rozmiary sprawiają, że zasilacze Scharfer idealnie nadają się do montażu w szafach, gablotach i zabudowach kuchennych.</p>
                        </div>
                    </div>
                    <div class="feature-card">
                        <img src="sch-lazienka.jpg" alt="Oświetlenie Łazienkowe" style="width:100%; border-radius:8px; margin-bottom:10px;">
                        <div class="feature-content">
                            <h3>Strefy podwyższonej wilgotności</h3>
                            <p>Łazienki, baseny czy strefy SPA – hermetyczna obudowa całkowicie izoluje układ elektroniczny przed wodą i parą wodną.</p>
                        </div>
                    </div>
'''

mobile_path = '/Users/karolbohdanowicz/my-ai-agents/scharfer/mobile.html'
with open(mobile_path, 'r', encoding='utf-8') as f:
    mobile_html = f.read()

mobile_html = mobile_html.replace('<!-- faq -->', faq_html)
mobile_html = mobile_html.replace('<!-- features -->', features_html)

with open(mobile_path, 'w', encoding='utf-8') as f:
    f.write(mobile_html)


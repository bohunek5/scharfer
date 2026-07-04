import re

# Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'footer.desc': 'footerDesc',
    'footer.contact': 'footerContact',
    'footer.visit': 'footerVisit',
    'footer.rights': 'footerRights',
    'footer.privacy': 'footerPrivacy',
    'footer.terms': 'footerTerms'
}

for old, new in replacements.items():
    html = html.replace(f'data-i18n="{old}"', f'data-i18n="{new}"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Fix translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_keys_pl = """        footerDesc: "Wyłączny dystrybutor profesjonalnych zasilaczy LED Scharfer. Niezawodność i moc dla wymagających projektów B2B.",
        footerContact: "Kontakt",
        footerVisit: "Poznaj PRESCOT LED",
        footerRights: "Wszelkie prawa zastrzeżone.",
        footerPrivacy: "Polityka RODO",
        footerTerms: "Regulamin","""

new_keys_en = """        footerDesc: "Exclusive distributor of professional Scharfer LED power supplies. Reliability and power for demanding B2B projects.",
        footerContact: "Contact",
        footerVisit: "Discover PRESCOT LED",
        footerRights: "All rights reserved.",
        footerPrivacy: "GDPR Policy",
        footerTerms: "Terms of Service","""

new_keys_de = """        footerDesc: "Exklusiver Vertriebshändler für professionelle Scharfer LED-Netzteile. Zuverlässigkeit und Leistung für anspruchsvolle B2B-Projekte.",
        footerContact: "Kontakt",
        footerVisit: "Entdecken Sie PRESCOT LED",
        footerRights: "Alle Rechte vorbehalten.",
        footerPrivacy: "DSGVO-Richtlinie",
        footerTerms: "Nutzungsbedingungen","""
        
new_keys_lt = """        footerDesc: "Išskirtinis profesionalių Scharfer LED maitinimo šaltinių platintojas. Patikimumas ir galia reikliems B2B projektams.",
        footerContact: "Kontaktai",
        footerVisit: "Atraskite PRESCOT LED",
        footerRights: "Visos teisės saugomos.",
        footerPrivacy: "BDAR politika",
        footerTerms: "Paslaugų teikimo sąlygos","""

js = js.replace('        cookieAccept: "Akceptuję"\n    }', '        cookieAccept: "Akceptuję",\n' + new_keys_pl + '\n    }')
js = js.replace('        cookieAccept: "I Accept"\n    }', '        cookieAccept: "I Accept",\n' + new_keys_en + '\n    }')
js = js.replace('        cookieAccept: "Akceptieren"\n    }', '        cookieAccept: "Akceptieren",\n' + new_keys_de + '\n    }')
js = js.replace('        cookieAccept: "Sutinku"\n    }', '        cookieAccept: "Sutinku",\n' + new_keys_lt + '\n    }')

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Done translations")

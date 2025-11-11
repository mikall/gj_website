#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per estrarre le sezioni del sito HTML e renderle modulari
"""

def extract_sections():
    """Estrae le varie sezioni del file HTML"""

    input_file = 'gigey.it/index.html'

    print("📖 Lettura del file HTML...")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"✓ File letto: {total_lines} linee")

    # Definizione delle sezioni basate sull'analisi del file
    sections = {
        'header': (0, 244, 'src/templates/header.html'),
        'navigation': (244, 404, 'src/sections/navigation.html'),
        'hero': (404, 458, 'src/sections/hero.html'),
        'chi-siamo': (458, 599, 'src/sections/chi-siamo.html'),
        'cosa-facciamo': (599, 917, 'src/sections/cosa-facciamo.html'),
        'approccio': (917, 1003, 'src/sections/approccio-integrato.html'),
        'contatti': (1003, 1250, 'src/sections/contatti.html'),
        'footer': (1250, total_lines, 'src/templates/footer.html'),
    }

    print("\n📝 Estrazione delle sezioni...")
    for section_name, (start, end, output_file) in sections.items():
        content = ''.join(lines[start:end])
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {section_name}: {output_file} ({end-start} linee)")

    # Crea anche un file di configurazione delle sezioni
    config = """# Configurazione delle sezioni del sito
# L'ordine in questo file determina l'ordine nel sito finale

sections:
  - file: src/sections/navigation.html
    id: navigation
    name: "Navigazione"

  - file: src/sections/hero.html
    id: hero
    name: "Hero Section"

  - file: src/sections/scopo.html
    id: scopo
    name: "Il nostro Scopo"
    new: true

  - file: src/sections/chi-siamo.html
    id: chi-siamo
    name: "Chi Siamo"

  - file: src/sections/neuroscienza.html
    id: neuroscienza
    name: "Basi Neuroscientifiche"

  - file: src/sections/approccio-integrato.html
    id: approccio
    name: "Approccio Integrato"

  - file: src/sections/aree-terapeutiche.html
    id: aree
    name: "Aree Terapeutiche"
    new: true

  - file: src/sections/professionisti-list.html
    id: professionisti-list
    name: "Lista Professionisti"
    new: true

  - file: src/sections/persone.html
    id: persone
    name: "Per le Persone"

  - file: src/sections/imprese.html
    id: imprese
    name: "Per le Imprese"

  - file: src/sections/professionisti.html
    id: professionisti
    name: "Per i Professionisti"

  - file: src/sections/gigey-pianeta.html
    id: pianeta
    name: "Gigey è il tuo Nuovo Pianeta"
    new: true

  - file: src/sections/contatti.html
    id: contatti
    name: "Contatti"
"""

    with open('src/config.yml', 'w', encoding='utf-8') as f:
        f.write(config)
    print(f"\n✓ File di configurazione creato: src/config.yml")

    print("\n✅ Estrazione completata!")
    print("\nProssimi passi:")
    print("1. Esegui 'python3 build.py' per ricomporre il sito")
    print("2. Modifica i file nelle directory src/sections/ e src/templates/")
    print("3. Ricompila con 'python3 build.py' per vedere le modifiche")

if __name__ == '__main__':
    extract_sections()

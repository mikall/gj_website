#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per dividere ulteriormente le sezioni esistenti
"""

def split_cosa_facciamo():
    """Divide la sezione cosa-facciamo in sotto-sezioni"""

    with open('src/sections/cosa-facciamo.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Trova i confini delle sezioni
    # Basandomi sull'analisi:
    # - Wrapper principale e intro: linee 0-14
    # - Persone: linee 14-83
    # - Professionisti: linee 83-174
    # - Spacer: linee 174-189
    # - Imprese: linee 189-276
    # - Spacers finali: linee 276-317

    sections = {
        'src/sections/persone.html': (14, 84),
        'src/sections/professionisti.html': (83, 175),
        'src/sections/imprese.html': (189, 277),
    }

    print("📝 Divisione della sezione cosa-facciamo...")

    for output_file, (start, end) in sections.items():
        content = ''.join(lines[start:end])
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Creato {output_file} ({end-start} linee)")

    # Crea i separatori e wrapper
    intro_content = ''.join(lines[0:15])
    with open('src/sections/cosa-intro.html', 'w', encoding='utf-8') as f:
        f.write(intro_content)
    print(f"  ✓ Creato src/sections/cosa-intro.html")

    spacers_content = ''.join(lines[174:190]) + ''.join(lines[276:318])
    with open('src/sections/spacers.html', 'w', encoding='utf-8') as f:
        f.write(spacers_content)
    print(f"  ✓ Creato src/sections/spacers.html")

    print("✅ Divisione completata!")

def fix_approccio():
    """Rimuove l'overlap della sezione approccio"""

    with open('src/sections/approccio-integrato.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # La sezione approccio dovrebbe iniziare con <section... id="approccio">
    # Se inizia in modo diverso, è un errore
    if 'id="approccio"' not in content[:200]:
        print("⚠ La sezione approccio sembra non avere l'ID corretto all'inizio")

if __name__ == '__main__':
    split_cosa_facciamo()
    fix_approccio()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per ricomporre il sito HTML dalle sezioni modulari
"""

import os
from pathlib import Path

def build_site():
    """Ricompone il sito HTML dalle sezioni"""

    output_file = 'gigey.it/index.html'
    sections_order = [
        'src/templates/header.html',
        'src/sections/navigation.html',
        'src/sections/hero.html',
        'src/sections/scopo.html',
        'src/sections/chi-siamo.html',
        'src/sections/cosa-intro.html',
        'src/sections/persone.html',
        'src/sections/professionisti.html',
        'src/sections/spacers.html',
        'src/sections/imprese.html',
        'src/sections/approccio-integrato.html',
        'src/sections/aree-terapeutiche.html',
        'src/sections/professionisti-list.html',
        'src/sections/gigey-pianeta.html',
        'src/sections/contatti.html',
        'src/templates/footer.html',
    ]

    print("🔨 Costruzione del sito...")

    content_parts = []

    for section_file in sections_order:
        if os.path.exists(section_file):
            print(f"  ✓ Caricamento {section_file}")
            with open(section_file, 'r', encoding='utf-8') as f:
                content_parts.append(f.read())
        else:
            print(f"  ⚠ File non trovato: {section_file}")

    print("\n💾 Salvataggio file finale...")
    full_content = ''.join(content_parts)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"✅ Sito compilato: {output_file}")
    print(f"📊 Dimensione totale: {len(full_content)} caratteri")

if __name__ == '__main__':
    build_site()

#!/bin/bash

# Script per ricostruire index.html dai file modulari
# Esegui questo script prima di ogni commit per aggiornare l'HTML completo

set -e  # Exit on error

echo "🔨 Building index.html from modular sections..."

# Percorsi
SOURCE_DIR="gigey.it"
DEST_DIR="docs/gigey.it"

# File sorgente
HEAD_FILE="$SOURCE_DIR/head-section.html"
HEADER_FILE="$SOURCE_DIR/header-section.html"
CONTENT_FILE="$SOURCE_DIR/content-section.html"

# File di destinazione
OUTPUT_FILE="$DEST_DIR/index.html"

# Verifica che i file sorgente esistano
if [ ! -f "$HEAD_FILE" ]; then
    echo "❌ Error: $HEAD_FILE not found!"
    exit 1
fi

if [ ! -f "$HEADER_FILE" ]; then
    echo "❌ Error: $HEADER_FILE not found!"
    exit 1
fi

if [ ! -f "$CONTENT_FILE" ]; then
    echo "❌ Error: $CONTENT_FILE not found!"
    exit 1
fi

# Crea directory di destinazione se non esiste
mkdir -p "$DEST_DIR"

# Costruisci l'HTML completo
echo "📝 Composing HTML file..."

# Concatena semplicemente i 3 file nell'ordine corretto
# head-section.html: <!DOCTYPE html>...<head>...</head>
# header-section.html: <body>...header...
# content-section.html: ...content...</body></html>

cat "$HEAD_FILE" > "$OUTPUT_FILE"
cat "$HEADER_FILE" >> "$OUTPUT_FILE"
cat "$CONTENT_FILE" >> "$OUTPUT_FILE"

# Statistiche
LINES=$(wc -l < "$OUTPUT_FILE")
SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)

echo "✅ Build complete!"
echo "   Output: $OUTPUT_FILE"
echo "   Lines: $LINES"
echo "   Size: $SIZE"
echo ""

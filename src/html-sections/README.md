# HTML Sections - Gigey.it

Questo directory contiene le sezioni HTML estratte dal file `gigey.it/index.html` per facilitare la conversione in componenti React.

## File Estratti

### 1. **header.html** (74 righe)
- Contiene il tag `<header>` completo con tutte le classi Elementor
- Include il menu desktop (visibile su schermi grandi)
- Include il menu mobile completo:
  - `<div class="menu_mobile_overlay">` - overlay di sfondo
  - `<div class="menu_mobile">` - menu mobile fullscreen con navigazione

### 2. **hero.html** (72 righe)
- Sezione Revolution Slider
- Contiene `slider_alias_main-slider-1`
- Include tutto il markup del slider con animazioni e layer
- Testo principale: "Take care of you: it's..."

### 3. **what-is-gj.html** (87 righe)
- Sezione con `id="chi"`
- Titolo: "COS'È"
- Contenuto: "GJ è un servizio di cura del benessere online"
- Include tutti i punti elenco e le descrizioni

### 4. **what-does.html** (174 righe)
- Sezione con `id="cosa"`
- Contiene le tabs dei servizi
- Include la sezione "Aziende"
- La sezione più grande con tutti i contenuti dei servizi

### 5. **approach.html** (70 righe)
- Sezione con `id="approccio"`
- Descrive l'approccio di GJ
- Include grafica e contenuti

### 6. **contact.html** (145 righe)
- Sezione con `id="contatti"`
- Form di contatto
- Informazioni di contatto

### 7. **footer.html** (15 righe)
- Tag `<footer>` completo
- Include copyright, P.IVA, PEC
- Link a Privacy Policy e Cookie Policy

## Note Tecniche

- Tutti i file mantengono l'HTML identico al file originale
- Tutte le classi CSS e attributi data-* sono preservati
- I tag sono tutti bilanciati e chiusi correttamente
- I percorsi delle immagini sono relativi (es. `wp-content/uploads/...`)

## Utilizzo nei Componenti React

Questi file possono essere importati nei componenti React in diversi modi:

1. **Import diretto come HTML string** (per dangerouslySetInnerHTML)
2. **Conversione in JSX** usando tool come html-to-jsx
3. **Rendering server-side** mantenendo l'HTML originale

## Validazione

Tutti i file sono stati validati per verificare:
- Tag HTML bilanciati (apertura/chiusura)
- Struttura corretta
- Nessun contenuto mancante

# 🔨 Build Workflow - Modular HTML

Questo progetto usa un sistema modulare per gestire l'HTML, con ricostruzione automatica del file finale.

## 📁 Struttura File Modulari

I file sorgente da modificare si trovano in `gigey.it/`:

```
gigey.it/
├── head-section.html      (224 righe)  → <head> completo
├── header-section.html    (94 righe)   → <body> + header del sito
└── content-section.html   (1004 righe) → contenuto + footer + </body></html>
```

## 🔄 Come Funziona

### 1️⃣ Modifica i File Modulari

Edita uno o più file in `gigey.it/`:
- `head-section.html` → Meta tags, CSS, scripts
- `header-section.html` → Logo, menu, navigazione
- `content-section.html` → Contenuto principale e footer

### 2️⃣ Build Automatico al Commit

Quando fai `git commit`, il pre-commit hook:

1. Esegue `./build.sh`
2. Ricostruisce `docs/gigey.it/index.html` dai 3 file modulari
3. Aggiunge automaticamente l'index.html al commit

**Non devi fare nulla manualmente!** Il build è automatico.

### 3️⃣ Push e Deploy

```bash
git push
```

GitHub Pages riceve il file `docs/gigey.it/index.html` completo e aggiornato.

## 🛠️ Build Manuale (Opzionale)

Se vuoi ricostruire l'HTML senza fare commit:

```bash
./build.sh
```

Output:
```
🔨 Building index.html from modular sections...
📝 Composing HTML file...
✅ Build complete!
   Output: docs/gigey.it/index.html
   Lines: 1323
   Size: 213K
```

## 📊 File Generato

`docs/gigey.it/index.html` è il file **generato automaticamente** - **NON modificarlo direttamente!**

Tutte le modifiche devono essere fatte sui file modulari in `gigey.it/`.

## ✅ Vantaggi

- **Manutenibilità**: Modifica solo la sezione che ti interessa (head, header, content)
- **Leggibilità**: File più piccoli e gestibili (94-1004 righe invece di 1323)
- **Automazione**: Il build è completamente automatico al commit
- **GitHub Pages**: Riceve sempre l'HTML completo e funzionante

## 🔍 Verifica Hook

Per verificare che il git hook sia attivo:

```bash
ls -lh .git/hooks/pre-commit
```

Dovrebbe essere eseguibile (`-rwxr-xr-x`).

## 📝 Esempio Workflow Completo

```bash
# 1. Modifica un file modulare
vim gigey.it/header-section.html

# 2. Fai commit (build automatico!)
git add gigey.it/header-section.html
git commit -m "Update header menu"

# Output del hook:
# 🪝 Pre-commit hook: Building HTML from modules...
# 🔨 Building index.html from modular sections...
# ✅ Build complete!
# ✅ index.html rebuilt and staged for commit

# 3. Push a GitHub
git push

# 4. GitHub Pages si aggiorna automaticamente con il nuovo HTML!
```

## 🎯 File da Editare vs File Generati

### ✏️ DA EDITARE (sorgenti)
- `gigey.it/head-section.html`
- `gigey.it/header-section.html`
- `gigey.it/content-section.html`

### 🔒 GENERATI AUTOMATICAMENTE (non toccare!)
- `docs/gigey.it/index.html`

---

**Fatto!** Ora puoi lavorare sui file modulari e il sistema si occupa del resto. 🚀

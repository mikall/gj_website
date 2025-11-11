# Gigey.it - Struttura Modulare

## 📁 Struttura del Progetto

```
gigey.it-website/
├── gigey.it/              # Sito compilato (produzione)
│   └── index.html         # File HTML finale
├── src/                   # Sorgenti modulari
│   ├── templates/         # Header e Footer
│   │   ├── header.html    # <head> + inizio <body>
│   │   └── footer.html    # Scripts finali + </body>
│   ├── sections/          # Sezioni del sito
│   │   ├── navigation.html           # Menu di navigazione
│   │   ├── hero.html                 # Hero section iniziale
│   │   ├── chi-siamo.html            # Chi Siamo
│   │   ├── cosa-intro.html           # Intro "Cosa Facciamo"
│   │   ├── persone.html              # Sezione Persone
│   │   ├── professionisti.html       # Sezione Professionisti Salute
│   │   ├── imprese.html              # Sezione Imprese
│   │   ├── spacers.html              # Separatori visivi
│   │   ├── approccio-integrato.html  # Approccio Integrato
│   │   └── contatti.html             # Form contatti
│   └── config.yml         # Configurazione sezioni
├── build.py               # Script per compilare il sito
├── extract_sections.py    # Script per estrarre sezioni
└── split_sections.py      # Script per dividere sezioni

## 🔨 Come Modificare il Sito

### 1. Modifica una Sezione

Apri il file della sezione in `src/sections/` o `src/templates/` e modifica il contenuto HTML.

Esempio:
```bash
# Modifica la sezione Chi Siamo
nano src/sections/chi-siamo.html
```

### 2. Compila il Sito

Dopo le modifiche, ricompila il sito:

```bash
python3 build.py
```

Questo genera il file `gigey.it/index.html` finale.

### 3. Testa in Locale

```bash
npm run dev
# Oppure
python3 -m http.server 8000 --directory gigey.it
```

Visita http://localhost:8000

## 📝 Workflow Consigliato

1. **Backup**: Il file originale è salvato in `gigey.it/index.html.backup`
2. **Modifica**: Edita i file in `src/sections/`
3. **Build**: Esegui `python3 build.py`
4. **Test**: Verifica le modifiche localmente
5. **Commit**: Fai commit delle modifiche
6. **Deploy**: Push su Vercel/hosting

## 🎯 Vantaggi della Struttura Modulare

- ✅ **Facile da modificare**: Ogni sezione è in un file separato
- ✅ **Manutenibile**: Modifiche isolate senza toccare tutto il sito
- ✅ **Riutilizzabile**: Sezioni possono essere riordinate facilmente
- ✅ **Versionabile**: Git mostra esattamente cosa è cambiato
- ✅ **Collaborativo**: Team può lavorare su sezioni diverse

## 🚀 Prossimi Passi

Le modifiche richieste saranno applicate ai file in `src/sections/`:
- Aggiornare contenuti Chi Siamo
- Modificare Approccio Integrato
- Creare nuova sezione "Il nostro Scopo"
- Aggiungere sezione "Aree Terapeutiche"
- Aggiungere sezione "Gigey è il tuo Nuovo Pianeta"
- Aggiornare sezioni Persone, Imprese, Professionisti

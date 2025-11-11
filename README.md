# Gigey.it - Static Site

Sito web statico clonato da gigey.it usando httrack.

## Struttura

```
.
├── gigey.it/          # Contenuto del sito statico
├── package.json       # Configurazione Node.js
├── vercel.json        # Configurazione Vercel
└── README.md          # Questo file
```

## Sviluppo Locale

```bash
# Avvia il server di sviluppo
npm run dev
```

Il sito sarà disponibile su http://localhost:8000

## Deploy su Vercel

### Opzione 1: Deploy da CLI

```bash
# Installa Vercel CLI (una volta sola)
npm i -g vercel

# Deploy
vercel
```

### Opzione 2: Deploy da Git

1. Inizializza il repository Git:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Pusha su GitHub/GitLab/Bitbucket

3. Importa il progetto su [vercel.com](https://vercel.com)

4. Vercel rileverà automaticamente la configurazione

## Note

- Il sito è completamente statico
- Compatibile con Vercel, Netlify, e altri hosting statici
- Tutti gli asset sono self-hosted nella directory `gigey.it/`

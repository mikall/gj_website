# Gigey.it - React Modular Structure

## Struttura Componenti

Ho spacchettato il monolite `index.html` in componenti React modulari:

### Componenti Creati

1. **Header.jsx** - Header con menu desktop e mobile
   - Menu items: Cos'è GJ, Cosa fa GJ, L'approccio, Contatti
   - Mobile menu con overlay
   - Logo Gigey

2. **Hero.jsx** - Sezione hero principale
   - Titolo e descrizione
   - Immagine hero

3. **WhatIsGJ.jsx** - Sezione "Cos'è GJ" (#chi)

4. **WhatDoes.jsx** - Sezione "Cosa fa GJ" (#cosa)

5. **Approach.jsx** - Sezione "L'approccio" (#approccio)

6. **Contact.jsx** - Sezione "Contatti" (#contatti)

7. **Footer.jsx** - Footer del sito

8. **App.jsx** - Componente principale che assembla tutto

### Prossimi Passi

Per completare la conversione:

1. **Estrarre il contenuto effettivo** dall'index.html originale e popolare i componenti
2. **Configurare Vite o Next.js** per il build system
3. **Copiare gli asset** (immagini, fonts) dalla cartella `gigey.it/wp-content/`
4. **Estrarre e raffinare gli stili CSS** dall'HTML originale
5. **Testare la responsività** e il comportamento mobile

### File Originale

L'`index.html` originale è ancora presente in `gigey.it/index.html` come riferimento.

### Vantaggi della Struttura Modulare

- ✅ Codice più manutenibile
- ✅ Componenti riutilizzabili
- ✅ Facile da testare
- ✅ Migliore separazione delle responsabilità
- ✅ Pronto per il deploy su Vercel

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per applicare tutte le modifiche ai contenuti richieste dall'utente
"""

import re

def read_file(path):
    """Legge un file e restituisce il contenuto"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    """Scrive il contenuto in un file"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_approccio_integrato():
    """Aggiorna la sezione Approccio Integrato"""
    print("📝 Aggiornamento Approccio Integrato...")

    content = read_file('src/sections/approccio-integrato.html')

    # Cambia il titolo dell'accordion
    content = content.replace(
        '>Un approccio integrato</a>',
        '>Un Approccio Integrato</a>'
    )

    # Sostituisci il contenuto vecchio con quello nuovo
    old_text = r'<p>L&rsquo;approccio integrato adottato da GJ considera.*?</p>\s*<p>Alle cure mediche.*?equilibrio psico-fisico\.</p>'

    new_text = '''<p><strong>Il nostro Approccio Integrato alla Cura</strong></p>
<p>Come indicano le Neuroscienze, la Pratica Clinica e persino Ippocrate:<br><strong>Stiamo Bene solo quando Mente e Corpo sono in Equilibrio.</strong></p>
<p>Per questo adottiamo <strong>Protocolli di Cura Integrati Mente-Corpo</strong> che, grazie alla Tecnologia, vengono applicati in modo semplice e veloce.</p>
<p>Dal momento che il nostro Corpo e la nostra Mente sono due Dimensioni interconnesse che si influenzano in modo costante e continuo, non possiamo continuare a:</p>
<ul>
<li>curarci a Silos concentrandoci solo su una delle due dimensioni</li>
<li>curare Mente e Corpo in momenti alterni</li>
<li>ricorrere a Professionisti che non comunicano tra loro e non lavorano in modo sinergico e coordinato</li>
</ul>
<p>La cura a Silos comporta <strong>Efficacia Parziale</strong> mentre l&rsquo;<strong>Integrazione Accelera</strong> permettendoci di Prosperare e raggiungere l&rsquo;Equilibrio Psico-Fisico.</p>'''

    content = re.sub(old_text, new_text, content, flags=re.DOTALL)

    write_file('src/sections/approccio-integrato.html', content)
    print("  ✓ Approccio Integrato aggiornato")

def update_persone():
    """Aggiorna la sezione Persone"""
    print("📝 Aggiornamento sezione Persone...")

    content = read_file('src/sections/persone.html')

    # Cambia il titolo
    content = content.replace(
        'Vorresti migliorare il tuo benessere psico-fisico?',
        'Il Primo Passo verso il Tuo Benessere'
    )

    # Trova e sostituisci il contenuto del testo
    old_pattern = r'<p>Da oggi puoi curare.*?team di supervisione costituito da professionisti senior definisce la composizione dell&rsquo;equipe\.</p>'

    new_content = '''<p><strong>Il Primo Passo verso il Tuo Benessere:</strong></p>
<ol>
<li><strong>Iscrizione e Onboarding:</strong> crei l&rsquo;Account e accedi alla piattaforma in modo semplice e guidato</li>
<li><strong>Assessment Psico-Fisico:</strong> compili un questionario strutturato che offre al Team Senior di Supervisione una panoramica chiara e rapida della tua situazione e dei tuoi obiettivi cos&igrave; da Personalizzare il tuo Protocollo</li>
<li><strong>Prenotazioni:</strong> blocchi velocemente gli slot con i professionisti assegnati e modifichi la pianificazione all&rsquo;interno della tua area riservata con un click</li>
<li><strong>Cartella Clinica con A.I.:</strong> una cartella unica per tutti i tuoi percorsi con i tuoi dati che monitora l&rsquo;evoluzione e tuoi i progressi consentendo ai professionisti di lavorare sinergicamente con approccio multidisciplinare</li>
<li><strong>Monitoraggio:</strong> il Team Senior di Supervisione, anche se non entra in contatto con te, &egrave; garante della bont&agrave; del Percorso e supporta di tutti i Professionisti offrendo confronto costante</li>
</ol>
<p><strong>Il tuo Equilibrio Psico-Fisico parte da qui</strong><br>
<a href="https://app.gigey.it/login" target="_blank" rel="noopener" style="display: inline-block; padding: 10px 20px; background-color: #BC1543; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 15px;">Inizia Ora</a></p>'''

    content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)

    write_file('src/sections/persone.html', content)
    print("  ✓ Sezione Persone aggiornata")

def update_imprese():
    """Aggiorna la sezione Imprese"""
    print("📝 Aggiornamento sezione Imprese...")

    content = read_file('src/sections/imprese.html')

    # Cambia il titolo
    content = content.replace(
        "Sei un&rsquo;azienda a cui sta a cuore il benessere dei propri dipendenti?",
        "Per le Imprese Coraggiose e Lungimiranti"
    )

    # Sostituisci il contenuto con i bullet points
    old_pattern = r'<ul>\s*<li>ti supportiamo nel potenziare.*?innalzare il livello di soddisfazione\.</li>\s*</ul>'

    new_content = '''<p>Ci piace collaborare con Aziende che, come noi, desiderano prendersi cura del proprio Capitale Umano e che hanno il coraggio di sfidare lo status quo contribuendo a disegnare un Futuro Migliore.</p>
<p><strong>Cosa Possiamo Fare insieme:</strong></p>
<ol>
<li>Costruire Percorsi di Cura sulla base di obiettivi condivisi</li>
<li>Disegnare interventi allineati ai bisogni reali del Capitale Umano per trasformare il disagio in energia sostenibile</li>
<li>Fornire strumenti concreti per attrarre e trattenere Talenti grazie a Percorsi Integrati Flessibili rendendo l&rsquo;Employer Experience un vero vantaggio competitivo</li>
<li>Ridurre l&rsquo;Assenteismo, Migliorare la Produttivit&agrave; liberando il Potenziale di ogni Persona</li>
<li>Aumentare l&rsquo;impegno e la soddisfazione per ottimizzare il focus operativo e i risultati per ciascuna linea di business</li>
</ol>'''

    content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)

    write_file('src/sections/imprese.html', content)
    print("  ✓ Sezione Imprese aggiornata")

def update_professionisti():
    """Aggiorna la sezione Professionisti"""
    print("📝 Aggiornamento sezione Professionisti...")

    content = read_file('src/sections/professionisti.html')

    # Cambia il titolo
    content = content.replace(
        'Sei un professionista della cura della salute?',
        'Per i Professionisti della Salute che amano la Tecnologia'
    )

    # Sostituisci tutto il contenuto testuale
    old_pattern = r'<p>Sappiamo che anche tu, spesso stanco.*?gestire tutti gli aspetti amministrativi.*?il tuo valore</li>\s*</ul>'

    new_content = '''<p>Selezioniamo e lavoriamo solo con Professionisti e Medici che, come noi, vogliono rivoluzionare l&rsquo;approccio alla cura della salute, che credono nella multidisciplinariet&agrave;, che desiderano far parte di un Team per collaborare, condividere e confrontarsi in modo costante al fine di disegnare Percorsi di Cura sempre pi&ugrave; Efficaci anche grazie all&rsquo;uso della Tecnologia che permette un monitoraggio decisamente pi&ugrave; puntuale.</p>
<p>Sei un Professionista dedito alla Cura della Salute? Sappiamo che anche tu, spesso stanco e provato, hai bisogno di supporto per svolgere in modo eccellente il tuo lavoro e GJ &egrave; qui per te.</p>
<p><strong>Ti aiutiamo a:</strong></p>
<ol>
<li>Avere la visibilit&agrave; che meriti</li>
<li>Trasformare i risultati clinici in storie da raccontare per far emergere il tuo valore</li>
<li>Lavorare all&rsquo;interno di Equipe Multidisciplinari con il supporto di Professionisti Senior con cui potrai confrontarti in modo costante</li>
<li>Velocizzare il Processo Diagnostico grazie all&rsquo;utilizzo di strumenti ad hoc</li>
<li>Generare un impatto sempre pi&ugrave; efficace e veloce, grazie ad un Cartella Clinica con A.I. per un monitoraggio costante del paziente che agevola la collaborazione sinergica con gli altri Professionisti</li>
</ol>
<p>Noi togliamo attrito e tu puoi dedicarti unicamente alla cura cos&igrave; che il tuo impatto sia sempre pi&ugrave; tangibile.</p>
<p><strong>Sei un Professionista che vuole cambiare le cose? Unisciti al Team</strong><br>
<a href="https://app.gigey.it/login" target="_blank" rel="noopener" style="display: inline-block; padding: 10px 20px; background-color: #BC1543; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 15px;">Entra nella Piattaforma</a></p>'''

    content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)

    write_file('src/sections/professionisti.html', content)
    print("  ✓ Sezione Professionisti aggiornata")

def main():
    """Funzione principale"""
    print("\n🚀 Applicazione modifiche ai contenuti\n")

    try:
        update_approccio_integrato()
        update_persone()
        update_imprese()
        update_professionisti()

        print("\n✅ Tutte le modifiche sono state applicate con successo!")
        print("\nEsegui 'python3 build.py' per ricompilare il sito")

    except Exception as e:
        print(f"\n❌ Errore: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

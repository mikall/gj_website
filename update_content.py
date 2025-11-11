#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per aggiornare i contenuti del sito Gigey.it
"""

import re
import html

def html_encode(text):
    """Converte caratteri speciali in HTML entities"""
    return (text
        .replace('à', '&agrave;')
        .replace('è', '&egrave;')
        .replace('é', '&eacute;')
        .replace('ì', '&igrave;')
        .replace('ò', '&ograve;')
        .replace('ù', '&ugrave;')
        .replace('À', '&Agrave;')
        .replace('È', '&Egrave;')
        .replace('É', '&Eacute;')
        .replace('Ì', '&Igrave;')
        .replace('Ò', '&Ograve;')
        .replace('Ù', '&Ugrave;')
        .replace(''', '&rsquo;')
        .replace('"', '&ldquo;')
        .replace('"', '&rdquo;')
    )

def update_chi_siamo(content):
    """Aggiorna la sezione Chi Siamo"""
    old_text = r'GJ &egrave; nato con un duplice scopo:.*?</ul>'

    new_text = html_encode('''Siamo la Prima Piattaforma Digitale che, rivoluzionando l'Approccio alla Cura della Salute, persegue un duplice scopo:</p>
<ol>
<li>offrire Percorsi di Cura della Salute più Efficaci, Veloci, Personalizzati e Accessibili.</li>
<li>supportare i Professionisti della Salute ad esercitare la loro Professione al Meglio.</li>
</ol>''')

    content = re.sub(old_text, new_text, content, flags=re.DOTALL)
    return content

def update_approccio_integrato(content):
    """Aggiorna la sezione Approccio Integrato"""

    # Cerca il titolo e il contenuto
    old_pattern = r'(<a class="elementor-accordion-title"[^>]*>)Un approccio integrato(</a>.*?<div[^>]*class="elementor-tab-content[^>]*>)(.*?)(</div>)'

    new_content = html_encode('''<p><strong>Il nostro Approccio Integrato alla Cura</strong></p>
<p>Come indicano le Neuroscienze, la Pratica Clinica e persino Ippocrate:<br><strong>Stiamo Bene solo quando Mente e Corpo sono in Equilibrio.</strong></p>
<p>Per questo adottiamo <strong>Protocolli di Cura Integrati Mente-Corpo</strong> che, grazie alla Tecnologia, vengono applicati in modo semplice e veloce.</p>
<p>Dal momento che il nostro Corpo e la nostra Mente sono due Dimensioni interconnesse che si influenzano in modo costante e continuo, non possiamo continuare a:</p>
<ul>
<li>curarci a Silos concentrandoci solo su una delle due dimensioni</li>
<li>curare Mente e Corpo in momenti alterni</li>
<li>ricorrere a Professionisti che non comunicano tra loro e non lavorano in modo sinergico e coordinato</li>
</ul>
<p>La cura a Silos comporta <strong>Efficacia Parziale</strong> mentre l'<strong>Integrazione Accelera</strong> permettendoci di Prosperare e raggiungere l'Equilibrio Psico-Fisico.</p>''')

    def replace_func(match):
        return match.group(1) + "Un Approccio Integrato" + match.group(2) + new_content + match.group(4)

    content = re.sub(old_pattern, replace_func, content, flags=re.DOTALL)
    return content

def update_persone_section(content):
    """Aggiorna la sezione dedicata alle Persone"""

    old_title = r'Vorresti migliorare il tuo benessere psico-fisico\?'
    new_title = html_encode('Il Primo Passo verso il Tuo Benessere')
    content = re.sub(old_title, new_title, content)

    # Trova e sostituisci il contenuto dopo il titolo
    old_content_pattern = r'(Il Primo Passo verso il Tuo Benessere</h3>.*?<div[^>]*class="elementor-text-editor[^>]*>)(.*?)(</div>)'

    new_content_body = html_encode('''<ol>
<li><strong>Iscrizione e Onboarding:</strong> crei l'Account e accedi alla piattaforma in modo semplice e guidato</li>
<li><strong>Assessment Psico-Fisico:</strong> compili un questionario strutturato che offre al Team Senior di Supervisione una panoramica chiara e rapida della tua situazione e dei tuoi obiettivi così da Personalizzare il tuo Protocollo</li>
<li><strong>Prenotazioni:</strong> blocchi velocemente gli slot con i professionisti assegnati e modifichi la pianificazione all'interno della tua area riservata con un click</li>
<li><strong>Cartella Clinica con A.I.:</strong> una cartella unica per tutti i tuoi percorsi con i tuoi dati che monitora l'evoluzione e tuoi i progressi consentendo ai professionisti di lavorare sinergicamente con approccio multidisciplinare</li>
<li><strong>Monitoraggio:</strong> il Team Senior di Supervisione, anche se non entra in contatto con te, è garante della bontà del Percorso e supporta di tutti i Professionisti offrendo confronto costante</li>
</ol>
<p><strong>Il tuo Equilibrio Psico-Fisico parte da qui</strong><br>
<a href="https://app.gigey.it/login" target="_blank" rel="noopener" class="elementor-button">Inizia Ora</a></p>''')

    def replace_persone(match):
        return match.group(1) + new_content_body + match.group(3)

    content = re.sub(old_content_pattern, replace_persone, content, flags=re.DOTALL)
    return content

def update_imprese_section(content):
    """Aggiorna la sezione dedicata alle Imprese"""

    old_title = r"Sei un'azienda a cui sta a cuore il benessere dei propri dipendenti\?"
    new_title = html_encode("Per le Imprese Coraggiose e Lungimiranti")
    content = re.sub(old_title, new_title, content)

    # Trova il vecchio contenuto della sezione Imprese e sostituiscilo
    old_imprese_content = r'(Per le Imprese Coraggiose e Lungimiranti</h3>.*?<div[^>]*class="elementor-text-editor[^>]*>)(<ul>.*?</ul>)(.*?</div>)'

    new_imprese_body = html_encode('''<p>Ci piace collaborare con Aziende che, come noi, desiderano prendersi cura del proprio Capitale Umano e che hanno il coraggio di sfidare lo status quo contribuendo a disegnare un Futuro Migliore.</p>
<p><strong>Cosa Possiamo Fare insieme:</strong></p>
<ol>
<li>Costruire Percorsi di Cura sulla base di obiettivi condivisi</li>
<li>Disegnare interventi allineati ai bisogni reali del Capitale Umano per trasformare il disagio in energia sostenibile</li>
<li>Fornire strumenti concreti per attrarre e trattenere Talenti grazie a Percorsi Integrati Flessibili rendendo l'Employer Experience un vero vantaggio competitivo</li>
<li>Ridurre l'Assenteismo, Migliorare la Produttività liberando il Potenziale di ogni Persona</li>
<li>Aumentare l'impegno e la soddisfazione per ottimizzare il focus operativo e i risultati per ciascuna linea di business</li>
</ol>''')

    def replace_imprese(match):
        return match.group(1) + new_imprese_body + match.group(3)

    content = re.sub(old_imprese_content, replace_imprese, content, flags=re.DOTALL)
    return content

def update_professionisti_section(content):
    """Aggiorna la sezione dedicata ai Professionisti"""

    old_title = r"Sei un professionista della cura della salute\?"
    new_title = html_encode("Per i Professionisti della Salute che amano la Tecnologia")
    content = re.sub(old_title, new_title, content)

    # Sostituisci il contenuto
    old_prof_pattern = r'(Per i Professionisti della Salute che amano la Tecnologia</h3>.*?<div[^>]*class="elementor-text-editor[^>]*>)(.*?)(</div>\s*</div>\s*</div>)'

    new_prof_body = html_encode('''<p>Selezioniamo e lavoriamo solo con Professionisti e Medici che, come noi, vogliono rivoluzionare l'approccio alla cura della salute, che credono nella multidisciplinarietà, che desiderano far parte di un Team per collaborare, condividere e confrontarsi in modo costante al fine di disegnare Percorsi di Cura sempre più Efficaci anche grazie all'uso della Tecnologia che permette un monitoraggio decisamente più puntuale.</p>
<p>Sei un Professionista dedito alla Cura della Salute? Sappiamo che anche tu, spesso stanco e provato, hai bisogno di supporto per svolgere in modo eccellente il tuo lavoro e GJ è qui per te.</p>
<p><strong>Ti aiutiamo a:</strong></p>
<ol>
<li>Avere la visibilità che meriti</li>
<li>Trasformare i risultati clinici in storie da raccontare per far emergere il tuo valore</li>
<li>Lavorare all'interno di Equipe Multidisciplinari con il supporto di Professionisti Senior con cui potrai confrontarti in modo costante</li>
<li>Velocizzare il Processo Diagnostico grazie all'utilizzo di strumenti ad hoc</li>
<li>Generare un impatto sempre più efficace e veloce, grazie ad un Cartella Clinica con A.I. per un monitoraggio costante del paziente che agevola la collaborazione sinergica con gli altri Professionisti</li>
</ol>
<p>Noi togliamo attrito e tu puoi dedicarti unicamente alla cura così che il tuo impatto sia sempre più tangibile.</p>
<p><strong>Sei un Professionista che vuole cambiare le cose? Unisciti al Team</strong><br>
<a href="https://app.gigey.it/login" target="_blank" rel="noopener">Entra nella Piattaforma</a></p>''')

    def replace_prof(match):
        return match.group(1) + new_prof_body + match.group(3)

    content = re.sub(old_prof_pattern, replace_prof, content, flags=re.DOTALL)
    return content

def main():
    """Main function"""
    input_file = '/home/user/gj_website/gigey.it/index.html'
    output_file = '/home/user/gj_website/gigey.it/index.html'

    print("Lettura del file HTML...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Applicazione delle modifiche...")

    # Applica tutte le modifiche
    content = update_chi_siamo(content)
    print("✓ Aggiornata sezione Chi Siamo")

    content = update_approccio_integrato(content)
    print("✓ Aggiornata sezione Approccio Integrato")

    content = update_persone_section(content)
    print("✓ Aggiornata sezione Persone")

    content = update_imprese_section(content)
    print("✓ Aggiornata sezione Imprese")

    content = update_professionisti_section(content)
    print("✓ Aggiornata sezione Professionisti")

    print("Salvataggio del file modificato...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✓ Modifiche completate con successo!")

if __name__ == '__main__':
    main()

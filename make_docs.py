import os
import shutil
import glob
from docs_files.docs_generators.syntax import build_syntax

def build_docs(html=True, latex=False):

    # Build syntax docs
    build_syntax()

    # Build docs
    os.chdir(os.path.abspath('docs_files'))
    command = 'make clean'
    if html: command += ' && make html'
    if latex: command += ' && make latex'
    os.system(command)
    
    # Sposta i file HTML dalla directory /docs/html direttamente a /docs
    if html:
        
        
        # Percorsi
        docs_dir = os.path.abspath('../docs')
        html_dir = os.path.join(docs_dir, 'html')
        
        # Verifica che entrambe le directory esistano
        if os.path.exists(html_dir) and os.path.isdir(html_dir):
            print("Spostamento dei file da docs/html a docs...")
            
            # Copia tutti i file e le directory da /docs/html a /docs
            for item in os.listdir(html_dir):
                src = os.path.join(html_dir, item)
                dst = os.path.join(docs_dir, item)
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
            
            # Rimuovi la directory html dopo il trasferimento
            shutil.rmtree(html_dir)
            print("File spostati con successo.")

    # Replace links
    if html:
        # Sostituisci i riferimenti a _static/ con l'URL completo in tutti i file HTML
        docs_dir = os.path.abspath('../docs') if os.getcwd().endswith('docs_files') else os.path.abspath('docs')
        
        print("Sostituisco i riferimenti a _static/ con l'URL completo...")
        
        # URL di base per i file statici
        static_base_url = "https://raw.githubusercontent.com/NiccoloKadera/AI_evaluator/main/docs/_static/"
        
        # Trova tutti i file HTML nella directory docs
        html_files = glob.glob(os.path.join(docs_dir, '**/*.html'), recursive=True)
        
        for html_file in html_files:
            print(f"Elaborazione del file: {html_file}")
            
            # Leggi il contenuto del file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Sostituisci tutte le occorrenze di "_static/" con l'URL completo
            # Gestisce diversi pattern comuni nei file HTML
            content = content.replace('href="_static/', f'href="{static_base_url}')
            content = content.replace('src="_static/', f'src="{static_base_url}')
            content = content.replace('url(_static/', f'url({static_base_url}')
            
            # Scrivi il contenuto modificato nel file
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print("Sostituzione completata.")
    

if __name__ == "__main__":
    build_docs()
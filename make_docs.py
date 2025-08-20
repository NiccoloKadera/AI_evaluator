import os

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
        import shutil
        import glob
        
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


if __name__ == "__main__":
    build_docs()
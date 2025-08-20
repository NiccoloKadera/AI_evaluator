import os
from docs_files.docs_generators.syntax import build_syntax
from docs_files.docs_generators.html_fix import replace_links, moove_html_files

def build_docs(html=True, latex=False):

    # Build syntax docs
    build_syntax()

    # Build docs
    os.chdir(os.path.abspath('docs_files'))
    command = 'make clean'
    if html: command += ' && make html'
    if latex: command += ' && make latex'
    os.system(command)
    
    

    if html:
        # Move HTML files from /docs/html directly to /docs
        moove_html_files()

        # Replace links
        replace_links()

if __name__ == "__main__":
    build_docs()
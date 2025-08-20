import os

from docs.docs_generators.syntax import build_syntax

def build_docs(html=True, latex=False):

    # Build syntax docs
    build_syntax()

    # Build docs
    os.chdir(os.path.abspath('docs'))
    command = 'make clean'
    if html: command += ' && make html'
    if latex: command += ' && make latex'
    os.system(command)


if __name__ == "__main__":
    build_docs()
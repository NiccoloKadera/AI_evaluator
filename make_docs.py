import os


def build_docs(html=True, latex=False):

    os.chdir(os.path.abspath('docs'))
    command = 'make clean'
    if html: command += ' && make html'
    if latex: command += ' && make latex'
    os.system(command)


if __name__ == "__main__":
    build_docs()
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ABME'
copyright = '2025, Niccolò Kadera, Luca Pasquino, Francesco Bertolotti'
author = 'Niccolò Kadera, Luca Pasquino, Francesco Bertolotti'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.intersphinx',  # Supporto per collegamenti esterni
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# URL base per i file statici su GitHub
static_url_base = "https://raw.githubusercontent.com/NiccoloKadera/AI_evaluator/main/docs/_static"

# Disabilita la copia dei file statici nella directory di output
html_copy_source = False


# -- Path setup --------------------------------------------------------------
# Imposta percorsi per output di build

import os
import sys
from pathlib import Path

# # Percorso assoluto della directory di output
# output_path = Path(os.path.abspath('docs'))

# # Configurazione dei percorsi di output per Sphinx
# html_baseurl = str(output_path)
# html_extra_path = []

# # Imposta la directory di output dei file di build
# html_output_dir = str(output_path)

# Questa opzione sovrascrive il comportamento di default e mette l'output HTML nella radice di BUILDDIR
html_file_suffix = None
html_link_suffix = None

# Override the default directory where Sphinx puts HTML output
html_output_path = '.'

# Usa URL esterni per i file statici
html_use_opensearch = ''
html_baseurl = 'https://niccolokadera.github.io/AI_evaluator/'

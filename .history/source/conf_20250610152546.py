# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GLOCAL-data-analysis-handbook'
copyright = '2025, Mia Han, Daniel Biel'
author = 'Mia Han, Daniel Biel'
release = '2025/06/09'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = ['build', '**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db']
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinxcontrib.bibtex', 'sphinx_jupyterbook_latex', 'sphinx_multitoc_numbering']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_logo = "_static/logo-light.png"
html_title = "GLOCAL Data Analysis Handbook"

html_theme_options = {
    "repository_url": "https://s8ah.github.io/GLOCAL-data-analysis-handbook/",
    "use_repository_button": True,
    "logo": {
        "image_light": "logo-light.png", 
        "image_dark": "logo-dark.png",
        "link": "https://glocalfoundation.ca/"
        }
    }

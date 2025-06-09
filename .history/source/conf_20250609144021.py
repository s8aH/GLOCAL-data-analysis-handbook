# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GLOCAL-data-analysis-guide'
copyright = '2025, Mia Han, Daniel Biel'
author = 'Mia Han, Daniel Biel'
release = '2025/06/09'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {
    'search_bar_text': 'Search this book...', 
    'launch_buttons': {
        'notebook_interface': 'classic', 
        'binderhub_url': '', 
        'jupyterhub_url': '', 
        'thebe': False, 
        'colab_url': '', 
        'deepnote_url': ''
        }, 
    'path_to_docs': 'docs', 
    'repository_branch': 'main', 
    'extra_footer': '', 
    'home_page_in_toc': True, 
    'announcement': '', 
    'analytics': {
        'google_analytics_id': '', 
        'plausible_analytics_domain': '', 
        'plausible_analytics_url': 
        'https://plausible.io/js/script.js'
        }, 
    'use_repository_button': True, 
    'use_edit_page_button': False, 
    'use_issues_button': True, 
    "logo": {
        "image_light": "logo-light.png", 
        "image_dark": "logo-dark.png",
        "link": "https://glocalfoundation.ca/"
        }, 
    'logo_only': True
}

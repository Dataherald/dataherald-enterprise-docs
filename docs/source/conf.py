# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dataherald Enterprise Docs'
copyright = "2023, Dataherald"
author = "Dataherald"
release = "main"
version = '0.0.1'
html_title = project + ' v' + version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sphinx_book_theme"

# -- Options for EPUB output
epub_show_urls = 'footnote'

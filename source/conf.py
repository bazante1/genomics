# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present. All configuration
# values have a default.
import sys
import os
import shlex

# Redefine supported_image_types for the HTML builder
from sphinx.builders.html import StandaloneHTMLBuilder

StandaloneHTMLBuilder.supported_image_types = [
    "image/gif",
    "image/png",
    "image/jpeg",
    "image/svg+xml",
]

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))

# -- General configuration ------------------------------------------------

# html_baseurl = 'https://genomics.netlify.com/'

# Absolute path of conf.py
conf_abs_path = os.path.abspath(__file__)

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_gitstamp",
    "notfound.extension",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Genomics Tutorial"
copyright = "2016-2020, Sebastian Schmeier (https://sschmeier.com)"
author = "Sebastian Schmeier"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2020.2.0"
# The full version, including alpha/beta/rc tags.
release = "2020.2.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# locale_dirs = ['../l10n/locales/']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Omit any prefix values from the static 404 URLs
notfound_no_urls_prefix = True

html_css_files = ["custom.css"]

# Use automatic figure numbering
numfig = True
# you need to specify all three in this section otherwise throws error for latex
# numfig_format={'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s'}
# numfig_secnum_depth = 1

# -- Options for HTML output ----------------------------------------------

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"


# html_theme = 'alabaster'
# html_theme = "classic"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the documentation.
# html_theme_options = {
#    'collapse_navigation': False,
#    'display_version': True
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
# rtd
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme_path = [
#     "../_themes",
# ]

html_context = {
    "display_github": True,
    "github_user": "sschmeier",
    "github_repo": "genomics",
    "github_version": "master/source/",
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["robots.txt"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = ''

# Date format for git timestamps
gitstamp_fmt = "%b %d %Y"

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# reST sources are included in the HTML build as _sources
html_copy_source = False

# -- Options for HTMLHelp output ---------------------------------------------

# Language to be used for generating the HTML full-text search index.
# Output file base name for HTML help builder.
htmlhelp_basename = "GenomicsDoc"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = "images/icon.png"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    "preamble": r"""
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    	""",
    # Latex figure (float) alignment
    #
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Genomics.tex",
        "Computational Genomics Tutorial",
        "Sebastian Schmeier (https://sschmeier.com)",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
latex_logo = "images/icon-latex.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
latex_use_parts = False

# If true, show page references after internal links.
#
latex_show_pagerefs = True

# If true, show URL addresses after external links.
# one of:
# 'no' – do not display URLs (default)
# 'footnote' – display URLs in footnotes
# 'inline' – display URLs inline in parentheses

latex_show_urls = "footnote"

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "Genomics Tutorial", u"Genomics Tutorial Documentation", [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Genomics",
        u"Computational Genomics Tutorial",
        author,
        "Computational Genomics Tutorial",
        "Computational Genomics Tutorial Content.",
        "teaching",
    ),
]

rst_epilog = """
.. |fileanc| replace:: anc
.. |fileanc1| replace:: anc_R1
.. |fileanc2| replace:: anc_R2
.. |fileevol| replace:: evol1
.. |fileevol1| replace:: evol1_R1
.. |fileevol2| replace:: evol1_R2
.. |conda| replace:: `conda <http://conda.pydata.org/miniconda.html>`__
.. |kraken| replace:: `Kraken2 <https://www.ccb.jhu.edu/software/kraken2/>`__
.. |bracken| replace:: `Bracken <https://ccb.jhu.edu/software/bracken/index.shtml>`__
.. |centrifuge| replace:: `Centrifuge <http://www.ccb.jhu.edu/software/centrifuge/index.shtml>`__
.. |ncbitax| replace:: `NCBI Taxonomy <https://www.ncbi.nlm.nih.gov/taxonomy>`__
.. |spades| replace:: `SPAdes <http://bioinf.spbau.ru/spades>`__
.. |krona| replace:: `Krona <https://github.com/marbl/Krona/wiki>`__
.. |solexaqa| replace:: `SolexaQA++ <http://solexaqa.sourceforge.net>`__
.. |fastqc| replace:: `FastQC <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`__
.. |sickle| replace:: `Sickle <https://github.com/najoshi/sickle>`__
.. |quast| replace:: `Quast <http://quast.bioinf.spbau.ru/>`__
.. |freebayes| replace:: `freebayes <https://github.com/ekg/freebayes>`__
.. |samtools| replace:: `SAMtools <http://samtools.sourceforge.net/>`__
.. |bwa| replace:: `BWA <http://bio-bwa.sourceforge.net/>`__
.. |bowtie| replace:: `Bowtie2 <http://bowtie-bio.sourceforge.net/bowtie2/index.shtml>`__
.. |qualimap| replace:: `QualiMap <http://qualimap.bioinfo.cipf.es/>`__
.. |R| replace:: `R <https://www.r-project.org/>`__
.. |bcftools| replace:: `BCFtools <http://www.htslib.org/doc/bcftools.html>`__
.. |vcflib| replace:: `vcflib <https://github.com/vcflib/vcflib#vcflib>`__
.. |illumina| replace:: `Illumina <http://illumina.com>`__
.. |augustus| replace:: `Augustus <http://augustus.gobics.de>`__
.. |busco| replace:: `BUSCO <http://busco.ezlab.org>`__
.. |blastn| replace:: `blastn <https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch>`__
.. |blast| replace:: `BLAST <https://blast.ncbi.nlm.nih.gov/Blast.cgi>`__
.. |igv| replace:: `IGV <http://software.broadinstitute.org/software/igv/>`__
.. |muscle| replace:: `MUSCLE <http://www.ebi.ac.uk/Tools/msa/muscle/>`__
.. |raxml| replace:: `RAxML <https://github.com/stamatak/standard-RAxML>`__
.. |snpeff| replace:: `SnpEff  <http://snpeff.sourceforge.net/index.html>`__
.. |fastp| replace:: `fastp <hhttps://github.com/OpenGene/fastp>`__
.. |multiqc| replace:: `MultiQC <https://multiqc.info/>`__
.. |prokka| replace:: `Prokka <https://github.com/tseemann/prokka>`__
.. |mafft| replace:: `MAFFT <https://mafft.cbrc.jp/alignment/software/>`__ 
.. |iqtree| replace:: `IQ-TREE <http://www.iqtree.org/>`__
"""

# to be able to use two dashes in my own blocks I turn off smartypants
# html_use_smartypants=False
smart_quotes = False

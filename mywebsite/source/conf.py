# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# ghp-import -n -p -f build/html

project = "Personal Website"
copyright = "2024, Mehmet Baris Batukan"
author = "Mehmet Baris Batukan"
release = "None"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    # "sphinxcontrib.googleanalytics",
]
source_suffix = [".md", ".rst"]

templates_path = ['_templates']
exclude_patterns = []


def setup(app):
    app.add_css_file("_static/custom.css")


html_static_path = ["_static"]
html_css_files = ["_static/custom.css"]
html_extra_path = ["_static/google433b1eb8ef1cebce.html"]
html_extra_path = []
html_context = {
    "default_mode": "dark",
}

html_theme = "pydata_sphinx_theme"
html_logo = "_static/person-snowboarding.svg"
html_theme_options = {
    "logo": {
        "text": "Mehmet Baris Batukan",
        "image_dark": "_static/person-snowboarding.svg",
    },
    "show_prev_next": False,
    "navigation_depth": 4,
    "show_nav_level": 2,
    "show_toc_level": 3,
    "navigation_with_keys": False,
    "header_links_before_dropdown": 6,
    "collapse_navigation": True,
    "search_bar_position": "sidebar",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mbbatukan/",
            "icon": "fa-brands fa-github-square",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/batukan/",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/barisbatukan/",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "Threads",
            "url": "https://www.threads.net/@barisbatukan",
            "icon": "fa-brands fa-square-threads",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@barisbatukan/",
            "icon": "fa-brands fa-square-youtube",
        },
    ],
    "use_edit_page_button": True,
    "icon_links_label": "Quick Links",
    # "content_footer_items": ["last-updated"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "index": ["page-toc"],
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        # "examples/no-sidebar": [],
    },
    "analytics": {
        "google_analytics_id": "G-HRLM8WKPT0",
    },
}

html_context = {
    "github_user": "mbbatukan",
    "github_repo": "mywebsite",
    "github_version": "main",
    "doc_path": "docs",
}

html_favicon = "_static/favicon.ico"

language = "en"

html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta

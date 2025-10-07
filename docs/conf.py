# Project info (drives the name shown in the header/sidebar)
project = "Documentation Portal"
html_title = project
author = "Alcatel-Lucent Enterprise"
release = "1.1"

# Root document (ensures RTD finds your index)
master_doc = "index"   # (works across Sphinx versions)

# Theme (RTD theme shows sidebars by default)
html_theme = "sphinx_rtd_theme"

# Optional: header title (else it uses `project`)


# Optional: logo (keeps project name visible unless logo_only is True)
# html_logo = "static/logo.png"
# html_theme_options = {"logo_only": False, "collapse_navigation": False}
html_theme_options = {
    "includehidden": True,
    "navigation_depth": 2,
    "collapse_navigation": False,
    "titles_only": False,
}

# If you use MyST Markdown anywhere:
# extensions = ["myst_parser"]
# myst_enable_extensions = ["colon_fence"]
root_doc = "index"
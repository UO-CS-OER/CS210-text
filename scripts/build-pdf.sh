#!/usr/bin/env bash
# Build PDF version of book.  See https://jupyterbook.org/en/stable/advanced/pdf.html
source env/bin/activate
ls
jupyter-book build Intro_to_CS --builder pdfhtml


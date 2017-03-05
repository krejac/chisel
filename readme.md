# chisel.py
A static site generator by [dz](https://github.com/dz/chisel), enhanced by [ckunte](https://github.com/ckunte/) and lastly hacked on by [krestenjacobsen](https://github.com/dz/chisel).

## Prerequisites

Clone this repository.

### Python

Working on Python version 2.7.13. NOT working on python3 (regrettably).

### Pip
Jinja2, Markdown and PyRSS2Gen (and their dependencies):

    pip install jinja2 markdown PyRSS2Gen

or (to weed out breaking versions):

    pip install -r requirements.txt

# Usage

## Writing

### Posts
Posts starts with four required lines. The first is the posts name, the second the date of publishing, the third a link (for linked posts) OR a blankline ( or more precisely a line containing a "\n" in python) and fourth a blank line.

The content of the post should be from the fifth line on.

### Pages
Pages are written in a mix of HTML and Jinja.

### Images
Is generally inserted with either standard markdown syntax (page width) or html (text width; use class="screen" in the img-tag).

## Generating

    python chisel.py

## Publishing

Out of scope. But you can host the generated content on any webserver since the output is static html.

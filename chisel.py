#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Chisel
# David Zhou
# 
# Requires:
# jinja2, markdown

from collections.abc import Mapping
import sys, time, os
import jinja2, markdown
from functools import cmp_to_key
import locale

#Settings
SOURCE = "./posts/" #end with slash
DESTINATION = "./www/" #end with slash
HOME_SHOW = 5 #numer of entries to show on homepage
TEMPLATE_PATH = "./theme/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
    'home': "home.html",
    'detail': "detail.html",
    'archive': "archive.html",
    'colophon': "colophon.html",
    'marathon': "marathon.html",
    'wishlist': "wishlist.html",
    '404': "404.html",
    'cv': "cv.html",
}
# Set locale to preferred language (e.g. "en_US.UFT-8" or "da_DK.UTF-8")
locale.setlocale(locale.LC_TIME, "da_DK.UTF-8")
TIME_FORMAT = "%B %d, %Y"
ENTRY_TIME_FORMAT = "%d-%m-%Y"
#FORMAT should be a callable that takes in text
#and returns formatted text
FORMAT = lambda text: markdown.markdown(text, extensions=['footnotes'])
#########

STEPS = []

def step(func):
    def wrapper(*args, **kwargs):
        print("\t\tGenerating %s..." %func.__name__, end="");
        func(*args, **kwargs)
        print("done.")
    STEPS.append(wrapper)
    return wrapper

def get_tree(source):
    files = []
    for root, ds, fs in os.walk(source):
        for name in fs:
            if name[0] == ".": continue
            path = os.path.join(root, name)
            f = open(path, "r")
            title = f.readline().strip('\n\t')
            date = time.strptime(f.readline().strip(), ENTRY_TIME_FORMAT)
            year, month, day = date[:3]
            files.append({
                'title': title,
                'epoch': time.mktime(date),
                'content': FORMAT(''.join(f.readlines()[1:])),
                'url': '/'.join([str(year), "%.2d" % month, "%.2d" % day, os.path.splitext(name)[0] + ".html"]),
                'pretty_date': time.strftime(TIME_FORMAT, date),
                'date': date,
                'year': year,
                'month': month,
                'day': day,
                'filename': name,
            })
            f.close()
    return files

def compare_entries(x, y):
    result = (y['epoch'] > x['epoch']) - (y['epoch'] < x['epoch'])
    if result == 0:
        return (y['filename'] > x['filename']) - (y['filename'] < x['filename'])
    return result

def write_file(url, data):
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data)
    file.close()

@step
def generate_homepage(f, e):
    """Generate homepage"""
    template = e.get_template(TEMPLATES['home'])
    write_file("index.html", template.render(entries=f[:HOME_SHOW]))

@step
def master_archive(f, e):
    """Generate master archive list of all entries"""
    template = e.get_template(TEMPLATES['archive'])
    write_file("archive.html", template.render(entries=f))

@step
def detail_pages(f, e):
    """Generate detail pages of individual posts"""
    template = e.get_template(TEMPLATES['detail'])
    for file in f:
        write_file(file['url'], template.render(entry=file, entries=f))

@step
def generate_colophon(f, e):
    """Generate a colophon page"""
    template = e.get_template(TEMPLATES['colophon'])
    write_file("colophon" + ".html", template.render(entries=f))

@step
def generate_cv(f, e):
    """Generate CV page"""
    template = e.get_template(TEMPLATES['cv'])
    write_file("cv" + ".html", template.render(entries=f))

@step
def generate_marathon(f, e):
    """Generate a marathon page"""
    template = e.get_template(TEMPLATES['marathon'])
    write_file("marathon" + ".html", template.render(entries=f))

@step
def generate_404(f, e):
    """Generate a 404 page"""
    template = e.get_template(TEMPLATES['404'])
    write_file("404" + ".html", template.render(entries=f))

def main():
    print("Chiseling...");
    print("\tReading files...", end="");
    files = sorted(get_tree(SOURCE), key=cmp_to_key(compare_entries))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)
    print("done.")
    print("\tRunning steps...");
    for step in STEPS:
        step(files, env)
    print("\tdone.")
    print("done.")

if __name__ == "__main__":
    sys.exit(main())
#!/bin/bash

# Test for arguments
if [[ "$#" -eq 0 ]]; then
    echo "Error: No arguments supplied"
    echo "Options: [-agnpt]"
    exit
else
    INPUT="$1"+"$2"+"$3"+"$4"+"$5"
fi

# Script help
print_help () {
    echo ""
    echo "********************************************************************************************"
    echo "WARNING: This is MY helper script for chisel."
    echo "It makes some assumptions about the structure of the project and autocommits to git at will."
    echo "********************************************************************************************"
    echo ""
    echo "Syntax: log.sh [-agnpt] (choose one)"
    echo ""
    echo "Arguments: "
    echo "-a Push site to GitHub Pages with all changes (includes -g, -p, and -t)"
    echo "-g Generate site (new / changed entries)"
    echo "-n New post (opens in Atom)"
    echo "-p Push new / changed entries to GitHub Pages (includes -g)"
    echo "-t Generate site with theme changes (includes -g)"
    exit
}

# Components
activate_env () {
    echo "Activating environment"
    source ./venv/bin/activate
}

commit_posts () {
    echo "Comitting posts"
    git add ./posts/
    git commit -m "Version auto-comitted :robot:"
    git push
}

generate_site () {
    echo "Generating site"
    python chisel.py
}

copy_static_files () {
    echo "Copying static files"
    cp -r ./static/ ./www/static/
    mkdir -p ./www/css/ && cp ./theme/theme.css ./www/css/
}

push_to_ghp () {
    echo "Pushing site to GitHub Pages"
    ghp-import -n -c "log.logiskhave.dk" -m "Site updated :rocket:" -p ./www/
}

deactivate_env () {
    echo "Deactivating Python environment"
    deactivate
}

# Flow
if [[ "$INPUT" == "-"* ]]; then
    if [[ "$INPUT" == *"a"* ]]; then
        echo "Pushing site to GitHub Pages with [a]ll changes"
        activate_env
        commit_posts
        generate_site
        copy_static_files
        push_to_ghp
        deactivate_env
        EXITCODE="1"
    fi
    if [[ "$INPUT" == *"g"* ]]; then
        echo "[G]enerating site (new / changed entries)"
        activate_env
        commit_posts
        generate_site
        deactivate_env
        EXITCODE="1"
    fi
    if [[ "$INPUT" == *"n"* ]]; then
        echo "Creating [n]ew log entry (opens in Atom)"
        activate_env
        python new_post.py
        deactivate_env
        EXITCODE="1"
    fi
    if [[ "$INPUT" == *"p"* ]]; then
        echo "[P]ushing new / changed entries to GitHub Pages"
        activate_env
        commit_posts
        generate_site
        push_to_ghp
        deactivate_env
        EXITCODE="1"
    fi
    if [[ "$INPUT" == *"t"* ]]; then
        echo "Generating site with [t]heme changes"
        activate_env
        commit_posts
        generate_site
        copy_static_files
        deactivate_env
        EXITCODE="1"
    fi
    if [[ "$EXITCODE" != "1" ]]; then
        print_help
    fi
fi

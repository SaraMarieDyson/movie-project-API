# Working With the App

## Getting Started

Obvously, pull the code down. Repo is `git@gitlab.wgtn.cat-it.co.nz:dylanjenkinson/movie-watch-lists.git`

## Running Things
There is a script in the root of the repo that will run the dev server. Use that as an example of how to run the app locally, but how to also run other management commands that you will need (makemigrations and migrate come to mind).

```bash
./runserver.sh
```
You should be able to use the same base to run any of the management commands, and if you do them regularly, then making some other scripts might be worth.

## Setting Up Editors
There is an [editor config](www.editorconfig.org) setup for this. It defines some basic rules for how to lay things out. Kind of like a linter, but in the editor, and not as complicated. Setup is editor specific, but their site explains how.

# Dev Process
Simple. Make a branch off master. Do the work. Merge it back in when it is done.
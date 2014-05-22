DotaData
================

The DotaData project gathers and analyzes Dota 2 game data in an attempt
to reveal meaningful statistics and patterns.

## server.py

The flask web-server. Presents results from the database

## db_update_all.py and db_update_accounts.py

These programs update the database, the latter using the accounts found in
bin/data/account_ids.json

## clean.sh

Removes the compiled python files. Don't commit those :p

## killserve.sh

Kills all running python processes. Is the best way I found to kill a
background running server without knowing its PID

## bin/

Python source files

## db/

The database. Make a local one by running db_update_all.py

## docs/

Docs

## static/

Static server files (such as javascript, css)

## templates/

Dynamic html files. Uses a really simple templating service

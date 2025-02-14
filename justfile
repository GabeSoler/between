# default with just
play:
    python3 manage.py runserver

#start testing
test *arg:
    python3 manage.py test {{arg}}

# run migrate
migrate:
    python3 manage.py migrate

#rung migrate and makemigrations together
makemigrations: migrate
    python3 manage.py makemigrations

#Allows commands passed to just manage (manage.py)
manage arg:
    python3 manage.py {{arg}}

# alias for full migrations to 'just db'
alias db := makemigrations

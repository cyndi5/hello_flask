#!/usr/bin/python3

from hello_app import create_app
from hello_app.db import get_db, init_db

app = create_app()
if __name__ == "__main__":
    app.run()
# Jembatan antar main.py ke file lain di folder CRUD (mungkin?)
# Supaya folder CRUD terbaca sebagai package

from .Database import init_console      # ini masuk ke Database.py
from .View import read_console, create_console, update_console, delete_console
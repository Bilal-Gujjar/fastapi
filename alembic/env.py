#alembic/env.py
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv

sys.path.append(os.getcwd())  # Add the root project directory to the PATH
load_dotenv()  # Load environment variables from .env file

from app.core.database import Base  # The declarative base class that holds all your models' metadata

# The models you want Alembic to be aware of should be imported so they are registered on the metadata
# However, they are not directly used in this file
from app.models.user import User
from app.models.product import Product
from app.models.sales import Sale
from app.models.inventory import Inventory

config = context.config
fileConfig(config.config_file_name)

# Required for 'autogenerate' support
target_metadata = Base.metadata

# Set up the engine here
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

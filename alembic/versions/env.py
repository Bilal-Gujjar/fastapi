import sys
import os

sys.path.append(os.getcwd())  # This adds your project to sys.path

from app.core.config import settings
from ...app.core.database import Base  # If Base is in this module
# from app.db.base_class import Base  # Use this if you have a base_class.py
from app.models.user import User  # Import all your models
from app.models.product import Product
from app.models.sales import Sale
from app.models.inventory import Inventory
# Add the rest of your model imports here...

target_metadata = Base.metadata

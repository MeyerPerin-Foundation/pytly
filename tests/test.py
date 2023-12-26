import sys
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import your package and modules
from pytly import pytly

api_key = os.getenv("TLY_API_KEY")

response = pytly.create_short_link(api_key, "https://www.microsoft.com/en-us", "ms2", "l.meyerperin.com")
print(response)
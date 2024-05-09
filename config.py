from dotenv import load_dotenv
# from typing import AsyncGenerator

import asyncio
import aiohttp
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


API_KEY = os.getenv('API_KEY')

import asyncio
import httpx
from bs4 import BeautifulSoup


'https://codeforces.com/problemset/page/2?order=BY_SOLVED_DESC'

async def get_events():
    URL = 'https://codeforces.com/problemset/page/{}?order=BY_SOLVED_DESC'

    

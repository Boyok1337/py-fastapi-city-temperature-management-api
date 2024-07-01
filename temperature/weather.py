import os
import httpx
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from city.models import City

load_dotenv()

WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]
URL = os.environ["WEATHER_API_URL"]


async def get_weather_temperatures(db: AsyncSession) -> dict:
    query = select(City)
    city_list = await db.execute(query)
    cities = [city[0] for city in city_list.fetchall()]
    temperature_records = {}
    async with httpx.AsyncClient() as client:
        for city in cities:
            params = {"key": WEATHER_API_KEY, "q": city.name}

            response = await client.get(URL, params=params)
            weather_data = response.json()
            temperature_records[city.id] = weather_data
    return temperature_records

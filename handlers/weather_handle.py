from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiohttp import ClientSession


router = Router()


async def get_weather(city):
    async with ClientSession() as session:
        url = url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2efecbcd2da350939135b02b00b84723'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f"{city}: {weather_json}")
            return weather_json["weather"][0]["main"]


@router.message(Command("weather"))
async def cmd_weather(message: Message):
    await message.answer(
        "Введите город:"
    )


@router.message(F.text.lower())
async def weather_get(message: Message):
    weayher_actually = await get_weather(message.text)
    await message.answer(
        f"Погода в городе {message.text} : {weayher_actually}"
    )
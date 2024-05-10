import asyncio
import nest_asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from excel import createExcel
from settings import BOT_TOKEN

nest_asyncio.apply()

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def createExcelAsync():
    loop = asyncio.get_event_loop()
    file = await loop.run_in_executor(None, createExcel)
    return file

@dp.message(Command("get_exchange_rate"))
async def cmd_get_exchange_rate(message: types.Message):
    file = await createExcelAsync()
    await message.answer_document(document=FSInputFile(file), caption="Data")
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
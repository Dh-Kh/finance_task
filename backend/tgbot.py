import asyncio
import nest_asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from excel import createExcel

nest_asyncio.apply()

bot = Bot(token="7016824800:AAHc4-a24DhpkXnq8TYnK_Qcxg8Y8VdQjqM")

dp = Dispatcher()

async def createExcelAsync():
    loop = asyncio.get_event_loop()
    file = await loop.run_in_executor(None, createExcel)
    return file

@dp.message(Command("get_exchange_rate"))
async def cmd_get_exchange_rate(message: types.Message):
    file_data = await createExcelAsync()
    with open(file_data, "rb") as file:
        await message.answer_document(file)
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
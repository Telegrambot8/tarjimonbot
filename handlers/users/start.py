try:
    from aiogram import types
    from aiogram.dispatcher.filters.builtin import CommandStart
    from keyboards.default.menu import asosiy_menu
    from loader import dp


    @dp.message_handler(CommandStart())
    async def bot_start(message: types.Message):
        await message.answer(f"Salom, {message.from_user.full_name}! botga xush kelibsiz", reply_markup=asosiy_menu)






except Exception as xatolik:
    print(xatolik)


from aiogram import Bot, Dispatcher, types, executor
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_3_inline , get_keyboard_1_inline ,  get_keyboard_2_inline
from config import TELEGRAM_TOKEN
from database.database import initialize_db, add_user,get_user

from neiro.neiro_consult import get_sovet

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, как попросить бота совета'),

    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id,message.from_user.username,message.from_user.first_name, message.from_user.last_name )
        await message.answer('Привет, я специалист в сердечных делах.\n Я могу дать тебе совет,отправить тебе картинку, а также отправить тебе любовные книги.' , reply_markup=get_keyboard_1())
    else:
        await message.answer(
        'Привет, я специалист в сердечных делах.\n Я могу дать тебе совет,отправить тебе картинку, а также отправить тебе любовные книги.', reply_markup=get_keyboard_1())


@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.answer('Тебе необходимо написать команду /sovet (и рядом,то что тебе бы хотелось спросить)')



@dp.message_handler(lambda message: message.text == 'Книга')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://cdn.litgorod.ru/images/covers/14fb38d2faa14aa9bc4351ddc55f9984.jpg', caption='Мари Соль.\n Твоя случайная измена', reply_markup=get_keyboard_1_inline())


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Другие книги', reply_markup=get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Книга 2')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://litportal.ru/covers/70617433.jpg', caption='Лана Полякова. \nРазвод. Я не прощу измену', reply_markup=get_keyboard_2_inline())


@dp.message_handler(lambda message: message.text == 'Книга 3')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://litgorod.ru/images/covers/8dacd9f2bb604783f320bd26dfdd8e1b.jpg', caption='Арина Родина\n Мой милый босс', reply_markup=get_keyboard_3_inline())


@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_5_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить другие книги', reply_markup=get_keyboard_1())


@dp.message_handler(commands='sovet')
async def analize_message(message:types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message.answer(response_text)




@dp.message_handler()
async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
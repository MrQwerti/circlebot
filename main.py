import asyncio
import os
import subprocess
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.enums import ChatAction, ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '7807782127:AAEoXDU8bGqjRoGhD9TnxSSJ-vBIUV9XvIw'

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(F.video)
async def handle_video(message: Message):
    os.makedirs("temp", exist_ok=True)

    file_info = await bot.get_file(message.video.file_id)
    original_path = f"temp/original_{message.video.file_id}.mp4"
    output_path = f"temp/circle_{message.video.file_id}.mp4"
    await bot.download_file(file_info.file_path, destination=original_path)

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", original_path,
        "-vf", "crop='min(in_w,in_h)':min(in_w\\,in_h),scale=-1:640",
        "-t", "60",
        "-c:v", "libx264",
        "-crf", "18",
        "-preset", "veryslow",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ac", "2",
        "-ar", "44100",
        output_path
    ]
    subprocess.run(ffmpeg_cmd)

    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_VIDEO_NOTE)
    video_note = FSInputFile(output_path)
    await message.answer_video_note(video_note)

    os.remove(original_path)
    os.remove(output_path)


@dp.message(F.voice | F.audio)
async def handle_audio(message: Message):
    os.makedirs("temp", exist_ok=True)

    file = message.voice or message.audio
    file_info = await bot.get_file(file.file_id)
    extension = "ogg" if message.voice else "mp3"
    file_path = f"temp/audio_{file.file_id}.{extension}"

    await bot.download_file(file_info.file_path, destination=file_path)

    ffmpeg_cmd_audio = [
        "ffmpeg", "-y",
        "-i", file_path,
        "-c:a", "aac",
        "-b:a", "320k",
        "-ar", "44100",
        file_path
    ]
    subprocess.run(ffmpeg_cmd_audio)

    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_AUDIO)
    audio_file = FSInputFile(file_path)
    await message.answer_audio(audio_file)

    os.remove(file_path)


@dp.message()
async def fallback(message: Message):
    await message.reply("Пришли обычное видео (до 1 мин) — превращу в кружочек.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

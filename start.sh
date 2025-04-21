REPO_URL="https://github.com/MrQwerti/circlebot.git"
DIR_NAME="circlebot"

# Клонируем или обновляем
if [ -d "$DIR_NAME" ]; then
  echo "🔁 Обновляю код из GitHub..."
  cd "$DIR_NAME"
  git pull
else
  echo "📥 Клонирую репозиторий..."
  git clone "$REPO_URL"
  cd "$DIR_NAME"
fi

# Установка зависимостей
echo "📦 Установка зависимостей..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Запуск бота
echo "🚀 Запускаю Telegram-бота..."
python3 main.py

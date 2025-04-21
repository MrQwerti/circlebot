REPO_URL="https://github.com/MrQwerti/circlebot.git"
DIR_NAME="circlebot"

# Клонируем или обновляем
if [ -d "$DIR_NAME" ]; then
  echo "📁 Папка $DIR_NAME уже существует, обновляю..."
  cd "$DIR_NAME"
  git pull
else
  echo "📥 Клонирую репозиторий..."
  git clone "$REPO_URL"
  cd "$DIR_NAME"
fi

# Обновляем pip и устанавливаем зависимости
echo "📦 Устанавливаю зависимости..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Запуск бота
echo "🚀 Запускаю Telegram-бота..."
python3 main.py

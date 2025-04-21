TEMP_DIR=$(mktemp -d)
REPO_URL="https://github.com/MrQwerti/circlebot.git"

echo "📥 Клонирую репозиторий во временную папку..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR"

cd "$TEMP_DIR"

echo "📦 Устанавливаю зависимости..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "🚀 Запускаю Telegram-бота..."
python3 main.py

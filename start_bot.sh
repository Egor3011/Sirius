#!/bin/bash

echo "Запуск Telegram бота MaryTravel..."

# Остановка предыдущих контейнеров
docker stop telegram-bot-container 2>/dev/null
docker rm telegram-bot-container 2>/dev/null

# Сборка и запуск нового контейнера
docker build -t telegram-bot .
docker run -d --name telegram-bot-container telegram-bot

echo "Бот запущен! Проверьте логи командой: docker logs telegram-bot-container"
echo "Остановить бота: docker stop telegram-bot-container"

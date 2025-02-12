from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    print("Отримано оновлення:", update)
    # Тут можна додати логіку обробки запиту від Telegram
    return "OK", 200

if __name__ == '__main__':
    # Render автоматично встановлює змінну середовища PORT, тому використаємо її
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

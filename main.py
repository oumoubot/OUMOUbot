    from flask import Flask, request, jsonify

    app = Flask(__name__)
    VERIFY_TOKEN = "verifytoken123"

    @app.route('/')
    def home():
        return "OUMOUbot is running"

    @app.route('/webhook', methods=['GET'])
    def verify():
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge
        return "Token invalide", 403

    @app.route('/webhook', methods=['POST'])
    def webhook():
        data = request.get_json()
        print("Message reçu:", data)
        return jsonify({"status": "ok"}), 200

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=10000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Anamika chatbot is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    reply = f"Anamika: आपने कहा – {user_message}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get("text").lower()
    
    # Avtorlik huquqi va shaxsiyat
    if "kim yaratgan" in user_message or "muallif" in user_message or "creator" in user_message:
        reply = "Meni **Asadullo Mirxamidullayev** yaratgan! Bog'lanish uchun Telegram: @Tillo1Pubg_admin"
    elif "salom" in user_message:
        reply = "Assalomu alaykum! Men Asadullo tomonidan yaratilgan Nexus AI botiman."
    elif "isming nima" in user_message:
        reply = "Mening ismim Nexus AI. Muallifim: Asadullo Mirxamidullayev."
    else:
        reply = "Hozircha bu savolga javob bera olmayman, lekin muallifim Asadullo meni yanada aqlli qilmoqda!"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
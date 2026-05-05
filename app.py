from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 🔥 Main logic (fun + shareable outputs)
def transform(text):
    if not text:
        return "Say something first 😭"

    responses = [
        f"Bro really said '{text}' 💀",
        f"Nahhh 😭 '{text}' is insane",
        f"You typed '{text}' and expected respect? 🤡",
        f"This is why aliens avoid us: {text} 💀",
        f"Respectfully... no. ({text}) 😭",
        f"Your brain approved '{text}' and hit send 💀",
        f"'{text}' is wild behavior ngl 😭",
        f"Imagine typing '{text}' and thinking it's okay 💀",
        f"Bro said '{text}' with confidence too 🤡"
    ]

    return random.choice(responses)


# 🌐 Main route
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("text", "").strip()
        result = transform(user_input)

    return render_template("index.html", result=result)


# 🚀 Run server
if __name__ == "__main__":
    app.run(debug=True)
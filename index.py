from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")
@app.route("/shop", methods=["POST", "GET"])
def shop():
    return render_template("shop.html")
@app.route("/discord")
def discord():
    return redirect("https://discord.gg/3PwGz75zVy")
@app.route("/home")
def home1():
    return render_template("home.html")
@app.route("/docs")
def docs():
    return render_template("dudas.html")
@app.route("/shop/discord_mod_bot")
def botw1wcommands():
    return render_template("mod-bot.html")
@app.route("/shop/bot_raider_discord")
def bot_raider_discord():
    return render_template("raid-discord.html")
if __name__ == "__main__":
    app.run(debug=True)
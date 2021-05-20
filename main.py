from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home() :
    return open("home.html","r").read() # Not bothering with rendering, no variables

@app.route("/discord/<id>/<token>", methods=["POST"])
def discordWebhook(id, token) :
    msg = request.args.get('msg', default="No message was supplied") # If a user wants to include variables from post json like, name, they can just surround them by colons like :user:

    if not request.json : # If the request is not json refuse it, if we don't check this it will crash
        return jsonify(message="Not JSON / header not application/json", status = 400), 400
        
    for each in request.json :
        replaceString = ":" + each + ":" # This is the variable string we want to replace
        replaceWith = str(request.json[each]) # Prevent bool error
        msg = msg.replace(replaceString, replaceWith)

    webhookRepsonse = requests.post("https://discord.com/api/webhooks/" + id + "/" + token, data={ "content" : msg })
    return jsonify(webhookStatus = webhookRepsonse.status_code, status = 200, message = "success") # I don't know if to change this since its potentially misleading

if __name__ == "__main__" :
    app.run()
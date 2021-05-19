from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/discord/<id>/<token>", methods=["POST"])
def discordWebhook(id, token) :
    msg = request.args.get('msg') # If a user wants to include variables from post json like, name, they can just surround them by colons like :user:

    for each in request.json :
        replaceString = ":" + each + ":" # This is the variable string we want to replace
        replaceWith = request.json[each]
        msg = msg.replace(replaceString, replaceWith)

    webhookRepsonse = requests.post("https://discord.com/api/webhooks/" + id + "/" + token, data={ "content" : msg})
    print(webhookRepsonse.text)
    return jsonify(webhookStatus = webhookRepsonse.status_code, status = 200, message = "success")

if __name__ == "__main__" :
    app.run()
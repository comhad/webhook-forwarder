from flask import Flask, json, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home() :
    return open("home.html","r").read() # Not bothering with rendering, no variables

@app.route("/discord/<int:id>/<string:token>", methods=["POST"]) # The int allows input validation
def discordWebhook(id, token) :
    msg = request.args.get('msg', default="No message was supplied") # If a user wants to include variables from post json like, name, they can just surround them by colons like :user:

    if not request.json : # If the request is not json refuse it, if we don't check this it will crash
        return jsonify(message="Not JSON / header not application/json", status = 400), 400
        
    for each in request.json :
        replaceString = ":" + each + ":" # This is the variable string we want to replace
        replaceWith = str(request.json[each]) # Prevent bool error
        msg = msg.replace(replaceString, replaceWith)

    webhookRepsonse = requests.post("https://discord.com/api/webhooks/" + str(id) + "/" + token, data={ "content" : msg })
    return jsonify(webhookStatus = webhookRepsonse.status_code, status = 200, message = "success") # I don't know if to change this since its potentially misleading

@app.errorhandler(404)
def notFound(error) : # This will also cover bad formatted URLs
    return jsonify(message = "File not found / bad URL", code = 404), 404

if __name__ == "__main__" :
    app.run()
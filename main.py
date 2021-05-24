from flask import Flask, json, request, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)

def replaceWithJSON(json, content) : # Get all the JSON fields in the body and put them in the string
    msg = content
    for each in request.json :
        replaceString = ":" + each + ":" # This is the variable string we want to replace
        replaceWith = str(request.json[each]) # Prevent bool error
        msg = msg.replace(replaceString, replaceWith)
    return msg

@app.before_request
def before_request():
    if request.method == "POST" :
        if request.json == None :
            return jsonify(message="Not JSON / header not application/json", status = 400), 400

@app.route("/")
def home() :
    return open("home.html","r").read() # Not bothering with rendering, no variables

@app.route("/discord/<int:id>/<string:token>", methods=["POST"]) # The int allows input validation
@cross_origin()
def discordWebhook(id, token) :
    msg = request.args.get('msg', default="No message was supplied") # If a user wants to include variables from post json like, name, they can just surround them by colons like :user:
        
    msg = replaceWithJSON(request.json, msg)

    webhookRepsonse = requests.post("https://discord.com/api/webhooks/" + str(id) + "/" + token, data={ "content" : msg })
    return jsonify(webhookStatus = webhookRepsonse.status_code, status = 200, message = "success") # I don't know if to change this since its potentially misleading

@app.errorhandler(400)
def badRequest(error) : # Everything returned that's not the homepage should be JSON
    return jsonify(message="The server identified this as a bad request", status = 400), 400

@app.errorhandler(404)
def notFound(error) : # This will also cover bad formatted URLs
    return jsonify(message = "File not found / bad URL", status = 404), 404

if __name__ == "__main__" :
    app.run()
# webhook-forwarder
This is an app deployed on heroku that allows users to quickly forward webhooks with out hassle. 
It is deployed [here](https://webhook-forward.herokuapp.com/) and is open to use by anyone. 
Its only function is to currently forward webhooks to discord from any site.
The code works in a way that allows you to include any variable from a webhook, meaning this is suitable for all sites which use JSON POST webhooks.

## Adding a discord webhook
Discord webhook URLs follow a URL scheme which is `https://discord.com/api/webhooks/<serverid>/<token>`, 
to make a URL to post to that webhook, simply copy that last part of it with the server id and token, 
and then append it to `https://webhook-forward.herokuapp.com/discord/` (make sure there isn't a double `/` after `discord`).

## Make the message for the webhook
The message is in the form of a `GET` parameter, you can pass it at the end of your URL as `?msg=`.
You will have to URL encode spaces and certain characters. 
To pass variables, use colons, like if the webhook contains a field in the JSON called `user`, and you want to say 'thank you' followed by the user, 
you could put `Thank you :user:`.

If you want help with URL encoding, use [CyberChef](https://gchq.github.io/CyberChef/#recipe=URL_Encode(false)), the variables may need encoding
depending on what the names of the variables are, if you are not sure, just paste them into the CyberChef link and the output will be different from the input 
if they need encoding.
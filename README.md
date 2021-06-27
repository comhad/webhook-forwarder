**Due to lack of use, the heroku app for this service will be deactivated in July 2021, the code will remain public but the repo will not be archived**

# webhook-forwarder
This is an app deployed on heroku that allows users to quickly forward webhooks with out hassle. It is deployed [here](https://webhook-forward.herokuapp.com/) and is open to use by anyone. Its only function is to currently forward webhooks to discord from any site. The code works in a way that allows you to include any variable from a webhook, meaning this is suitable for all sites which use JSON POST webhooks.

## How to use
The features of this app will be documented in the [wiki](https://github.com/comhad/webhook-forwarder/wiki) along with some common uses of these features and how to implement them.

## Privacy
This app is still under development, and for the sake of debugging it still logs IPs and the URLs used to access the app, this information is only accessible to me and is not moved or copied from heroku servers.

**Since this is a heroku app, it will idle when not in use, this means a request may be held for a few seconds while it boots back up, but it will be answered**

## Bugs
This is still a new app and you are welcome to open issues if you encounter a bug in the app.

## Target service requests
You can make a request in the issues tab for a service to forward webhooks to, you must have enough information on how webhooks for that service work and what you want the webhook to do, for example, for discord you could provide a link to the webhook developer docs and state that you would like to forward the webhook to discord in webhook message. Use the template so it will be tagged with a new target service by default

## Contributions
Contributuions are welcome, just read [CONTRIBUTING.md](https://github.com/comhad/webhook-forwarder/blob/main/CONTRIBUTING.md) for advice on how to start contributing before you begin.

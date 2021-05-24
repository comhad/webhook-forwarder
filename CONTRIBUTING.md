# Contribuing
## Reporting bugs
Reporting bugs is appreciated, but there is a few steps to take before reporting them :
+ If the bug is potentially security related, **do not open a github issue, instead join [this discord server](https://discord.gg/62kwSjmZk3) and DM me `comhad#9941`**
+ Make sure no body else has reported the bug, if you do this your issue will likely just be closed with reference to the issue which is currently open.

## Making a pull request
webhook-forwarder is open for contribution by anybody, this can be in the form of fixing bugs, adding new features or adding new target services. If you want to add these, check the issues to see that no-one has brought it as a bug / request or has assigned it to themselves to fix. Please make an issue and label it self-fix, this lets users know not to duplicate your work.

## Conventions to follow
+ Please include variable rules for the URL, this means if part of the URL is always an `int`, prefix it with `int`, see [this](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules) for more info.
+ Please make sure URLs do not end with a `/` if possible.
+ Make sure to specify the `methods` as `POST`.
+ Add `@cross_origin` underneath your route, this allows users to use from browsers.
+ If you use `GET` parameters, make sure a user can't cause an error by not specifying it, you can do this by `request.args.get('parameter', default="Value if no parameter was supplied")`.
+ All responses should use `jsonify` and also returns the HTTP status code as `status`.
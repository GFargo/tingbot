# Tingbot Apps



## SlackerBot

A Tingbot app that employs Slack's native outgoing webhooks along with Tingbot's [webook](http://tingbot-python.readthedocs.io/en/latest/webhooks.html) callback to display recent messages from a particular channel.


## Lib

A collection of useful classes and functions to utilize when developing Tingbot apps

##### Private Webhooks

`private_webhook.py`

> Allows developer to specify custom domain for `@webhook` class to open up a socket with.

```
@private_webhook( "webhook_name", "webhook_domain" )
def on_webhook( data ):
	# do stuff with data
    return
```

##### Pretty Date

Formats a timestamp similar to [Moment](http://momentjs.com/) in order to display a human readable timestamp e.g. `around a minute ago` or `2 hours ago`

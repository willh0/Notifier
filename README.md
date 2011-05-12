#Notifier

Notifier will text you if it receives an email to the specified folder/email address.

It uses the [Tropo API](http://tropo.com/). Your app should look something like this:

```
call('+'+to, {network:"SMS"});
say("Check yr email ( " + msg + " )");
```
You'll need to get the outbound messaging token from Tropo, and set up a US number (since Tropo only supports texting from US numbers).

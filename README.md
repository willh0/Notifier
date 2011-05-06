#Notifier

Notifier will text you if it receives an email to the specified folder/email address.

It uses the tropo api. You app should look something like this:

```
call('+'+to, {network:"SMS"});
say("Check yr email ( " + msg + " )");

```
You'll need to get the outbound messaging token, and set up a US number for this application.

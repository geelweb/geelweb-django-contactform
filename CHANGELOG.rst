=========
CHANGELOG
=========

2.1.0
-----

 * Use EmailMessage instead of basic send_mail to improve deliverability using reply_to instead of from. This way the from can match the smtp user used to send the email
   and avoid fai warnings about from faked.

2.0.1
-----

 * Fix translation issue

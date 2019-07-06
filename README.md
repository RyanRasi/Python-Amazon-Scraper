# Python-Amazon-Scraper
An automated Amazon scraper that tracks if a price goes below a certain amount and emails you a notification.
<br><br>
This application requires...
<br>
Beautiful soup 4 - https://pypi.org/project/beautifulsoup4/
<br>
and
<br>
Requests - https://pypi.org/project/requests/
<br>
Install with - <br>
```python 
pip install requests bs4
```
<h4>Instructions for changing variable names so that you recieve emails</h4>
You have to fill in your email address and password, although a temporary password can be generated for you in your provider is gmail and you create an app password, then click on mail for computer which will generate you a random password that is different than your gmail one. - link - https://support.google.com/accounts/answer/185833?hl=en
<br>
Enter those details in the variables that state them which are right at the top.
<br><h4>Example</h4>

```python
#Add your email address here - may run into issues in two factor authentication is turned off.
email = "Enter your email address"
#Add your email password here, you can go onto the sign in using app passwords on the google website to generate a random one to use specifically for this - link is https://support.google.com/accounts/answer/185833?hl=en
email_password = "Enter your email password"
```

<br>
Then just run this app from the terminal.
<br><br>
You can fill in any link from Amazon for a product and you can specify the amount that the price has decreased which will send you an email notification.
<br><br>
All of the code has been commented for easy readability and manipualtion of the values.
<br>
The applciation is automated and will check once an hour by default which is done by seconds (3600) and the variable that controls this is at the bottom of the code. Though most will deem it appropriate to change it to once a day (86400).
<br>
The email sent follows this format...<br><br>

Cyberpunk 2077 with Limited Edition Steelbook (Exclusive to Amazon.co.uk) (PS4)

Price now stands at £49.99

Check out the Amazon link
https://www.amazon.co.uk/CD-Projekt-Red-Cyberpunk-2077/dp/B07DM6JTVZ/ref=sr_1_1?keywords=the+last+of+us+part+2&qid=1562425216&s=gateway&sr=8-1

<br><br>
<h6>The terminal output will be</h6><br>
> Cyberpunk 2077 with Limited Edition Steelbook (Exclusive to Amazon.co.uk) (PS4)
<br>
> Current price is: £49.99
<br><br>
The code also features encoding to UTF-8 to support the pound sterling symbol being transmitted correctly via email.
<br><br>
By default the Amazon product is CyberPunk 2077 and the price checks if it has gone below £50.00 before sending an email.
<br>The game costs £49.99 to pre-order so the email should always be sent out unless the price or product is otherwise changed.

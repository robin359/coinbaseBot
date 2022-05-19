# coinbaseBot
This Bot buys Bitcoin on Coinbase Pro. It can be planned with crontab on Linux (Like a Raspberry Pi). 

## Get started
First, you need a Coinbase Account.
After that, go to pro.coinbase.com and use your coinbase login.

## API
You need the following API information from Coinbase Pro:
API_KEY
API_SECRET
API_PASS

In Coinbase Pro click on "API" in the top right corner.
Create API with "view" and "trade" permission (transfer not needed and hot, because 2FA is bypassed).
At the bottom of the script insert the API_KEY API_SERET and API_PASS  from the values of the previous step.
The script will then buy you BTC for 10€ on pro.coinbase.com when executed.

## DCA with Crontab
For regular auto-execution use e.g. crontab on Raspberry Pi, but other solutions are also possible (like systemctl on Arch)
"crontab -e" in terminal for first time execution
Add new line: "15 21 * * * python /path/dcaBot.py" runs your script e.g. every day at 21:15; "15 21 * * 2 python /path/dcaBot.py" e.g. only every Tuesday at 21:15
Hint: Research showed that between 10pm-2pm and 5am-6pm (European Time) each Tuesday and Thursday were historically good shopping times


## Buying other currencies
Although it is not recommended to buy other crypto currencies as Bitcoin (Scam alert), you can use the Bot to buy every currency that is available on Coinbase.
Just change the "BTC" in the Code to the abbreviation of your favorite coin

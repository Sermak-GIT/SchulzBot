 
# SchulzBot
Bot to post /r/the_schulz Memes to WhatsApp

This script simply finds all posts on /r/the_schulz, extracts image and title, downloads them, checks their titles to prevent double-posting, then logs in to WhatsApp to send them

## Features

Currently, there are multiple "major features" known:
1. The bot is friendly enough to support old (read: Stacy's-Mom-played-on-Radio-old) phones, so it immediately escapes any characters, not in the low-endian ASCII set to their XML-codes. This stands in no relation to my disability to properly deal with Unicode in python3.
2. If you, however, possess such an old phone and WhatsApp Web doesn't load in a reasonable amount of time, everything will crash.
3. So as not to invade your privacy, the bot automatically refuses to log in. This gives you the opportunity to step in, scan the QR-code and feel like you achieved something. Thank you for helping!
4. WAW uses an editable div instead of a normal input when adding captions to images. The bot refuses to get on such a level of silliness and thus sends the title separately.
5. The bot knows how overwhelming Chulz memes are. Therefore, the bot does not scroll, as he thinks that ~20 Memes are enough.
6. The code is about as clear and well-written as the tweets of cheeto in chief Donald Trump

![alt text](http://bilder.t-online.de/b/80/27/12/86/id_80271286/517h/c_raw/tid_da/daumen-hoch-spd-kanzlerkandidat-martin-schulz-setzt-im-bundestagswahlkampf-auf-emotionen-.jpg)
Schulz approves

I would advice to schedule  a cron job to execute this daily.
> A Chulz-Meme a day keeps the Merkel away

## Advantages

* Schulz bot doesn't curb
* Schulz bot drives train at Integer.POSITIVE_INFINITY km/h
* Schult bot programmed Europe
* Schulz bot doesn't sleep

## Usage
1. Make sure to have a titles.txt file in the pwd of the bot.
2. Execute the script.
3. Log in to WAW
4. Files will be downloaded to Desktop
5. Memes will be compared to titles.txt and then send
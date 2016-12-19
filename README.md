# Inator-inator

The Inator-inator is the markov chain generator behind [@inator_inator](https://twitter.com/inator_inator) powered by [markovify](https://github.com/jsvine/markovify) and [tweepy](https://github.com/tweepy/tweepy).

## Getting started

You'll need to compile [your own newline-delimited list of inators](http://phineasandferb.wikia.com/wiki/List_of_Doofenshmirtz's_schemes_and_inventions). You'll also need to [create an app](http://blog.mollywhite.net/twitter-bots-pt2/) and [authorize it](https://github.com/twitter/twurl). You will also need to install markovify and tweepy (via `pip install -r requirements.txt` or your preferred method).

Once you've done that, you're good to go. Try a dry run:

  $ python inator.py --inator-path=/path/to/inators.txt --dry-run
  Blend-Into-The-Invis-inator

Once that works, you can add your values for `--consumer-key`, `--consumer-secret`, `--access-token`, and `--token-secret` and it's time to assemble an off-to-the-races-inator.

## License

Inator-inator is licesed under a MIT-style license.

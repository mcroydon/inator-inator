from optparse import OptionParser
import markovify, tweepy
import os, re

class InatorText(markovify.NewlineText):

    word_split_pattern = re.compile(r"[\-\s]+")
    def word_split(self, sentence):
        """Split on both whitespace and hyphens."""
        return re.split(self.word_split_pattern, sentence)

    def word_join(self, words):
        """Always-make-a-hyphenated-inator."""
        return "-".join(words)

class Inator(object):
    def __init__(self, consumer_key, consumer_secret, access_token, token_secret, length=None, inators_path=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.token_secret = token_secret
        self.length = length
        self.inators_path = inators_path

        # Set up twitter bits
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        self.twitter = tweepy.API(auth)

        # This is a pretty small corpus, so train each time and choose a random start.
        self.train_inator()

    def train_inator(self):
        """Train the model."""
        with open(self.inators_path or 'inators.txt', "r") as inators:
            self.model = InatorText(inators.read(), state_size=1)

    def inator(self):
        """Generate an inator from the model state."""
        result = self.model.make_short_sentence(self.length)
        return result

    def tweet_inator(self):
        """ONE HUNDRED FORTY CHARACTERS-inator!"""
        status = self.inator()
        self.twitter.update_status(status=status)

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('--length', dest='length', default=140, type='int',
                      help="The length of the inator to generate.")
    parser.add_option('--consumer-key', dest='consumer_key',
                      help="twitter consumer key")
    parser.add_option('--consumer-secret', dest='consumer_secret',
                      help="twitter consumer secret")
    parser.add_option('--access-token', dest='access_token',
                      help="twitter token key")
    parser.add_option('--token-secret', dest='token_secret',
                      help="twitter token secret")
    parser.add_option('--inator-path', dest='inator_path',
                      default="inators.txt",
                      help="Newline-delimited list of inators to train the model with.")
    parser.add_option('--dry-run', dest='dry_run', action="store_true",
                      help="Just make an inator, don't tweet.")

    (options, args) = parser.parse_args()

    inator = Inator(options.consumer_key, options.consumer_secret,
                    options.access_token, options.token_secret,
                    options.length, options.inator_path)

    if options.dry_run:
        print inator.inator()
    else:
        inator.tweet_inator()

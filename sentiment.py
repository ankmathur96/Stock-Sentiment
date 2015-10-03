from data import word_sentiments
#########################################################################################################
# sentiment.py currently uses a pre-calculated sentiment indexing used in several open source projects. #
# Finance-specific sentiment analysis coming soon.                                                      #
#########################################################################################################

#####UTIL#####
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]
##############

def make_sentiment(value):
    """Return a sentiment, which represents a value that may not exist.

    >>> positive = make_sentiment(0.2)
    >>> neutral = make_sentiment(0)
    >>> unknown = make_sentiment(None)
    >>> has_sentiment(positive)
    True
    >>> has_sentiment(neutral)
    True
    >>> has_sentiment(unknown)
    False
    >>> sentiment_value(positive)
    0.2
    >>> sentiment_value(neutral)
    0
    """
    assert (value is None) or (-1 <= value <= 1), 'Bad sentiment value'
    def sentiment_attributes():
        return value
    return sentiment_attributes

def has_sentiment(s):
    """Return whether sentiment s has a value."""
    sentiment_val = s()
    if sentiment_val == None:
        return False
    return True

def sentiment_value(s):
    """Return the value of a sentiment s."""
    assert has_sentiment(s), 'No sentiment value'
    return s() #s() retrieves the value.

def get_word_sentiment(word):
    """Return a sentiment representing the degree of positive or negative
    feeling in the given word.

    >>> sentiment_value(get_word_sentiment('good'))
    0.875
    >>> sentiment_value(get_word_sentiment('bad'))
    -0.625
    >>> sentiment_value(get_word_sentiment('winning'))
    0.5
    >>> has_sentiment(get_word_sentiment('Berkeley'))
    False
    """
    return make_sentiment(word_sentiments.get(word))

def analyze_tweet_sentiment(tweet):
    """Return a sentiment representing the degree of positive or negative
    feeling in a given text segments
    If no words in the tweet have a sentiment value, return
    make_sentiment(None).

    >>> positive = 'i love my job. #winning'
    >>> round(sentiment_value(analyze_tweet_sentiment(positive)), 5)
    0.29167
    >>> negative = 'i hate my job'
    >>> sentiment_value(analyze_tweet_sentiment(negative))
    -0.25
    >>> no_sentiment = 'berkeley golden bears!', None, 0, 0)
    >>> has_sentiment(analyze_tweet_sentiment(no_sentiment))
    False
    """
    words = tweet_words(tweet)
    sentiment_vals = []
    for each_word in words:
        each_word_sent = get_word_sentiment(each_word)
        if has_sentiment(each_word_sent):
            sentiment_vals.append(sentiment_value(each_word_sent))
    if len(sentiment_vals) == 0:
        return make_sentiment(None)
    return make_sentiment(sum(sentiment_vals) / len(sentiment_vals))
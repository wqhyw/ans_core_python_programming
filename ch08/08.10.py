#! /usr/bin/env python

def counts(sentence):
    """
    @program: count vowels, consonants and words in sentence
    @param: sentence => a sentence
    @return: res
    @rtype: tuple
    """

    res = [0, 0, 0]
    words = sentence.split()
    res[0] += len(words)
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    for word in words:
        for letter in word:
            if letter.lower() in vowels:
                res[1] += 1
            elif letter.lower() in consonants:
                res[2] += 1
            else:
                pass

    return tuple(res)


def test():
    sentence = raw_input("Input a sentence: ")
    res = counts(sentence)
    print "words: {wn}, vowels: {vn}, consonants: {cn}.".format(wn=res[0], vn=res[1], cn=res[2])


if __name__ == '__main__':
    test()

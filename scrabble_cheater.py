import sys

#Notes:
# scrabble_cheater.py provides a list of words and scores that are available for a given RACK of
# letters. On the command line You provide the 7 letters in the RACK and the filter.
#
#What is a filter?
# Most scrabble players are trying to find a word that will work across other words already
# played on the board.
# Sample filter:
#   ++r+   <= provides up to 4 letter words that have an "r"
#   +r+t+  <= provides up to 5 letter words that have an "r" & "t" separated by 1 letter.
#
# Enjoy cheating :-)



def read_command_line():
    if len(sys.argv) < 3:
        print("Usage: scrabble_cheater.py [RACK] [WORD FILTER: ex. ++der+e++")
        sys.exit(1)
    rack = sys.argv[1]
    letter_position = sys.argv[2]
    if len(rack) != 7:
        print("Error: Not enough letters in your RACK (requires 7 letters)")
        sys.exit(1)
    return(rack, letter_position)


def create_wordlist():
    with open("sowpods.txt", "r") as f:
        wordlist = [word.lower().strip() for word in f.readlines()]
    return wordlist


def calc_word_score( word ):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    score = 0
    for i in word:
        score = scores[i] + score
    return score




def check_word(word, rack, word_filter):
    # Performance enhancements - added to help avoid O(n^2) loops below
    if len(word_filter) < len(word):
        return False

#        print(word, scored_results[word])
    i = 0
    while i <= len(word):
        j = 0
        while j < len(rack):
            if word[i] == word_filter[i]:  # check word against filter
                j = len(rack)
            elif word[i] == rack[j] and not(word_filter[i].isalpha()): # check word against rack
                rack = rack.replace(rack[j],'', 1)
                j = len(rack)
            elif j == len(rack)-1 or i == len(word)-1:
                return False
            j = j + 1
        if i == len(word)-1:
            print("check_word() - Good Word: ", word)
            return True
        i = i + 1


def ScrabbleMain(rack, word_filter):
    scored_results = {}
    scored_results_sorted = {}

#    rack, word_filter = read_command_line()
#    rack = "dahae"
#    word_filter = "+a++++"

    wordlist = create_wordlist()
    for word in wordlist:
        if check_word(word, rack, word_filter):
            scored_results[word] = calc_word_score(word)

    # value-based sorting and printing
    scored_results_sorted = {k: v for k, v in sorted(scored_results.items(), key=lambda x: x[1], reverse=True)}
    print("ScrabbleMain - Scored Results Sorted: ", scored_results_sorted )
    return(scored_results_sorted)






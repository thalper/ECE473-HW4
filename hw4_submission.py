import shell
import util
import wordsegUtil

############################################################
# Problem 1: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def start(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def goalp(self, state):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def expand(self, state):
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 2: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def goalp(self, state):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def expand(self, state):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE


if __name__ == '__main__':
    shell.main()

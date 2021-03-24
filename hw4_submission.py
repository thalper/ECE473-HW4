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
        return 0
        # raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def goalp(self, state):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return len(self.query) == state
        # raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def expand(self, state):
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        expList = []
        for i in range(state,len(self.query)):
            action = self.query[state:i+1]
            newState = i + 1
            cost = self.unigramCost(action)
            expTuple = (action, newState, cost)
            expList.append(expTuple)
        return expList
        # END_YOUR_CODE

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return ' '.join(ucs.actions)
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
        return (wordsegUtil.SENTENCE_BEGIN, 0)
        # END_YOUR_CODE

    def goalp(self, state):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return state[1] == len(self.queryWords) - 1
        # END_YOUR_CODE

    def expand(self, state):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        expList = []
        PF = []
        word = self.queryWords[state[1] + 1]
        PF = self.possibleFills(word)
        if len(PF) == 0:
            action = word
            newState = (action, state[1] + 1)
            cost = self.bigramCost(state[0], action)
            expTuple = (action, newState, cost)
            expList.append(expTuple)
        for y in PF:
            cost = self.bigramCost(state[0], y)
            action = y
            newState = (action, state[1] + 1)
            expTuple = (action, newState, cost)
            expList.append(expTuple)
                    
        return expList
        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    if len(queryWords) == 0:
        return ''
    queryWords.insert(0, wordsegUtil.SENTENCE_BEGIN)
    bcs = util.UniformCostSearch(verbose=0)
    bcs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))

    return ' '.join(bcs.actions)
    # END_YOUR_CODE


if __name__ == '__main__':
    shell.main()

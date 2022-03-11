# logicBottomUp.py - Bottom-up Proof Procedure for Definite Clauses
# AIFCA Python3 code Version 0.8.4 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2020.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from logicProblem import yes

def fixed_point(kb):
    """Returns the fixed point of knowledge base kb.
    """
    fp = ask_askables(kb)
    added = True
    while added:
        added = False   # added is true when an atom was added to fp this iteration
        for c in kb.clauses:
            if c.head not in fp and all(b in fp for b in c.body):
                fp.add(c.head)
                added = True
                kb.display(2,c.head,"added to fp due to clause",c)
    return fp

def ask_askables(kb):
    return {at for at in kb.askables if yes(input("Is "+at+" true? "))}

#import Ch5.11 excercise 4 KB
from logicProblem import ex4_KB
def test(kb=ex4_KB, fixedpt = {'e', 'c', 'b', 'j', 'a'}):
    fp = fixed_point(kb)
    assert fp == fixedpt, "kb gave result "+str(fp)
    print("Passed unit test")

if __name__ == "__main__":
    test()

    
    ex4_KB.max_display_level=3  # give detailed trace
    print(fixed_point(ex4_KB))  # gives bottom-up proof procedure
    #           and returns C.


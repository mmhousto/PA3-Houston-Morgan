# logicTopDown.py - Top-down Proof Procedure for Definite Clauses
# AIFCA Python3 code Version 0.8.4 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2020.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from logicProblem import yes

def prove(kb, ans_body, indent=""):
    """returns True if kb |- ans_body
    ans_body is a list of atoms to be proved
    """
    kb.display(2,indent,'yes <-',' & '.join(ans_body))
    if ans_body:
        selected = ans_body[0]   # select first atom from ans_body
        if selected in kb.askables:
            return (yes(input("Is "+selected+" true? "))
                    and  prove(kb,ans_body[1:],indent+"    "))
        else:
            return any(prove(kb,cl.body+ans_body[1:],indent+"    ")
                       for cl in kb.clauses_for_atom(selected))
    else:
        return True    # empty body is true

from logicProblem import ex4_KB
def test2():
    a1 = prove(ex4_KB,['a'])
    assert a1, "ex4_KB proving a gave "+str(a1)
    a2 = prove(ex4_KB,['j'])
    assert a2, "ex4_KB proving j gave "+str(a2)
    print("Passed unit tests")
if __name__ == "__main__":
    test()   
# elect.max_display_level=3  # give detailed trace
# prove(elect,['live_w6'])
# prove(elect,['lit_l1'])


from logicProblem import ex4_KB, yes # imports KB
from aipython.logicBottomUp import fixed_point, test # imports bottom-up
from aipython.logicTopDown import prove, test2 # imports top-down

if __name__ == "__main__":
    # BOTTOM UP
    print("BOTTOM UP PROOF PROCEDURE")
    test() # tests KB and fixed points
    print("Trace of values assigned to 'C' in the Bottom-Up Proof Procedure is: ")
    ex4_KB.max_display_level=3  # give detailed trace
    print(fixed_point(ex4_KB))  # gives bottom-up proof procedure
    #           and returns C (all logical consequences of ex4_KB).

    # TOP DOWN
    print("\nTOP DOWN PROOF PROCEDURE")# derivation for the query 'ask a'.
    ex4_KB.max_display_level=1
    test2() # tests ask queries: 'ask a' and 'ask j'
    ex4_KB.max_display_level=3
    print("For query 'ask a':")
    prove(ex4_KB,['a']) # ask a


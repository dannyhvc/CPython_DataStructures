'''
Author: Daniel Herrera-Vazquez
'''
from typing import List


def lis(L: List[int]) -> List:
    ''' Longest Increasing Sub-sequence
    ===================================
    Dynamic Programming problem to see what increasing
    sequence in list is longer than the others within a list
    -----------------------------------------------------------------
    ## Pseudo Code:
    ```txt
    VAR subSeqList
    VAR a,b,c WHERE a,b,c ARE items IN subSeqList SUCH THAT a < b < c
    FOR EACH IN subSeqList AS item:
        IF b < c AND a < b THEN
            subSeqList = `[...a, b]`
        ELSE
            subSeqList = `[...a, c]` 
    ```
    '''
    alpha: List[int] = []  # final list
    beta: List[int] = []  # list to compare too
    for item in L:
        # if list is empty then add first element to the list
        if not len(alpha):
            alpha.append(item)
        elif alpha[-1] < item:
            alpha.append(item)
        else:
            if not len(beta):
                beta.append(item)
            elif beta[-1] < item:
                beta.append(item)
            elif len(beta) == 1:
                if beta[-1] > item:
                    beta = [item]

        ''' edge cases for the '''
        if len(alpha) <= len(beta):
            if alpha[-1] > beta[-1]:
                alpha = beta.copy()
                beta.clear()
        elif (len(beta) > 0)\
                and (beta[0] <= alpha[-1]) and (beta[0] >= alpha[-2]):
            # edge case.
            alpha.pop()
            for x in beta:
                alpha.append(x)
            beta.clear()

        print(f"alpha = {alpha}")
        print(f'beta  = {beta}\n')


if __name__ == '__main__':
    lis([7, 3, 4, 1, 7, 0, 1, 2, 7, 3, 7, 4, 5])

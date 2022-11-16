#!/bin/python3


def process_shortcut( val, index, ans ):
    start = ans[index]
    lowerIdx, higherIdx = index - 1, index + 1

    lowerStop = False
    higherStop = False

    while lowerIdx > 0 or higherIdx < len(ans) - 1:
        if lowerIdx > 0 and ans[lowerIdx] > val:
            ans[lowerIdx] = val
            lowerIdx -= 1
        elif not lowerStop:
            lowerStop = True
        if higherIdx < len(ans)-1 and ans[higherIdx] > val:
            ans[higherIdx] = val
            higherIdx += 1
        elif not higherStop:
            higherStop = True

        val += 1

        if higherStop and lowerStop:
            break
    return ans

def process_intersections():
    n = int( input() )
    shortcuts = [ int( x ) for x in input().split() ]

    # List of stamina needed / intersections
    ans = list( range(0, n) )

    for i in range(0, n):
        j = shortcuts[i]

        # Indexing is not the same for shortcut and i
        if i > 0 and ( ans[i-1] + 1 ) < ans[i]:
            ans[i] = ans[i-1]+1
        if i < j - 2:
            if ans[j-1] > ans[i] + 1:
                ans[j-1] = ans[i] + 1
                ans = process_shortcut( ans[j-1] + 1, j-1, ans )
    print( *ans )


process_intersections()

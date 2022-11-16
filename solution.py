#!/bin/python3

def process_shortcut( val, index, ans ):
    start = ans[index]
    lowerIdx = index - 1
    lowerStop = False

    # Walk backward after taking a shortcut to see if we can save stamina
    while lowerIdx > 0:
        if lowerIdx > 0 and ans[lowerIdx] > val:
            ans[lowerIdx] = val
            lowerIdx -= 1
        else:
            break
        val += 1

    return ans

def process_intersections():
    # Process input
    n = int( input() )
    shortcuts = [ int( x ) for x in input().split() ]

    # List of stamina needed / intersections
    ans = list( range(0, n) )

    for i in range(0, n):
        j = shortcuts[i]

        # Indexing is not the same for shortcut and i
        if i > 0 and ( ans[i-1] + 1 ) < ans[i]:
            ans[i] = ans[i-1]+1

        # Check if we really would win anything by going through the shortcut
        if i < j - 2 and ans[j-1] > ans[i] + 1:
            ans[j-1] = ans[i] + 1
            ans = process_shortcut( ans[j-1] + 1, j-1, ans )
    print( *ans )


process_intersections()

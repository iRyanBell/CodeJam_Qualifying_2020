# Nesting Depth
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f


t = int(input())
for i in range(1, t + 1):
    S = input()
    S_Nested = []
    depth = 0
    for j in range(len(S)):
        s = int(S[j])
        depthDelta = abs(s - depth)
        if s > depth:
            # Increase nesting depth.
            depth += depthDelta
            for k in range(depthDelta):
                S_Nested.append('(')
            S_Nested.append(str(s))
        elif s < depth:
            # Decrease nesting depth.
            depth -= depthDelta
            for k in range(depthDelta):
                S_Nested.append(')')
            S_Nested.append(str(s))
        else:
            # Continue at depth.
            S_Nested.append(str(s))

    for k in range(depth):
        # Close remaining depth.
        S_Nested.append(')')

    print("Case #{}: {}".format(i, ''.join(S_Nested)))

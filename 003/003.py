# Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

t = int(input())


def check_schedule_conflict(s1, s2):
    # New event precedes scheduled event.
    if s1[0] <= s2[0] and s1[1] <= s2[0]:
        return False

    # New event follows scheduled event.
    if s1[0] >= s2[1] and s1[1] >= s2[1]:
        return False

    return True


for i in range(1, t + 1):
    N = int(input())

    S = []  # Schedule
    C = []  # Schedule: Cameron
    J = []  # Schedule: Jamie

    is_doable = True

    for j in range(N):
        # [Start, End] (minutes)
        se = [int(x) for x in input().strip().split(' ')]
        S.append([j, se])

    # Sort by start times
    S.sort(key=lambda x: x[1][0])

    for j in range(N):
        idx = S[j][0]
        se = S[j][1]

        # Check Cameron's schedule
        is_conflict_cameron = False
        for event in C:
            is_conflict = check_schedule_conflict(se, event[2])
            if is_conflict:
                is_conflict_cameron = True
                break

        # Fallback: Jamie's schedule
        is_conflict_jamie = False
        if is_conflict_cameron:
            for event in J:
                is_conflict = check_schedule_conflict(se, event[2])
                if is_conflict:
                    is_conflict_jamie = True
                    break
            if is_conflict_jamie:
                is_doable = False
            else:
                J.append([idx, "J", se])
        else:
            C.append([idx, "C", se])

    if is_doable:
        S = C + J  # Full schedule
        S.sort(key=lambda x: x[0])  # Sort by event idx
        S = [x[1] for x in S]
        print("Case #{}: {}".format(i, "".join(S)))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))

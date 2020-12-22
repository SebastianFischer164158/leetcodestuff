def numberOfMatches(n: int) -> int:
    total_match_count = 0
    while n > 1:
        if n % 2 == 0:
            matches_played = n / 2
            teams_advancing = matches_played
        else:
            matches_played = (n - 1) / 2
            teams_advancing = (n - 1) / 2 + 1
        print(f"ROUND -> Teams = {n} , Matches = {matches_played}, teams advancing = {teams_advancing}")
        total_match_count += matches_played
        n -= matches_played
    return int(total_match_count)


print(numberOfMatches(n=14))

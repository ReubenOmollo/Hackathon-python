def is_match(s, p):
    #defines a function is_match that takes two arguments s and p.
    # Initialize the DP table with False values
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    #This line initializes a 2D list (table) called dp with dimensions (len(s) + 1) x (len(p) + 1). Each element in the table is set to False initially.
    #The table will be used to store whether substrings of s match substrings of p.

    # Base case: Empty string and empty pattern is a match
    dp[0][0] = True #This sets the value of dp[0][0] to True
    
    # Handle patterns with '*' at the beginning
    for j in range(2, len(p) + 1):
        if p[j-1] == '*':#This loop iterates through the pattern p starting from the second character (index 2) to check if the pattern can match an empty string.
            dp[0][j] = dp[0][j-2] #dp[0][j] = dp[0][j-2] means that if * can match zero occurrences, then the match status at dp[0][j] is the same as dp[0][j-2].

    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            #this loop iterates over the character of string s and pattern p.
            # The outer loop goes through each character of s (index i), and the inner loop goes through each character of p (index j).


            if p[j-1] == '.' or p[j-1] == s[i-1]:
                #This checks if the current character in the pattern p (at j-1) is a wildcard . or if it matches the character in s (at i-1).
                # Direct match or '.' wildcard match

                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                #This checks if the current character in the pattern p is a *.
                # '*' can mean zero occurrences or one/more occurrences of the previous character
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if p[j-2] == s[i-1] or p[j-2] == '.' else False)

                #dp[i][j-2]: This represents the case where * matches zero occurrences of the preceding character.
                # Thus, we look at the match status without the preceding character and the *.

                #dp[i-1][j]: This checks if the preceding character (at j-2) matches the current character in s (at i-1).
                # If they match (or if the preceding character is .), it indicates that * can match one or more occurrences of that character.

    # The answer is whether the full string s matches the full pattern p
    return dp[len(s)][len(p)]
    #Finally, this returns the value of dp[len(s)][len(p)], which indicates whether the entire string s matches the entire pattern p.

# Example usage
s = "aab"
p = "c*a*b"
result = is_match(s, p)
print(f"The pattern '{p}' matches the string '{s}': {result}")

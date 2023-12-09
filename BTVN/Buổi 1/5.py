def find_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1
print(find_substring("abcdef", "bc"))          
print(find_substring("abcdefabcdef", "bc"))
print(find_substring("abcdefabcdef", "al"))    
    

from sys import stdin

s = stdin.readline().rstrip()

def better_rle(s):
    """
    performs optimal rle on valid utf char string
    asymptotic runtime: O(n)
    space complexity: O(1)
    """
    if s == '':
        return s

    rle = '' #init rle
    count = 1 #init frequency count to 1
    
    last_char = s[0] #grab first char in string
    ptr = 1 #init pointer to first index (second char, if exists) in string

    while ptr < len(s): #loop through rest of chars from index 1 to len(s) - 1
        curr_char = s[ptr] #grab char at current pointer

        if last_char == curr_char: #compare last seen char with char at pointer, if same
            count += 1  #increment frequency count by one
            last_char = curr_char #set last seen character to character at current pointer
        else: #if not same
            rle += (str(count) + last_char) #add rle pair to rle
            
            last_char = curr_char #set last seen char to character at current pointer
            count = 1 #reset count to 1

        ptr += 1 #increment the pointer to walk through input string

    rle += (str(count) + last_char) #add last chunk/sequence/rle pair

    return rle #return rle string

def rle(s):
    """
    performs rle on valid utf char string
    asymptotic runtime: O(n)
    space complexity: O(n)
    """
    if s == '':
        return s

    ch_stack = [c for c in s] #build stack from input string
    reversed_rle = '' #since we're using a stack, we build rle in reverse

    last_ch = ch_stack.pop() #get last char from stack to begin rle
    count =  1 #init count to 1

    while ch_stack: # while the stack is not empty
        ch = ch_stack.pop() #get current char from stack for comparison with last seen char
        
        if ch == last_ch: #if curr character is same as last seen
            count += 1 #increment count of current sequence
            last_ch = ch #update last seen character to current
        else: #otherwise
            reversed_rle += (last_ch + str(count)) #add rle of current sequence to reversed rle string
            last_ch = ch #update last seen character to current
            count = 1

    reversed_rle += (last_ch + str(count)) #add last chunk/sequence

    return reversed_rle[::-1] #return a reverse of the reversed rle

print(better_rle(s))


from sys import stdin

s = stdin.readline().rstrip()

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

print(rle(s))


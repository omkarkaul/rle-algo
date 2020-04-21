from sys import stdin

rle = stdin.readline().rstrip()

def build_run(rle):
    """
    builds original string from rle string
    asymptotic runtime: O(k^n) in the worst case 
    space complexity: O(k^n) in the worst case
    where k is the average frequency out of all rle pairs in the rle
    """
    run = '' #initialize empty run string

    for i in range(0, len(rle), 2): #loop through each rle pair
        frequency = int(rle[i]) #first element in pair is frequency
        character = rle[i+1] #second element is actual character
        
        for _ in range(frequency): #loop frequency number of times
            run += character #add actual character to the run
    
    return run #return original run

print(build_run(rle))


"""
Carl Bechie
CIS 185
ex 11.2
"""

def reverse(lyst):
    # Define your reverse function here without using the reverse function.
    reversedLyst = []  # a Lyst to hold a new reversed lyst
    
    # ------------> Big O notation = O(n)  <----------------------
    for index in range(len(lyst) -1, -1, -1):  # start at the last index of lyst and apped to the revesed lyst 
        reversedLyst.append(lyst[index]) 

    return reversedLyst 

def main():
    """Tests with two lists."""
    lyst = list(range(8)) # get a list with numbers 0 - 7 

    print("\nNormal Lyst:   ", lyst)
    print("Reversed Lyst: ", reverse(lyst), "\n")
    
    lyst = list(range(6)) # make a list with numbers 0 - 5
    print("Normal Lyst:   ", lyst)
    print("Reversed Lyst: ", reverse(lyst), "\n")
    

if __name__ == "__main__":
     main()

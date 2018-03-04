notes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b'] #all notes

#series of whole and half steps for each type of key
major = [2,2,1,2,2,2,1]
minor = [2,1,2,2,1,2,2]
harmonicMinor = [2,1,2,2,1,3,1]
melodicMinor = [2,1,2,2,2,2,1]

def getscale(root= 'c', seq = major): 
    global notes
    out = [root] 
    pos = notes.index(root) #start position at root
    
    for offset in seq: #for each additional note
        pos+=offset #adjust position
        if pos>11: # loop around if out of index 
            pos%=11
            pos-=1
        out.append(notes[pos]) #append note
    return out #return out list 

if __name__ == "__main__": #for testing
    print(getscale('c',melodicMinor))

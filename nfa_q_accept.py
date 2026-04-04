with open("nfa.txt", 'r') as nfa:
    #get number of states
    num_states = int(nfa.readline().strip())
    print("There are " + str(num_states) + " states")

    #get start state
    start_state = int(nfa.readline().strip())
    print("q" + str(start_state) + " is the start state")

    #get number of accept states
    num_accepts = int(nfa.readline().strip())
    
    #set accept states
    list_of_accepts = []
    for i in range(num_accepts):
        list_of_accepts.append(int(nfa.readline().strip()))
    print("accept states:", list_of_accepts)

    #get alphabet
    alphabet = list(nfa.readline().strip())
    print("This is the alphabet: ", alphabet)

    #get number of transitions
    num_transitions = int(nfa.readline().strip())

    #make transitions list
    trans = []
    for i in range(num_transitions):
        trans.append(nfa.readline().strip())
    print("All transitions: ",trans)



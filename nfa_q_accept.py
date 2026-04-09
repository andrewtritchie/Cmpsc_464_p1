test_string = "0"
out = False
with open("nfa.txt", 'r') as nfa:
    #get number of states
    num_states = int(nfa.readline().strip())
    #print("There are " + str(num_states) + " states")

    #get start state
    start_state = int(nfa.readline().strip())
    #print("q" + str(start_state) + " is the start state")

    #get number of accept states
    num_accepts = int(nfa.readline().strip())
    
    #set accept states
    list_of_accepts = []
    for i in range(num_accepts):
        list_of_accepts.append(int(nfa.readline().strip()))
    #print("accept states:", list_of_accepts)

    #get alphabet
    alphabet = list(nfa.readline().strip())
    #print("This is the alphabet: ", alphabet)

    #get number of transitions
    num_transitions = int(nfa.readline().strip())

    #make transitions list
    trans = []
    for i in range(num_transitions):
        trans.append(nfa.readline().strip())
    #print("All transitions: ",trans)


    for a in list_of_accepts:
        current_states = {a}
        dummy_string = test_string
        
        
        while(len(dummy_string)>0):
            next_states = set()
            state_flag = False
            for state in current_states:
                for t in trans:
                    src, sym, dst = [x.strip() for x in t.split(',')]
                    if state ==int(dst):
                        if sym == "E":
                            next_states.add(int(src))
                        elif dummy_string[-1] == sym:
                            next_states.add(int(src))
                            state_flag=True
            if not next_states:
                break
            if state_flag:
                dummy_string = dummy_string[:-1]
            current_states = next_states
            
        #If the dummy string is empty and we are at a start state, we return true
        if len(dummy_string) == 0 and start_state in current_states:
            out = True
    print(out)

        

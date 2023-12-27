# qlearn.py
# Created by: Eric Dean
# Created on: 12/26/23
# Last Updated: 12/26/23
# Comment: First AI -- Warehouse Optimization

# Importing modules
import numpy as np

# Setting discount factor and learning rate
gamma = 0.75
alpha = 0.9

# Part 1 - Defining the Environment

# Defining the states
location_to_state = {'A': 0,
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8,
                     'J': 9,
                     'K': 10,
                     'L': 11}

# Defining the actions
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# Defining the rewards
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,1,0,0,0,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,1000,1,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1],
[0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,1],
[0,0,0,0,0,0,0,1,0,0,1,0]])

# PART 2 - BUILDING THE AI SOLUTION WITH Q-LEARNING
# Initializing the Q-Values
Q = np.array(np.zeros([12,12]))

# Implementing the Q-Learning Process

# Repeating 1000 times
for i in range(1000):
    
    # Picking a random state
    current_state = np.random.randint(0,12)
    playable_actions = []

    # Looping through all of the actions
    for j in range(12):
        # Reward > 0 
        if R[current_state,j] > 0:
            playable_actions.append(j) 

    # Choose a random next state based on the available actions
    next_state = np.random.choice(playable_actions)
    
    # Finding the Temporal Difference
    TD = R[current_state, next_state] + \
        gamma*Q[next_state, np.argmax(Q[next_state,])] - \
        Q[current_state,next_state]
    
    # Bellman Equation for new Q value
    Q[current_state,next_state] = Q[current_state,next_state] + alpha*TD
    

#print("Q-Values: \n",Q.astype(int))

# PART 3 - GOING INTO PRODUCTION

# Making a mapping from the states to the locations
state_to_location = {state: location for location, state in location_to_state.items()}

# Starting at Location E = 4 -> G = ...

# Making the final function that will return the optimal route
def route(starting_location,ending_location):
    route = [starting_location]
    next_location = starting_location 
    while (next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

# Printing the final route
print('Route:')
out = route('E','G')
print(out) # yay


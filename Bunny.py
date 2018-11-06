# -*- coding: utf-8 -*-
"""
Bunny function

This function takes in an NxM matrix with positive integers. 
It outputs the number of carrots eaten by Bunny. 

I decided to conver the input lists into numpy arrays for easier manipulation
"""

import numpy as np
## I am first writing smaller functions for specific tasks 

# This function finds the center cell for Bunny to start at
# Input is a numpy array, output is the [row,col] location in the array
def get_center(np_array):
    # Grab the dimensions of the array
    n = np_array.shape[0]
    m = np_array.shape[1]
    # Check if the dimension is odd 
    if (n%2 == 1) & (m%2 == 1): # if both are odd, can directly assign center
        # get the middle number
        n_center = n/2
        m_center = m/2
    elif (n%2 == 0) & (m%2 == 1): # if rows are even, check the two values in that column
        m_center = m/2
        # get the two val
        n_poss = n/2
        n_center = n_poss + np_array[(n_poss-1):(n_poss+1), m_center].argmax() - 1
    elif (m%2 == 0) & (n%2 == 1): # if cols are even, check the two values in that row
        n_center = n/2
        m_poss = m/2
        m_center = m_poss + np_array[n_center, (m_poss-1):(m_poss+1)].argmax() - 1
    else: # if both are even
        n_poss = n/2
        m_poss = m/2
        poss = np_array[(n_poss-1):(n_poss+1),(m_poss-1):(m_poss+1)]
        n_center = n_poss + np.where(poss == np.max(poss))[0][0] - 1
        m_center = m_poss + np.where(poss == np.max(poss))[1][0] - 1
    return(n_center, m_center)
    

def check_adj(np_array, n_loc, m_loc):

'''
I ran out of time to deal with the edge case of a 1d array (either n or m = 1).
To do this more elegantly, I would pull out each check adjacent into a separate
function (check_up, check_right, etc.) and then use conditional statements to
test for either of those cases and using only the applicable functions. For 
example, if n=1, I would only check right and left, and update accordingly. 

'''

def Bunny(garden):
    # Convert the nested list into a numpy array
    garden_np = np.array(garden)
    
    n_max = garden_np.shape[0] - 1 # correct for zero index
    m_max = garden_np.shape[1] - 1 
    
    # Start Bunny at the center
    # n_iter and m_iter will keep track of Bunny's location
    n_prev, m_prev = get_center(garden_np)
    # Initialize the carrot count
    carrots = 0
    
    # keep iterating until the break condition is met
    while True: 
        # Carrots will keep the total number eaten
        carrots += garden_np[n_prev, m_prev]
        # Remove the carrots eaten
        garden_np[n_prev, m_prev] = 0
        # Set the new steps as previous
        n_new = n_prev
        m_new = m_prev
        
        # Check all adjacent cells, storing their values in a set pattern of 
        # up, right, down, left so I can update the n_iter and m_iter 
        adj = np.zeros(4)
        
        # Update the adj array but only if it's a valid move
        # Up
        if n_prev > 0:
            adj[0] = garden_np[n_prev-1, m_prev]
        # Right
        if m_prev < m_max:
            adj[1] = garden_np[n_prev, m_prev+1]
        # Down
        if n_prev < n_max:
            adj[2] = garden_np[n_prev+1, m_prev]
        # Left
        if m_prev > 0:
            adj[3] = garden_np[n_prev, m_prev-1]
        
        # Update the new position Bunny should go
        direction = adj.argmax()
        if direction == 0:
            n_new -= 1
        if direction == 1:
            m_new += 1
        if direction == 2:
            n_new += 1
        if direction == 3:
            m_new -= 1
                    
        # If no more carrots to eat, break
        if (sum(adj) == 0):
            break
        else: # Move Bunny to the new cell
            n_prev = n_new
            m_prev = m_new
    
    
    # Give back the carrots eaten
    return(carrots)
    
    
   
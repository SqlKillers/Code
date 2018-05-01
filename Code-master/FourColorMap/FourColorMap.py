import pyodbc
import os

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=H:\Documents\code\Code-master\States1.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

"""
SAMPLE LISTS:

# list of states
state_arr = ["A", "A", "B", "B", "B", "C", "C", "C", "D", "D"]
# list of states touching those states
touch_arr = ["B", "C", "A", "C", "D", "A", "B", "D", "B", "C"]
# Every instance of that state will be colored, refers to the states in touch_arr
color_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Outputs the colors of the states to final_color_arr for easier output to the form
final_color_arr = [0, 0, 0, 0]
"""
state_arr = []
touch_arr = []
color_arr = []
final_color_arr = []

cursor.execute("SELECT Abbreviation,Adjacent,Color FROM qryGetColors")
for row in cursor:
    state_arr.append(row.Abbreviation)
    touch_arr.append(row.Adjacent)
    color_arr.append(row.Color)
    
def check_lengths(state_arr, touch_arr, color_arr):
    if len(state_arr) != len(touch_arr) or len(state_arr) != len(color_arr):
        print("State list:", len(state_arr), "\nTouching State list:", len(touch_arr), "\nColor Array:", len(color_arr),
              "\nArrays aren't equal lengths!")
    else:
        print("Lists are equal lengths.")

def find_touching(state_arr, touch_arr, color_arr):
    i = 0
    j = 0
    
    current_state = 0
    next_state = 0
    
    # pointer list keeps track of where each state starts
    # p is the index of the pointer list
    p = 0
    pointer_arr = []
    color_subset = []
    while i < len(state_arr):
        pointer_arr.append(current_state)
       
        
        num_occur = state_arr.count(state_arr[next_state])
        j = next_state
        next_state = next_state + num_occur

        # creates a list of colors whoose touching_states are the same as the current_state
        while j < next_state:
            color_subset.append(color_arr[j])
            j += 1           
        state_color = get_color(color_subset)
        print(state_color)
        
        if state_color != -1 and next_state != len(state_arr):
            for k in range(len(touch_arr)):
                if state_arr[current_state] == touch_arr[k]:
                    color_arr[k] = state_color
            previous_state = current_state
            current_state = next_state
         
        elif state_color == -1:
            print(pointer_arr)
            print(p)
            i = pointer_arr[p-1]
            j = pointer_arr[p]
            break
        p += 1
        i = next_state
        print(color_subset)
        color_subset = []
        print(i)
        


def get_color(colors):
    is_used = [False, False, False, False]

    # Every existing color is set to True
    for color in colors:
        is_used[color] = True

    # Checks 'is_used' for the first false value, the index of that gives the color to return
    for i in range(len(is_used)):
        if is_used[i] is False:
            return i

    # returns -1 incase the program needs to go backwards
    return -1
    print(is_used)



check_lengths(state_arr, touch_arr, color_arr)
find_touching(state_arr, touch_arr, color_arr)



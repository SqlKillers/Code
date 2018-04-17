# list of states
state_arr = ["A", "A", "B", "B", "B", "C", "C", "C", "D", "D"]
# list of states touching those states
touch_arr = ["B", "C", "A", "C", "D", "A", "B", "D", "B", "C"]
# Every instance of that state will be colored, refers to the states in touch_arr
color_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Outputs the colors of the states to final_color_arr for easier output to the form
final_color_arr = [["A",0],["B",0],["C",0],["D",0],["E",0]]

#Makes sure the arrays are the same length
def check_lengths(state_arr, touch_arr, color_arr):
    if len(state_arr) != len(touch_arr) or len(state_arr) != len(color_arr):
        print("State list:", len(state_arr), "\nTouching State list:", len(touch_arr), "\nColor Array:", len(color_arr),
              "\nArrays aren't equal lengths!")
    else:
        print("Lists are equal lengths.")


def find_touching(state_arr, touch_arr, color_arr):
    i = 0
    color_subset = []
    current_state = 0
    next_state = 0
	
    while i < len(state_arr):
		# Gets the number of the occurrences for the current state 
        num_occur = state_arr.count(state_arr[next_state])
        j = next_state
		# Where is the next state in the array?
        next_state = next_state + num_occur

        # creates a list of colors whoose touching_states are the same as the current_state
		# From the first occurrence of the current state up to the first occurrence of the next state, create a subset of those colors.
        while j < next_state:			
            color_subset.append(color_arr[j])
            j += 1			
		#Gets the color of the current state
        state_color = get_color(color_subset)
		
        if state_color != -1 and next_state != len(state_arr):
			#Applies the color to every instance of the current state in the touch_arr
            for k in range(len(touch_arr)):
                if state_arr[current_state] == touch_arr[k]:
                    color_arr[k] = state_color
			#Sets the current_state to the next state for the next loop
            current_state = next_state
		#Clears the subset
        color_subset = []
		#Next loop will skip to the next_state
        i = next_state


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
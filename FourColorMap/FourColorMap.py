
"""
VBA Function:

Function find_touching(states_arr As String, adjacent_arr As String)
    Dim num_occur As Integer
    Dim first_occur As Integer
    Dim next_state As Integer
    Dim i As Integer
    Dim j As Integer
    Dim flag As Boolean
    next_state = 0
    
    For i = 0 To UBound(states_arr) Step 1
        MsgBox state_arr(next_state)
        used_state(i) = states_arr(next_state)
        flag = False
        
        For j = 0 To UBound(states_arr) Step 1
            If (flag = False & used_state(0) = states_arr(j)) Then
                first_occur = j
                num_occur = num_occur + 1
                flag = True
            ElseIf (flag = True & used_state(0) = states_arr(j)) Then
                num_occur = num_occur + 1
            Else
                break
            next_state = first_occur + num_occur + 1
            
End Function
"""

# list of states
state_arr = ["A", "A", "B", "B", "B", "C", "C", "C", "D", "D"]
# list of states touching those states
touch_arr = ["B", "C", "A", "C", "D", "A", "B", "D", "B", "C"]
# Every instance of that state will be colored, refers to the states in touch_arr
color_arr = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
# Outputs the colors of the states to final_color_arr for easier output to the form
final_color_arr = [0, 0, 0, 0]


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
        num_occur = state_arr.count(state_arr[next_state])
        j = next_state
        next_state = next_state + num_occur

        # creates a list of colors whoose touching_states are the same as the current_state
        while j < next_state:
            color_subset.append(color_arr[j])
            j += 1
        state_color = get_color(color_subset)

        if state_color != -1 and next_state != len(state_arr):
            for k in range(len(touch_arr)):
                if state_arr[current_state] == touch_arr[k]:
                    color_arr[k] = state_color
            current_state = next_state
        color_subset = []
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
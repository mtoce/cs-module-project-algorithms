'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # First-pass solution: run-time ~0.14s (bad implementation since used a double for-loop)
    # this solution only works if the repeated numbers are next to each other
    repeated = []
    for i in range(len(arr)):
        k = i + 1
        # check the next value and if they are equal and not already in repeated
        # append it to the repeated numbers list
        for j in range(k, len(arr)):
            if arr[i] == arr[j] and arr[i] not in repeated:
                repeated.append(arr[i])
        # then after the j loop is done, during the i loop check if number is in repeated
        # if it isn't, then it is the solo dolo and we can return it
        if arr[i] not in repeated:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

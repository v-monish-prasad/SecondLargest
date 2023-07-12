def secondLargest(array):
    if not array:
        return "Empty Array."

    count = 0
    maximum, preMax = array[0], -1

    for i in range(1, len(array)):
        if array[i] >= maximum:
            preMax = maximum
            maximum = array[i]
        else:
            if array[i] > preMax:
                preMax = array[i]

    return preMax


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(secondLargest(array))

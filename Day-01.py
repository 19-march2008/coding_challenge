def sort012(arr):
    # standard sorting function
    arr.sort()

if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    sort012(arr)
    
    for num in arr:
        print(num, end=" ")

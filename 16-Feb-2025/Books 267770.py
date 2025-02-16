# Problem: Books - https://codeforces.com/contest/279/problem/B

     n, time = list(map(int, input().split()))
     arr = list(map(int, input().split()))
    left = 0
    window = 0
    count = 0
    books = 0
    for right in range(len(arr)):
        books += arr[right]
        while books > time:
            books-=arr[left]
            left+=1

        count = right - left + 1
        window = max(window, count)
        
    return window
    print(books(arr, time))
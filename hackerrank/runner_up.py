# You are given n scores. Store them in a list and find the score of the runner-up.
# The first line contains n . The second line contains an array A[]  of n integers each separated by a space.
# Given list is {2,3,6,6,5} . The maximum score is 6, second maximum is 5 . Hence, we print 5  as the runner-up score.
# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    for scores in n:
        for scores in arr:
            print(max(arr))
from sys import stdin

C = int(stdin.readline().strip())

for _ in range(C):
    stdin.readline()
    height = [int(x) for x in stdin.readline().strip().split()]
    
    def cut(left, right):
        if left == right:
            return height[left]
        else:
            mid = (left + right) // 2
            curr_box = max(cut(left, mid), cut(mid+1, right))

            high, low = mid + 1, mid
            curr_height = min(height[low], height[high])
            curr_box = max(curr_box, curr_height * 2)


            while left < low or high < right:
                if high < right and (low == left or height[low - 1] < height[high + 1]):
                    high += 1
                    curr_height = min(curr_height, height[high])
                else:
                    low -= 1
                    curr_height = min(curr_height, height[low])
                curr_box = max(curr_box, curr_height * (high - low + 1))
            return curr_box
    print(cut(0, len(height) - 1))
            
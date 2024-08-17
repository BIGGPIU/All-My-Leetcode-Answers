Sample = [-1,0,2,4,6,8]
target = 4
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = right//2
        while (right >= left):
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                mid = right//2 
            elif nums[mid] < target:
                left = mid + 1
                hold = (right - left)//2
                mid = left + hold
                
        return -1
        
        



if __name__ == '__main__':
    hold = (Solution.search(None,Sample,target))
    print (hold)
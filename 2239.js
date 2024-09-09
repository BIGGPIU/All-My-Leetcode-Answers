/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let mem = 999999
    nums.sort()
    for (let i = 0; i < nums.length(); i++) {
        if (Math.abs(nums[i]) <= Math.abs(mem)) {
            mem = Math.abs(nums[i])
        }
    }
};


findClosestNumber([-4,-2,1,4,8])
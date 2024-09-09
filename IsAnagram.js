class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let a = []
        let x = 0
        for (let i = 0; i<s.length; i++) {
            a.push(s[i])
        }
        for (let i = 0; i <t.length; i++) {
            if (a.includes(t[i])) {
                x = a.indexOf(t[i])
                a.pop(x)
            }
            else {
                return false
            }
        }
        return true
    }
}

let crashout = new Solution()
crashout.isAnagram("racecar","carrace")

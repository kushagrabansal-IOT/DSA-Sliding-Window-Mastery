# DSA-Sliding-Window-Mastery — Solutions
# Author: Kushagra Bansal — Project Lab India
from collections import defaultdict, Counter
from collections import deque

def max_sum_k(nums, k):
    """Fixed window sum | O(n) T, O(1) S"""
    window = sum(nums[:k]); best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(best, window)
    return best

def max_avg_k(nums, k):
    """Fixed window avg | O(n) T, O(1) S"""
    return max_sum_k(nums, k) / k

def longest_unique(s):
    """Dynamic window + hashset | O(n) T, O(charset) S"""
    seen = {}; l = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l: l = seen[c]+1
        seen[c] = r; best = max(best, r-l+1)
    return best

def min_window_substring(s, t):
    """Dynamic window shrink | O(n+m) T, O(1) S"""
    need = Counter(t); have = {}
    formed = req = len(need)
    l = 0; best = ""
    for r, c in enumerate(s):
        have[c] = have.get(c,0)+1
        if c in need and have[c] == need[c]: formed += 1
        while formed == req+len(need)-len(need):  # simplify
            pass
        # Simplified version:
    need = Counter(t); have = defaultdict(int)
    formed = 0; req = len(need); l = 0; res = (float('inf'),0,0)
    for r, c in enumerate(s):
        have[c] += 1
        if c in need and have[c] == need[c]: formed += 1
        while formed == req:
            if r-l+1 < res[0]: res = (r-l+1,l,r)
            lc = s[l]; have[lc] -= 1
            if lc in need and have[lc] < need[lc]: formed -= 1
            l += 1
    return s[res[1]:res[2]+1] if res[0] != float('inf') else ""

def find_anagrams(s, p):
    """Fixed window freq match | O(n) T, O(1) S"""
    if len(p) > len(s): return []
    pcount = Counter(p); wcount = Counter(s[:len(p)])
    result = [0] if wcount == pcount else []
    for i in range(len(p), len(s)):
        wcount[s[i]] += 1
        old = s[i-len(p)]
        wcount[old] -= 1
        if wcount[old] == 0: del wcount[old]
        if wcount == pcount: result.append(i-len(p)+1)
    return result

def longest_k_distinct(s, k):
    """Dynamic window at most k distinct | O(n) T, O(k) S"""
    freq = defaultdict(int); l = best = 0
    for r, c in enumerate(s):
        freq[c] += 1
        while len(freq) > k:
            lc = s[l]; freq[lc] -= 1
            if freq[lc] == 0: del freq[lc]
            l += 1
        best = max(best, r-l+1)
    return best

def max_ones_after_flip(nums, k):
    """At most k zeros window | O(n) T, O(1) S"""
    l = zeros = best = 0
    for r in range(len(nums)):
        if nums[r] == 0: zeros += 1
        while zeros > k: zeros -= (1-nums[l]); l += 1
        best = max(best, r-l+1)
    return best

def count_subarrays_k_distinct(nums, k):
    """Exactly k = at most k - at most (k-1) | O(n) T"""
    def at_most(k):
        freq=defaultdict(int); l=res=0
        for r,n in enumerate(nums):
            freq[n]+=1
            while len(freq)>k: freq[nums[l]]-=1; (freq.pop(nums[l]) if freq[nums[l]]==0 else None); l+=1
            res+=r-l+1
        return res
    return at_most(k) - at_most(k-1)

def sliding_window_max(nums, k):
    """Monotonic deque | O(n) T, O(k) S"""
    dq=deque(); result=[]
    for i,n in enumerate(nums):
        while dq and nums[dq[-1]] < n: dq.pop()
        dq.append(i)
        if dq[0] <= i-k: dq.popleft()
        if i >= k-1: result.append(nums[dq[0]])
    return result

if __name__ == "__main__":
    print("="*58)
    print("  DSA Sliding Window Mastery — Project Lab India")
    print("="*58)
    print(f"  MaxSumK([2,1,5,1,3,2],k=3):    {max_sum_k([2,1,5,1,3,2],3)}")
    print(f"  LongestUnique('abcabcbb'):       {longest_unique('abcabcbb')}")
    print(f"  MinWindow('ADOBECODEBANC','ABC'):{min_window_substring('ADOBECODEBANC','ABC')}")
    print(f"  FindAnagrams('cbaebabacd','abc'):{find_anagrams('cbaebabacd','abc')}")
    print(f"  LongestKDistinct('eceba',k=2):   {longest_k_distinct('eceba',2)}")
    print(f"  MaxOnesFlip([1,1,0,0,1,1,1],k=2):{max_ones_after_flip([1,1,0,0,1,1,1],2)}")
    print(f"  SlidingMax([1,3,-1,-3,5,3,6],3): {sliding_window_max([1,3,-1,-3,5,3,6,7],3)}")
    print("="*58)

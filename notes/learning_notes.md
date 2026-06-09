# Sliding Window — Learning Notes
# By Kushagra Bansal | Project Lab India

## Fixed vs Dynamic Window
Fixed: window size k is constant
  → Add right, remove left at every step
  → Sum/avg/max in O(n) instead of O(n*k)

Dynamic: window grows/shrinks based on condition
  → Expand right freely
  → Shrink left when condition violated
  → Track best valid window

## Universal Templates

# Fixed Window (size k)
window = sum(nums[:k]); best = window
for i in range(k, len(nums)):
    window += nums[i] - nums[i-k]
    best = max(best, window)

# Dynamic Window (max valid)
l = 0; best = 0
for r in range(len(s)):
    add s[r] to window
    while window is invalid:
        remove s[l] from window; l += 1
    best = max(best, r-l+1)

# Dynamic Window (min valid)
l = 0; best = inf
for r in range(len(s)):
    add s[r] to window
    while window is valid:
        best = min(best, r-l+1)
        remove s[l]; l += 1

## Key Insight: At Most K → Exactly K
exactly_k(arr, k) = at_most(arr,k) - at_most(arr,k-1)

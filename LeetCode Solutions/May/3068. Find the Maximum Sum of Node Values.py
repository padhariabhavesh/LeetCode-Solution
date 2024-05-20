'''

3068. Find the Maximum Sum of Node Values

There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

    Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
        nums[u] = nums[u] XOR k
        nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.


'''

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalSum = 0
        count = 0
        positiveMin = float("inf")
        negativeMax = float("-inf")

        for nodeValue in nums:
            nodeValAfterOperation = nodeValue ^ k

            totalSum += nodeValue
            netChange = nodeValAfterOperation - nodeValue

            if netChange > 0:
                positiveMin = min(positiveMin, netChange)
                totalSum += netChange
                count += 1
            else:
                negativeMax = max(negativeMax, netChange)

        if count % 2 == 0:
            return totalSum
        return max(totalSum - positiveMin, totalSum + negativeMax)

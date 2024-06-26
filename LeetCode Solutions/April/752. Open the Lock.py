'''

752. Open the Lock


You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

https://leetcode.com/problems/open-the-lock/solutions/5056964/752-open-the-lock-python
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque([(0,'0000')])

        def getChildren(lock):
            res = []
            for i in range(4):
                lock1 = lock[:i]+str((int(lock[i])+1)%10)+lock[i+1:]
                lock2 = lock[:i]+str((int(lock[i])-1+10)%10)+lock[i+1:]
                res+=[lock1,lock2]
            return res

        while q:
            turns,code = q.popleft()
            if code==target:
                return turns

            if code in visited:
                continue

            visited.add(code)

            for child in getChildren(code):
                if child not in visited:
                    q.append((turns+1,child))

        return -1



        
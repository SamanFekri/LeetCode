class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Split it to negative, zeros, and positive
        n, z, p = [], [], []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num == 0:
                z.append(num)
            else:
                p.append(num)
        
        # Make the set from each one because we do not want to have duplicate results in output
        N, Z, P = set(n), set(z), set(p)

        result = []
        # If we have >= 3 zeroes
        if len(z) >= 3:
            result.append([0, 0, 0])

        # If we have zero check do we have num and -num
        if len(z) > 0:
            for num in N:
                if -num in P:
                    result.append([num, 0, -num])
        
        # make a dict to only have unique results
        udict = {}
        # Check for each pair in n do we have correspondance number in P which num3 = -(num1 + num2)
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if -(n[i] + n[j]) in P:
                    temp = [n[i], n[j], -(n[i] + n[j])]
                    temp.sort()
                    key = ' '.join(str(temp))
                    if key in udict:
                        continue
                    result.append(temp)
                    udict[key] = temp

        # Check for each pair in p do we have correspondance number in N which num3 = -(num1 + num2) 
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if -(p[i] + p[j]) in N:
                    temp = [p[i], p[j], -(p[i] + p[j])]
                    temp.sort()
                    key = ' '.join(str(temp))
                    if key in udict:
                        continue
                    result.append(temp)
                    udict[key] = temp

        return result

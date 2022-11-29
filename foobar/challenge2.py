def solution(n,b):
    def num2base(n,b):
        if n=="0":
            return "0"
        d=[]
        while n:
            d.append(str(int(n%b)))
            n = int(n // b)
        d.reverse()
        return ''.join(d)
    nums=[n]
    k = len(n)
    def recursor(n,b,nums):
        y = ''.join(sorted(n))
        x=y[::-1]
        z = num2base(int(x,b)-int(y,b),b)
        while len(z)<k:
            z='0'+z
        if z in nums:
            return len(nums)-nums.index(z)
        nums.append(z)
        n=z
        return recursor(n,b,nums)
    return recursor(n,b,nums)

print(solution("0", 3))
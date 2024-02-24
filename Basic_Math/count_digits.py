def countDigits(n: int) -> int:
    ans = 0;
    temp = n
    while n != 0:
        rem = n % 10
        if rem != 0 and temp % rem == 0:
            ans += 1
        n = n // 10
    return ans
# ============================================================
#        TCS NQT - TOP 50 CODING QUESTIONS (Python)
#        Converted from Java | Practice in PyCharm
# ============================================================
# HOW TO USE:
#   - Read the question comment above each solution
#   - Try writing it yourself first, then check the solution
#   - Run each question individually by uncommenting main()
# ============================================================


# ─────────────────────────────────────────────
# Q1. CHECK EVEN OR ODD
# Input: a number n
# Output: "Even" if divisible by 2, else "Odd"
# ─────────────────────────────────────────────
n = int(input())
print("Even" if n % 2 == 0 else "Odd")


# ─────────────────────────────────────────────
# Q2. CHECK PRIME NUMBER
# A prime number is divisible only by 1 and itself (e.g., 2, 3, 5, 7)
# We only check divisors up to sqrt(n) — saves time
# Input: n | Output: "Prime" or "Not Prime"
# ─────────────────────────────────────────────
import math
n = int(input())
prime = True
if n <= 1:
    prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break
print("Prime" if prime else "Not Prime")


# ─────────────────────────────────────────────
# Q3. FACTORIAL OF A NUMBER
# Factorial: n! = 1 × 2 × 3 × ... × n  (e.g., 5! = 120)
# Input: n | Output: factorial value
# ─────────────────────────────────────────────
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)


# ─────────────────────────────────────────────
# Q4. FIBONACCI SERIES (First N Terms)
# Series: 0, 1, 1, 2, 3, 5, 8, 13... (each = sum of previous two)
# Input: n | Output: first n terms
# ─────────────────────────────────────────────
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# ─────────────────────────────────────────────
# Q5. REVERSE A NUMBER
# e.g., 1234 → 4321
# Input: n | Output: reversed number
# ─────────────────────────────────────────────
n = int(input())
rev = 0
while n != 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)


# ─────────────────────────────────────────────
# Q6. CHECK PALINDROME NUMBER
# A number is palindrome if it equals its reverse (e.g., 121, 1331)
# Input: n | Output: "Palindrome" or "Not Palindrome"
# ─────────────────────────────────────────────
n = int(input())
temp, rev = n, 0
while n != 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Palindrome" if temp == rev else "Not Palindrome")


# ─────────────────────────────────────────────
# Q7. ARMSTRONG NUMBER
# A 3-digit Armstrong: sum of cubes of digits = number (e.g., 153 = 1³+5³+3³)
# Input: n | Output: "Armstrong" or "Not Armstrong"
# ─────────────────────────────────────────────
n = int(input())
temp, total = n, 0
while n != 0:
    digit = n % 10
    total += digit ** 3
    n //= 10
print("Armstrong" if temp == total else "Not Armstrong")


# ─────────────────────────────────────────────
# Q8. SUM OF DIGITS
# e.g., 1234 → 1+2+3+4 = 10
# Input: n | Output: sum of all digits
# ─────────────────────────────────────────────
n = int(input())
total = 0
while n != 0:
    total += n % 10
    n //= 10
print(total)


# ─────────────────────────────────────────────
# Q9. LARGEST OF THREE NUMBERS
# Input: three numbers a, b, c | Output: the largest
# ─────────────────────────────────────────────
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))


# ─────────────────────────────────────────────
# Q10. GCD OF TWO NUMBERS (Euclidean Algorithm)
# GCD = Greatest Common Divisor (e.g., GCD(12, 8) = 4)
# Euclidean method: keep replacing (a, b) with (b, a%b) until b=0
# Input: a, b | Output: GCD
# ─────────────────────────────────────────────
a, b = int(input()), int(input())
while b != 0:
    a, b = b, a % b
print(a)


# ─────────────────────────────────────────────
# Q11. LCM OF TWO NUMBERS
# LCM = Least Common Multiple | Formula: LCM = (a × b) / GCD
# Input: a, b | Output: LCM
# ─────────────────────────────────────────────
a, b = int(input()), int(input())
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print(lcm)


# ─────────────────────────────────────────────
# Q12. CHECK LEAP YEAR
# Leap year: divisible by 4 but NOT 100, OR divisible by 400
# Input: year | Output: "Leap Year" or "Not Leap Year"
# ─────────────────────────────────────────────
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# ─────────────────────────────────────────────
# Q13. COUNT VOWELS AND CONSONANTS
# Vowels: a, e, i, o, u | Rest of letters = consonants
# Input: a string | Output: count of vowels and consonants
# ─────────────────────────────────────────────
s = input().lower()
vowels = consonants = 0
for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)


# ─────────────────────────────────────────────
# Q14. REVERSE A STRING
# e.g., "hello" → "olleh"
# Input: a string | Output: reversed string
# ─────────────────────────────────────────────
s = input()
print(s[::-1])


# ─────────────────────────────────────────────
# Q15. CHECK ANAGRAM
# Two strings are anagrams if they have the same characters (e.g., "listen" & "silent")
# Trick: sort both strings and compare
# Input: two strings | Output: "Anagram" or "Not Anagram"
# ─────────────────────────────────────────────
s1 = input()
s2 = input()
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")


# ─────────────────────────────────────────────
# Q16. REMOVE DUPLICATES FROM STRING
# Keep only the first occurrence of each character
# e.g., "programming" → "progamin"
# Input: a string | Output: string without duplicate chars
# ─────────────────────────────────────────────
s = input()
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)


# ─────────────────────────────────────────────
# Q17. FIND SECOND LARGEST IN ARRAY
# Track the largest and second largest while traversing once
# Input: n, then n integers | Output: second largest
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)


# ─────────────────────────────────────────────
# Q18. LINEAR SEARCH
# Check each element one by one until key is found
# Input: n, array elements, key | Output: "Found" or "Not Found"
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
key = int(input())
print("Found" if key in arr else "Not Found")


# ─────────────────────────────────────────────
# Q19. BINARY SEARCH (works only on SORTED array)
# Cuts search space in half each time — much faster than linear
# low/high pointers, check mid each time
# Input: n, sorted array, key | Output: "Found" or "Not Found"
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
key = int(input())
low, high, found = 0, n - 1, False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
print("Found" if found else "Not Found")


# ─────────────────────────────────────────────
# Q20. BUBBLE SORT
# Repeatedly swap adjacent elements if they're in wrong order
# Largest element "bubbles up" to end in each pass
# Input: n, array | Output: sorted array
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(*arr)


# ─────────────────────────────────────────────
# Q21. SELECTION SORT
# Find minimum element and place it at the beginning, repeat
# Input: n, array | Output: sorted array
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(*arr)


# ─────────────────────────────────────────────
# Q22. INSERTION SORT
# Like sorting playing cards — pick each element and insert in correct position
# Input: n, array | Output: sorted array
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(*arr)


# ─────────────────────────────────────────────
# Q23. MATRIX ADDITION
# Add corresponding elements of two matrices
# Input: rows r, cols c, then matrix A, then matrix B
# Output: resultant matrix
# ─────────────────────────────────────────────
r, c = int(input()), int(input())
a = [[int(input()) for _ in range(c)] for _ in range(r)]
b = [[int(input()) for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        print(a[i][j] + b[i][j], end=" ")
    print()


# ─────────────────────────────────────────────
# Q24. TRANSPOSE OF A MATRIX
# Swap rows and columns: element at [i][j] goes to [j][i]
# Input: r, c, matrix | Output: transposed matrix
# ─────────────────────────────────────────────
r, c = int(input()), int(input())
a = [[int(input()) for _ in range(c)] for _ in range(r)]
for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()


# ─────────────────────────────────────────────
# Q25. COUNT FREQUENCY OF ELEMENT IN ARRAY
# How many times does a given number appear in the array?
# Input: n, array, key | Output: count
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
key = int(input())
print(arr.count(key))


# ─────────────────────────────────────────────
# Q26. CHECK IF ARRAY IS SORTED (Ascending)
# Compare each element with the next — if any is greater, not sorted
# Input: n, array | Output: "Sorted" or "Not Sorted"
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
sorted_flag = all(arr[i] <= arr[i + 1] for i in range(n - 1))
print("Sorted" if sorted_flag else "Not Sorted")


# ─────────────────────────────────────────────
# Q27. MERGE TWO ARRAYS
# Combine two arrays into one (no sorting needed)
# Input: n1, array1, n2, array2 | Output: merged array
# ─────────────────────────────────────────────
n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
print(*(a + b))


# ─────────────────────────────────────────────
# Q28. FIND MISSING NUMBER (1 to N)
# Given array has n-1 numbers from 1 to n — find the missing one
# Trick: expected sum = n*(n+1)/2, subtract actual sum
# Input: n, then n-1 numbers | Output: missing number
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
print(n * (n + 1) // 2 - sum(arr))


# ─────────────────────────────────────────────
# Q29. COUNT WORDS IN A STRING
# Split by spaces and count
# Input: a sentence | Output: word count
# ─────────────────────────────────────────────
s = input().strip()
print(0 if not s else len(s.split()))


# ─────────────────────────────────────────────
# Q30. REMOVE ALL SPACES FROM STRING
# e.g., "hello world" → "helloworld"
# Input: string | Output: string without spaces
# ─────────────────────────────────────────────
s = input()
print(s.replace(" ", ""))


# ─────────────────────────────────────────────
# Q31. FIND DUPLICATE ELEMENTS IN ARRAY
# Print elements that appear more than once
# Input: n, array | Output: duplicate elements
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
seen = set()
for num in arr:
    if arr.count(num) > 1 and num not in seen:
        print(num, end=" ")
        seen.add(num)


# ─────────────────────────────────────────────
# Q32. MOVE ALL ZEROS TO END
# Keep non-zero elements in order, push all zeros to end
# e.g., [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# Input: n, array | Output: modified array
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
non_zeros = [x for x in arr if x != 0]
result = non_zeros + [0] * (n - len(non_zeros))
print(*result)


# ─────────────────────────────────────────────
# Q33. ROTATE ARRAY RIGHT BY 1 POSITION
# Last element moves to the front
# e.g., [1, 2, 3, 4, 5] → [5, 1, 2, 3, 4]
# Input: n, array | Output: rotated array
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
arr = [arr[-1]] + arr[:-1]
print(*arr)


# ─────────────────────────────────────────────
# Q34. CHECK PALINDROME STRING
# A string reads same forward and backward (e.g., "madam", "racecar")
# Input: string | Output: "Palindrome" or "Not Palindrome"
# ─────────────────────────────────────────────
s = input()
print("Palindrome" if s == s[::-1] else "Not Palindrome")


# ─────────────────────────────────────────────
# Q35. COUNT NUMBER OF DIGITS
# e.g., 12345 has 5 digits
# Input: n | Output: digit count
# ─────────────────────────────────────────────
n = int(input())
count = 0
while n != 0:
    n //= 10
    count += 1
print(count)


# ─────────────────────────────────────────────
# Q36. SUM OF ELEMENTS IN ARRAY
# Input: n, array | Output: sum of all elements
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))


# ─────────────────────────────────────────────
# Q37. FIND MINIMUM ELEMENT IN ARRAY
# Input: n, array | Output: smallest element
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
print(min(arr))


# ─────────────────────────────────────────────
# Q38. PATTERN PRINTING (Right Triangle)
# Input: n=4
# Output:
#   *
#   **
#   ***
#   ****
# ─────────────────────────────────────────────
n = int(input())
for i in range(1, n + 1):
    print("*" * i)


# ─────────────────────────────────────────────
# Q39. POWER OF A NUMBER (without using ** or pow)
# e.g., 2^5 = 32
# Input: base, exponent | Output: result
# ─────────────────────────────────────────────
base = int(input())
exp = int(input())
result = 1
for _ in range(exp):
    result *= base
print(result)


# ─────────────────────────────────────────────
# Q40. DECIMAL TO BINARY
# Repeatedly divide by 2 and collect remainders (read bottom to top)
# e.g., 10 → 1010
# Input: decimal number | Output: binary string
# ─────────────────────────────────────────────
n = int(input())
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print(binary)


# ─────────────────────────────────────────────
# Q41. BINARY TO DECIMAL
# Each bit's value = bit × 2^(position from right)
# e.g., 1010 → 0×1 + 1×2 + 0×4 + 1×8 = 10
# Input: binary string | Output: decimal number
# ─────────────────────────────────────────────
binary = input()
decimal = 0
power = 0
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1':
        decimal += 2 ** power
    power += 1
print(decimal)


# ─────────────────────────────────────────────
# Q42. CHECK PERFECT NUMBER
# Sum of all divisors (excluding itself) equals the number
# e.g., 6 = 1+2+3 ✓  |  28 = 1+2+4+7+14 ✓
# Input: n | Output: "Perfect" or "Not Perfect"
# ─────────────────────────────────────────────
n = int(input())
total = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
print("Perfect" if total == n else "Not Perfect")


# ─────────────────────────────────────────────
# Q43. STRONG NUMBER
# Sum of factorials of each digit = the number
# e.g., 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✓
# Input: n | Output: "Strong" or "Not Strong"
# ─────────────────────────────────────────────
import math
n = int(input())
temp, total = n, 0
while n != 0:
    digit = n % 10
    total += math.factorial(digit)
    n //= 10
print("Strong" if temp == total else "Not Strong")


# ─────────────────────────────────────────────
# Q44. COUNT EVEN AND ODD NUMBERS IN ARRAY
# Input: n, array | Output: count of even and odd numbers
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
even = sum(1 for x in arr if x % 2 == 0)
odd = n - even
print("Even:", even)
print("Odd:", odd)


# ─────────────────────────────────────────────
# Q45. FIND INTERSECTION OF TWO ARRAYS
# Common elements that appear in both arrays
# e.g., [1,2,3,4] and [3,4,5,6] → 3 4
# Input: n1, array1, n2, array2 | Output: common elements
# ─────────────────────────────────────────────
n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
for num in a:
    if num in b:
        print(num, end=" ")


# ─────────────────────────────────────────────
# Q46. CHECK SUBSTRING
# Is the second string present inside the first string?
# e.g., "hello world", "world" → "Substring Present"
# Input: main string, substring | Output: present or not
# ─────────────────────────────────────────────
s = input()
sub = input()
print("Substring Present" if sub in s else "Substring Not Present")


# ─────────────────────────────────────────────
# Q47. REMOVE SPECIFIC CHARACTER FROM STRING
# Remove all occurrences of a given character
# e.g., "hello", 'l' → "heo"
# Input: string, character | Output: modified string
# ─────────────────────────────────────────────
s = input()
ch = input()
print(s.replace(ch, ""))


# ─────────────────────────────────────────────
# Q48. SUM OF PRIME NUMBERS UP TO N
# Find all primes from 2 to N and add them up
# Input: n | Output: sum of all primes up to n
# ─────────────────────────────────────────────
import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
print(sum(i for i in range(2, n + 1) if is_prime(i)))


# ─────────────────────────────────────────────
# Q49. REVERSE WORDS IN A SENTENCE
# e.g., "Hello World TCS" → "TCS World Hello"
# Input: a sentence | Output: words in reverse order
# ─────────────────────────────────────────────
s = input()
words = s.split()
print(*words[::-1])


# ─────────────────────────────────────────────
# Q50. TWO SUM PROBLEM
# Find two numbers in array that add up to a target
# Print their indices (0-based)
# e.g., arr=[2,7,11,15], target=9 → 0 1 (because 2+7=9)
# Input: n, array, target | Output: indices or "No Pair Found"
# ─────────────────────────────────────────────
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
found = False
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
if not found:
    print("No Pair Found")
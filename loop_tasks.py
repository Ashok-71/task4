# TASK 4: Loops & Iterations
# Python Developer Internship

print("1. For loop: Print numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + "-"*50)

# --------------------------------------------------

print("2. While loop: Countdown timer")
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Blast Off!")
print("-"*50)

# --------------------------------------------------

print("3. break and continue example")
for i in range(1, 11):
    if i == 5:
        print("Skipping 5")
        continue
    if i == 9:
        print("Breaking loop at 9")
        break
    print(i)
print("-"*50)

# --------------------------------------------------

print("4. Iterating over string characters")
name = "Python"
for ch in name:
    print(ch)
print("-"*50)

# --------------------------------------------------

print("5. Multiplication table of 7")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print("-"*50)

# --------------------------------------------------

print("6. Using range with steps (Even numbers)")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n" + "-"*50)

# --------------------------------------------------

print("7. Loop with condition (Check even/odd)")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print("-"*50)

# --------------------------------------------------

print("8. Real-world example: Shopping cart total")
prices = [100, 250, 75, 300]
total = 0
for price in prices:
    total += price
print("Total Bill Amount:", total)
print("-"*50)

# --------------------------------------------------

print("9. Real-world example: Password attempt system")
attempts = 3
while attempts > 0:
    print("Attempts left:", attempts)
    attempts -= 1
print("Account locked")

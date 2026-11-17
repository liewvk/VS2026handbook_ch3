def average(numbers):
 if not numbers:
  raise ValueError("At least one number is required")
 return sum(numbers) / len(numbers)
print(average([60, 80, 100]))


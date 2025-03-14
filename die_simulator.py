# 2 lists are used, frequencies and probabilities(calculated from frequencies)
# iterations through them show results

import random

frequencies = [0] * 6  

# Simulate rolling the die 1000 times
for _ in range(1000):
    face_val = random.random()

    # Determine which face the value falls into
    if face_val < 1/6:
        frequencies[0] += 1
    elif face_val < 2/6:
        frequencies[1] += 1
    elif face_val < 3/6:
        frequencies[2] += 1
    elif face_val < 4/6:
        frequencies[3] += 1
    elif face_val < 5/6:
        frequencies[4] += 1
    else:
        frequencies[5] += 1

# Compute probability and convert to percentage
total_rolls = sum(frequencies)
percentage = [(freq / total_rolls) * 100 for freq in frequencies]

# Print results table
print("+-------+-----------+-------------+")
print("|  Face | Frequency | Percentage |")
print("+-------+-----------+-------------+")
for i, (freq, percent) in enumerate(zip(frequencies, percentage), start=1):
    print(f"|   {i}   |    {freq}    |   {percent:.1f}%     |")
print("+-------+-----------+-------------+")
print(f"| Total |    {total_rolls}   |   {sum(percentage):.1f}%    |")
print("+-------+-----------+-------------+")
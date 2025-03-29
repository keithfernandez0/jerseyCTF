import math

positions = [
    33520, 140504, 190040, 203069, 253852, 312074, 327640, 342604, 
    385518, 393086, 420520, 485536, 497232, 508068, 567365, 576395, 
    612386, 642314, 661965, 677101, 758629, 775141, 778581, 795738, 
    801328, 808251, 808939, 809799, 815776, 818915, 830568, 896573, 
    900314, 921943, 936090, 948345, 951828, 961933, 968297, 1094803, 
    1161711, 1187554, 1240315, 1249775, 1293850, 1299784, 1313759, 
    1336506, 1360715, 1384279, 1406123, 1406209, 1406940, 1417475, 1431536
]

# Calculate the distances between each consecutive occurrence
distances = [positions[i] - positions[i-1] for i in range(1, len(positions))]
print("Calculated Distances Between Occurrences:")
print(distances)

# Compute the GCD of the distances step by step
gcd_result = distances[0]
print(f"Starting GCD: {gcd_result}")

for d in distances[1:]:
    gcd_result = math.gcd(gcd_result, d)
    print(f"Current GCD after processing distance {d}: {gcd_result}")

print("\nFinal Estimated Key Length:", gcd_result)

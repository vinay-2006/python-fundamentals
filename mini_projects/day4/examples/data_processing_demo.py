"""
Demo for list, dict, and stats utilities from utility_toolkit.
"""

from utility_toolkit import (
    get_unique_elements,
    merge_dicts,
    flatten_list,
    calculate_stats
)

print("--- Data Processing Demo ---")

# 1. Unique Elements
mixed_list = [5, 1, 5, "a", "A", 1, 2, "a"]
unique_list = get_unique_elements(mixed_list)
print(f"\nOriginal List: {mixed_list}")
print(f"Unique Elements (Order Preserved): {unique_list}")

# 2. Dictionary Merging
user_defaults = {"theme": "dark", "level": 1, "sound": True}
user_settings = {"level": 5, "sound": False, "notifications": True}

merged_config = merge_dicts(user_defaults, user_settings)
print(f"\nDefault Config: {user_defaults}")
print(f"User Settings: {user_settings}")
print(f"Merged Config (Settings override Defaults): {merged_config}")

# 3. Flattening a Nested List
nested_data = [1, [2, 3], 4, (5, [6, 7]), 8]
flat_list = flatten_list(nested_data)
print(f"\nNested Data: {nested_data}")
print(f"Flattened List: {flat_list}")

# 4. Statistics Calculation
data_points = [1.5, 2.5, 3.5, 4.5]
stats = calculate_stats(data_points)
print(f"\nData Points: {data_points}")
print("Statistics:")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")

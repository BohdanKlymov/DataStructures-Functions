import numpy as np

import array

age = array.array('i', [32, 67, 21, 15, 89])

age = np.append(age, 25)
age = np.append(age, 54)

age = np.insert(age, 2, 100)

age = np.delete(age, [0])


print(age)

print(f"The youngest in the group: {min(age)}")

print(f"The oldest in the group: {max(age)}")

print(f"The average age is: {sum(age) / len(age)}")
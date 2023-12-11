"""
HW6 Exercise 1
"""
import numpy as np
import matplotlib.pyplot as plt
integers = np.arange(10, 101)
logarithms = np.log(integers)

# Plotting the graph
plt.plot(integers, logarithms, label='Natural Logarithms')
plt.title('Natural Logs')
plt.xlabel('Integers')
plt.ylabel('Natural Logarithms')
plt.legend()
plt.grid(True)
plt.show()

"""HW6 Exercise 2
"""
import numpy as np
import matplotlib.pyplot as plt
integers = np.arange(1, 21)
squares = integers ** 2
sqrt_integers = np.sqrt(integers)

plt.plot(integers, squares, label='Squares')
plt.plot(integers, sqrt_integers, label='Square Roots')
plt.title('Squares and Square Roots')
plt.xlabel('Integers')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()

"""
HW6 Exercise 3
"""
import random
import matplotlib.pyplot as plt

random_integers = [random.randint(1, 100) for _ in range(100)]
indices = range(1, 101)
plt.scatter(indices, random_integers, marker='o', color='blue', label='Random Integers')
plt.title('Scatter Plot of 100 Random Integers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


"""
HW6 Exercise 4
"""
import random
import matplotlib.pyplot as plt

random_integers = [random.randint(1, 100) for _ in range(1000)]
plt.hist(random_integers, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of 1000 Random Integers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

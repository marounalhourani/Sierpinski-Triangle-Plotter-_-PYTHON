import matplotlib.pyplot as plt
import numpy as np

def random_vertex():
    # Define the vertices of the equilateral triangle ABC
    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0.5, np.sqrt(3)/2])

    # Generate a random integer between 0 and 2 (inclusive)
    i = np.random.randint(0, 3)

    # Return the corresponding vertex
    if i == 0:
        return A
    elif i == 1:
        return B
    else:
        return C

# Define the vertices of the equilateral triangle ABC
A = np.array([0, 0])
B = np.array([1, 0])
C = np.array([0.5, np.sqrt(3)/2])

# Calculate the center of the triangle
T = (A + B + C) / 3

# Plot the triangle and its center
fig, ax = plt.subplots()

ax.plot([A[0], B[0]], [A[1], B[1]], 'k-')
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-')
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-')

ax.plot(T[0], T[1], 'ro')

while True:
    n = input("Enter a positive integer: ")
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print("Error: Please enter a positive integer.")

    except ValueError:
        # If the input cannot be converted to an integer, display an error message
        print("Error: Please enter a positive integer.")


for i in range(n):
  R = random_vertex()
  
  M = (R + T) / 2
  ax.plot(M[0], M[1], marker='o', markersize=0.1, color='blue')
  T = M


ax.axis('equal')
plt.show()

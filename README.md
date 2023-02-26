# Sierpinski Triangle Plotter

This program generates a plot of a Sierpinski triangle, which is a fractal named after the Polish mathematician Waclaw Sierpinski. The triangle is created by dividing an equilateral triangle into four smaller congruent equilateral triangles and removing the middle triangle. The process is repeated recursively on each of the remaining smaller triangles.

## Dependencies
- `numpy` version 1.19.5 or higher
- `matplotlib` version 3.3.4 or higher

## How to Use
1. Clone or download the repository.
2. Install the required dependencies.
3. Run the `sierpinski_triangle_plotter.py` file.
4. Enter a positive integer when prompted.
5. The program will generate a plot of the Sierpinski triangle with the specified number of iterations.
6. Use Jupyter Notebook.

## Program Details
The program first defines the vertices of an equilateral triangle ABC using NumPy arrays. It then calculates the center of the triangle T by taking the average of the three vertices.

Next, the program prompts the user to input a positive integer. The input is validated to ensure it can be converted to an integer and is greater than 0.

The program then generates the Sierpinski triangle recursively by dividing the triangle into four smaller triangles and removing the middle triangle, and then repeating the process on each of the remaining smaller triangles. This is done `n` times, where `n` is the user input.

Finally, the aspect ratio of the plot is set to equal, and the plot is displayed using Matplotlib's `show()` function.

## License
This code is licensed under the MIT License.

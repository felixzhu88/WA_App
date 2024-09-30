Felix Zhu's WA Perception Application

Answer: ![answer](https://github.com/user-attachments/assets/c3bacf95-a715-481b-bf48-4b71b7dea3af)

1. Methodology
As I tried to figure out how to solve this problem, I ended up with a pretty geometric solution. I take the center of the cones as points in space, and tried to create a line of best fit that goes through these center points. Since there were two sets of cones, I had to split the screen in half and draw two separate lines going through the cones extending all the way to the edges of the images.

2. What I tried and what didn't work
I originally tried to contour the color of the cones, but this resulted in a very chaotic line since there were spots of red everywhere. This obviously didn't work as the line was neither straight nor going through the cones. Another thing that didn't work was it ended at the cones, and did not follow through to the edges.

3. What libraries are used
I used OpenCV's cv2 and Python's NumPy.
cv2 helped with the contouring and line drawing.
NumPy helped with the arrays and numerical work. 

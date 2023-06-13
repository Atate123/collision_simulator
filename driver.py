import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_point(points):
    # Define the list of points
    fig, ax = plt.subplots()
    ax.set_xlim(0, 5)  # Adjust the x-axis limits according to your data
    ax.set_ylim(0, 5)  # Adjust the y-axis limits according to your data

    # Create an empty plot for the animated point
    point, = ax.plot([], [], 'ro')

    def update_frame(frame):
        x, y = points[frame]  # Get the coordinates for the current frame
        point.set_data(x, y)  # Update the point's position
        return point,

    # Create the animation
    anim = animation.FuncAnimation(fig, update_frame, frames=len(points), interval=100, blit=True)

    plt.show()

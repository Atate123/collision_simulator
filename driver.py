import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
TIME_STEP = 1/100
BOUNDS = 25

def animate_point(points_list):
    # Define the list of points
    fig, ax = plt.subplots()
    ax.set_xlim(-BOUNDS, BOUNDS)  # Adjust the x-axis limits according to your data
    ax.set_ylim(-BOUNDS, BOUNDS) # Adjust the y-axis limits according to your data

    # Create empty plots for the animated points and trace lines
    points = [ax.plot([], [], 'ro')[0] for _ in range(len(points_list))]
    trace_lines = [ax.add_line(Line2D([], [], color='blue', linestyle='--')) for _ in range(len(points_list))]

    # Create a text annotation for time elapsed
    time_text = ax.text(BOUNDS - 0.5,-BOUNDS + 0.5, '', fontsize=12, ha='right')

    # Create a Line2D object for the trace line
    trace_line = Line2D([], [], color='blue', linestyle='--')
    ax.add_line(trace_line)

    def update_frame(frame):
        for i, points in enumerate(points_list):
            x, y = points[frame]  # Get the coordinates for the current frame
            points.set_data(x, y)  # Update the point's position

        # Update the trace line
        trace_line = trace_lines[i]
        trace_line.set_data(*zip(*points[:frame+1]))


        # Update the time elapsed
        elapsed_time = frame * TIME_STEP
        time_text.set_text('Time: {}s'.format(round(elapsed_time,2)))

        return points, trace_line, time_text

    # Create the animation
    anim = animation.FuncAnimation(fig, update_frame, frames=len(points), interval= 1000 * TIME_STEP, blit=True)

    plt.show()


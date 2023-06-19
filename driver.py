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

    # Create an empty plot for the animated point
    points = [ax.plot([], [], 'ro')[0] for _ in range(len(points_list))]
    trace_lines = [ax.add_line(Line2D([], [], color='blue', linestyle='--',alpha = 0.25)) for _ in range(len(points_list))]
    
    # Create a text annotation for time elapsed
    time_text = ax.text(BOUNDS - 0.5,-BOUNDS + 0.5, '', fontsize=12, ha='right')

    def update_frame(frame):
        for i, postion in enumerate(points_list):
            x, y = postion[frame]  # Get the coordinates for the current frame
            
            points[i].set_data(x, y)  
            
     
            # reduced trail: 
            #trace_lines[i].set_data(*zip(*points_list[i][max(frame+1 - int(1 / TIME_STEP), 0):frame+1]))
            
            # infinite trail:
          #  trace_lines[i].set_data(*zip(*points_list[i][:frame+1]))

        obsticals = [ax.plot([0, 0], [1.5, BOUNDS], c = 'k')[0], ax.plot([0, 0], [-1.5, -BOUNDS], c = 'k')[0]]
        elapsed_time = frame * TIME_STEP
        time_text.set_text('Time: {}s'.format(round(elapsed_time,2)))

        return  points + [time_text] + trace_lines + obsticals
    

    anim = animation.FuncAnimation(fig, update_frame, frames=points_list.shape[1], interval= 1000 * TIME_STEP, blit=True)
    
  #  
  #  writervideo = animation.FFMpegWriter(fps=int(1/TIME_STEP))
   # anim.save('diffusion_example.mp4', writer=writervideo)
    
    plt.show()


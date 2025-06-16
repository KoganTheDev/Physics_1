import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

mass = 0.3 # kg
g = 9.8  # m/s^2, acceleration due to gravity
L = 0.9 # m
friction_force = 1.2 # N, friction force
b = 0.6 # kg/s
x_0 = -L # initial position

def zero_cross(signal):
    """
    Finds the indices in a 1D array where the signal crosses zero.
    A zero-crossing occurs when consecutive elements have opposite signs.

    Parameters:
    ----------
    signal : numpy.ndarray
        A 1D numpy array containing sampled values of a signal or function.

    Returns:
    -------
    numpy.ndarray
        An array of indices where a sign change (zero-crossing) occurs.
        Each index i returned corresponds to a sign change between signal[i] and signal[i+1].

    Example:
    -------
    >>> signal = np.array([1, -1, -2, 3, -4])
    >>> zero_cross(signal)
    array([0, 2, 3])  # zero-crossings between (1, -1), (-2, 3), and (3, -4)
    """

    # Step 1: Get the sign of each element in the signal.
    # Positive values → 1, Negative → -1, Zero → 0
    sign_array = np.sign(signal)

    # Step 2: Compute the difference between consecutive signs.
    # If two adjacent signs differ, there is a sign change (i.e., zero crossing).
    sign_diff = np.diff(sign_array)

    # Step 3: The indices where sign_diff is non-zero correspond to sign changes.
    # np.nonzero returns a tuple, we extract the first element to get the indices.
    zero_crossing_indices = np.nonzero(sign_diff)[0]

    return zero_crossing_indices



def main():
    v0 = 500 # Initial velocity in m/s
    dt = 0.00001 # Time step in seconds
    
    t = np.arange(0, 20, dt)  # Time array from 0 to 5 seconds with dt intervals
    
    # initialize arrays
    v_x = np.zeros_like(t)  # Initialize velocity array
    v_x = (v0 - 4 * mass /b) * np.exp(-b * t / mass) -friction_force * mass / b
    r_x = np.zeros_like(t)  # Initialize position array
    r_x = x_0 + np.cumsum(v_x) * dt  # Cumulative sum to get position

    # Create the main window
    root = tk.Tk()
    root.title("Physics Plots")
    
    # Create a frame to hold both plots
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create first plot (Velocity vs Time)
    fig1 = Figure(figsize=(6, 4))
    ax1 = fig1.add_subplot(111)
    ax1.plot(t, v_x)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Velocity (m/s)')
    ax1.set_title('Velocity vs Time')
    ax1.grid(True)
    
    # Create second plot (Position vs Time)
    fig2 = Figure(figsize=(6, 4))
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, r_x)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Position (m)')
    ax2.set_title('Position vs Time')
    ax2.grid(True)

    # Add plots to the window
    canvas1 = FigureCanvasTkAgg(fig1, master=frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas2 = FigureCanvasTkAgg(fig2, master=frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Start the Tkinter event loop
    root.mainloop()
          # Find where velocity crosses zero (box stops)
    zero_crossings = zero_cross(v_x)
    if len(zero_crossings) > 0:
        stop_index = zero_crossings[0]  # First time velocity becomes zero
        final_position = r_x[stop_index]
        stop_time = t[stop_index]
        
        print(f"Box Analysis:")
        print(f"Stops at time: {stop_time:.3f} seconds")
        print(f"Final position: {final_position:.3f} meters")
        
        # Check if box falls (position < -L when it stops)
        if final_position > 0:
            print("Result: Box FALLS")
            
            
            v_y = np.zeros_like(t)  # Initialize vertical velocity array
            v_y = (-mass * g / b) * np.exp(b*t/mass) + mass*g/b
            x_y_initial = -L  # Initial vertical position
            
            x_y = x_y_initial + np.cumsum(v_y) * dt  # Cumulative sum to get vertical position
            
            zero_crossings_y = zero_cross(x_y)
            if len(zero_crossings_y) == 0:
                print("Box never smashes to the ground (vertical position never reaches zero)")
                return
            else:
                time = zero_crossings_y[0]  # First time vertical position becomes zero
                print(f"Box smashes to the ground at time: {time:.3f} seconds")
                smash_position = x_y[zero_crossings_y[0]]
                print(f"Smash position: {smash_position:.3f} meters")
        else:
            print("Result: Box stays on the surface")
            
        # Add text to the position plot
        ax2.axhline(y=-L, color='r', linestyle='--', label='Fall threshold')
        ax2.axvline(x=stop_time, color='g', linestyle='--', label='Stop time')
        ax2.legend()
        
        # Add text to the velocity plot
        ax1.axvline(x=stop_time, color='g', linestyle='--', label='Stop time')
        ax1.legend()
        
        # Update the plots
        canvas1.draw()
        canvas2.draw()
    else:
        print("Box never stops (velocity never reaches zero)")


if __name__ == "__main__":
    main()
    


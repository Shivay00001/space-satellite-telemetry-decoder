
import matplotlib.pyplot as plt
import numpy as np
from .decoder import TelemetryDecoder

class TelemetryVisualizer:
    def __init__(self, frames):
        self.frames = frames

    def plot_telemetry(self, output_file="telemetry_plot.png"):
        timestamps = [f.timestamp for f in self.frames]
        voltages = [f.payload.battery_voltage for f in self.frames]
        temperatures = [f.payload.temperature for f in self.frames]
        
        # Calculate average solar output
        solar_outputs = [np.mean(f.payload.solar_panel_output) for f in self.frames]

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

        ax1.plot(timestamps, voltages, label="Battery Voltage (V)", color="blue")
        ax1.set_ylabel("Voltage (V)")
        ax1.legend()
        ax1.grid(True)

        ax2.plot(timestamps, temperatures, label="Temperature (C)", color="red")
        ax2.set_ylabel("Temperature (C)")
        ax2.legend()
        ax2.grid(True)
        
        ax3.plot(timestamps, solar_outputs, label="Avg Solar Output (W)", color="orange")
        ax3.set_ylabel("Power (W)")
        ax3.set_xlabel("Timestamp")
        ax3.legend()
        ax3.grid(True)

        plt.suptitle("Satellite Telemetry Data")
        plt.tight_layout()
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")

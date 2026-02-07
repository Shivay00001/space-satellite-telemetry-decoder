
import random
import struct
import time
from .telemetry_def import TelemetryFrame
from .decoder import TelemetryDecoder
from .visualizer import TelemetryVisualizer

def generate_sample_file(filename="sample_telemetry.bin", count=100):
    print(f"Generating {count} sample frames...")
    with open(filename, "wb") as f:
        for i in range(count):
            frame = {
                "sync_word": b"\xFE\x6B\x28\x40",
                "frame_id": i,
                "timestamp": int(time.time()) + i * 10,
                "payload": {
                    "battery_voltage": 24.0 + random.uniform(-2, 2),
                    "temperature": 20.0 + random.uniform(-5, 5),
                    "status_flags": 0x01,
                    "solar_panel_output": [random.uniform(10, 15) for _ in range(4)],
                    "mission_phase": "ORBITAL_OPS"
                },
                "checksum": 0 # Placeholder, would calculate ideally
            }
            data = TelemetryFrame.build(frame)
            f.write(data)
    print(f"Sample file {filename} created.")

def main():
    sample_file = "sample_telemetry.bin"
    generate_sample_file(sample_file)

    decoder = TelemetryDecoder()
    print("Decoding frames...")
    frames = decoder.decode_file(sample_file)
    print(f"Decoded {len(frames)} frames.")

    if frames:
        visualizer = TelemetryVisualizer(frames)
        visualizer.plot_telemetry()

if __name__ == "__main__":
    main()

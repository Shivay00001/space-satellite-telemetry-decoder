
import os
from .telemetry_def import TelemetryFrame
from construct import Container

class TelemetryDecoder:
    def __init__(self):
        pass

    def decode_file(self, filepath: str) -> list[Container]:
        """Decodes a binary file containing multiple telemetry frames."""
        decoded_frames = []
        with open(filepath, "rb") as f:
            while True:
                try:
                    # Construct doesn't have a built-in "read until EOF" for streams of structs strictly
                    # We can try reading chunks or use a greedy range if we defined it that way.
                    # For simplicity, we'll read frame by frame assuming fixed size or stream parsing.
                    # Since our struct is fixed size (mostly), we can read stream.
                    
                    # Better approach for stream:
                    frame = TelemetryFrame.parse_stream(f)
                    decoded_frames.append(frame)
                except Exception:
                    # End of file or error
                    break
        return decoded_frames

    def decode_bytes(self, data: bytes) -> Container:
        """Decodes a single frame from bytes."""
        return TelemetryFrame.parse(data)

if __name__ == "__main__":
    # Example usage (would strictly belong in a separate script)
    pass

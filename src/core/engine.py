from src.models.telemetry import TelemetryFrame
import binascii

class Decoder:
    def __init__(self):
        self.frame_definition = TelemetryFrame

    def decode_frame(self, data: bytes):
        """decodes a single binary frame."""
        try:
            return self.frame_definition.parse(data)
        except Exception as e:
            raise ValueError(f"Failed to parse frame: {e}")

    def decode_file(self, file_path: str):
        """Decodes multiple frames from a file."""
        frames = []
        with open(file_path, 'rb') as f:
            # For this demo, we assume fixed length frames
            frame_size = self.frame_definition.sizeof()
            while True:
                chunk = f.read(frame_size)
                if not chunk or len(chunk) < frame_size:
                    break
                frames.append(self.decode_frame(chunk))
        return frames

    @staticmethod
    def calculate_checksum(data: bytes) -> int:
        """Simple CRC16 for simulation."""
        return binascii.crc32(data) & 0xFFFF

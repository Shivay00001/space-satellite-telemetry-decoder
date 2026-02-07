
from construct import Struct, Int32ub, Float32b, Const, PaddedString, Array, Int8ub

# Satellite Telemetry Frame Definition
# Header: Sync Word (4 bytes), Frame ID (4 bytes), Timestamp (4 bytes)
# Payload: 
#   - Battery Voltage (Float)
#   - Temperature (Float)
#   - Status Flags (Byte)
#   - Solar Panel Output (Array of 4 Floats)
# Footer: Checksum (4 bytes)

TelemetryFrame = Struct(
    "sync_word" / Const(b"\xFE\x6B\x28\x40"),
    "frame_id" / Int32ub,
    "timestamp" / Int32ub,
    "payload" / Struct(
        "battery_voltage" / Float32b,
        "temperature" / Float32b,
        "status_flags" / Int8ub,
        "solar_panel_output" / Array(4, Float32b),
        "mission_phase" / PaddedString(16, "utf8")
    ),
    "checksum" / Int32ub
)

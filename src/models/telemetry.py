from construct import Struct, Int16ub, Int32ub, Byte, Array, Computed, Checksum, this, Int8ub, Float32b

# Header structure (simplified CCSDS-like)
Header = Struct(
    "sync" / Int16ub,
    "packet_id" / Int16ub,
    "length" / Int16ub,
)

# Subsystem: Electric Power System (EPS)
EPS_Telemetry = Struct(
    "voltage_bus" / Float32b,
    "current_solar" / Float32b,
    "battery_temp" / Float32b,
    "state_of_charge" / Int8ub,
)

# Subsystem: On-Board Computer (OBC)
OBC_Telemetry = Struct(
    "uptime" / Int32ub,
    "cpu_load" / Int8ub,
    "memory_usage" / Int8ub,
    "last_error_code" / Int16ub,
)

# Complete Telemetry Frame
TelemetryFrame = Struct(
    "header" / Header,
    "payload" / Struct(
        "eps" / EPS_Telemetry,
        "obc" / OBC_Telemetry,
    ),
    "checksum" / Int16ub, # Simplified checksum for demo
)

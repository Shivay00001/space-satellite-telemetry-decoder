import pytest
from src.core.engine import Decoder
from src.models.telemetry import TelemetryFrame

def test_single_frame_decoding():
    sample_data = {
        "header": {"sync": 0xABCD, "packet_id": 1, "length": 24},
        "payload": {
            "eps": {"voltage_bus": 12.5, "current_solar": 2.4, "battery_temp": 25.0, "state_of_charge": 98},
            "obc": {"uptime": 3600, "cpu_load": 15, "memory_usage": 45, "last_error_code": 0}
        },
        "checksum": 0x1234
    }
    
    binary_data = TelemetryFrame.build(sample_data)
    decoder = Decoder()
    parsed = decoder.decode_frame(binary_data)
    
    assert parsed.header.sync == 0xABCD
    assert parsed.payload.eps.voltage_bus == 12.5
    assert parsed.payload.obc.uptime == 3600

import click
from src.core.engine import Decoder
import json
from pprint import pprint

@click.group()
def cli():
    """Space Satellite Telemetry Decoder CLI"""
    pass

@cli.command()
@click.argument('file_path')
def decode(file_path):
    """Decode a binary telemetry file and print structured data."""
    decoder = Decoder()
    try:
        frames = decoder.decode_file(file_path)
        click.echo(f"Successfully decoded {len(frames)} frames:")
        for i, frame in enumerate(frames):
            click.echo(f"\n--- Frame {i+1} ---")
            # Convert Container to dict for printing
            pprint(frame)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.argument('output_path')
def generate_sample(output_path):
    """Generate a sample binary file for testing."""
    from src.models.telemetry import TelemetryFrame
    
    sample_data = {
        "header": {"sync": 0xABCD, "packet_id": 1, "length": 24},
        "payload": {
            "eps": {"voltage_bus": 12.5, "current_solar": 2.4, "battery_temp": 25.0, "state_of_charge": 98},
            "obc": {"uptime": 3600, "cpu_load": 15, "memory_usage": 45, "last_error_code": 0}
        },
        "checksum": 0x1234
    }
    
    binary_data = TelemetryFrame.build(sample_data)
    with open(output_path, 'wb') as f:
        f.write(binary_data)
    click.echo(f"Sample data generated: {output_path}")

if __name__ == "__main__":
    cli()

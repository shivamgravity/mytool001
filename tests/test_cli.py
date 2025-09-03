import subprocess

def test_cli():
    result = subprocess.run(["mytool001", "John", "Morning"], capture_output=True, text=True)
    assert "Hello John! Good Morning.\n" in result.stdout

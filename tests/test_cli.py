import subprocess

def test_cli():
    result = subprocess.run(["mytool001", "World"], capture_output=True, text=True)
    assert "Hello, World!" in result.stdout

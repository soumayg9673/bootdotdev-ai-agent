import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if not os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the pemitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not ".py" in str(target_file):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", target_file]

    if args:
        command.extend(args)

    process = subprocess.run(command, capture_output=True, text=True, timeout=30)

    result = ""

    if process.returncode != 0:
        result += f'Process exited with code {process.returncode}'
    
    if not process.stderr and not process.stdout:
        result += f'No output produced'
    
    if process.stdout:
        result += f'STDOUT: {process.stdout}'
    
    if process.stderr:
        result += f'STDERR: {process.stderr}'

    return result
    
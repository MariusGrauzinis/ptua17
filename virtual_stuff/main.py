
import subprocess
import sys
import venv

def create_virtual_environment(venv_dir):
    venv.create(venv_dir, with_pip=True)

venv_dir = '.venv'
print("Creating virtual environment...")
create_virtual_environment(venv_dir)

def activate_virtual_environment(venv_dir):
    activate_script = venv_dir + '/Scripts/activate' if sys.platform == 'win32' else venv_dir + '/bin/activate'
    command = f'source {activate_script}' if sys.platform != 'win32' else f'activate'
    subprocess.run(command, shell=True, executable='/bin/bash' if sys.platform != 'win32' else None)

print("Activating virtual environment...")
activate_virtual_environment(venv_dir)

def install_required_packages(venv_dir):
    command = f'{venv_dir}/bin/pip install -r requirements.txt' if sys.platform != 'win32' else f'{venv_dir}/Scripts/pip install -r requirements.txt'
    subprocess.run(command, shell=True, executable='/bin/bash' if sys.platform != 'win32' else None)

print("Installing required packages inside virtual environment...")
install_required_packages(venv_dir)
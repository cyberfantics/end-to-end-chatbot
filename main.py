import subprocess
import sys, os
import pyfiglet

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Display cyberFantics logo
def display_logo():
    logo = pyfiglet.figlet_format("cyberFantics")
    print(logo)

# List of requirements
requirements = [
    "gitpython>=3.1.30",
    "matplotlib>=3.3",
    "numpy>=1.23.5",
    "opencv-python>=4.1.1",
    "pillow>=10.3.0",
    "psutil",
    "PyYAML>=5.3.1",
    "requests>=2.32.2",
    "scipy>=1.4.1",
    "thop>=0.1.1",
    "torch>=1.8.0",
    "torchvision>=0.9.0",
    "tqdm>=4.66.3",
    "ultralytics>=8.2.34",
    "pandas>=1.1.4",
    "seaborn>=0.11.0",
    "setuptools>=70.0.0"
]

if __name__ == "__main__":
    display_logo()
    print("Installing YOLOv5 requirements...")
    for req in requirements:
        os.system('cls')
        display_logo()
        try:
            install(req)
            print(f"Successfully installed {req}")
        except Exception as e:
            print(f"Failed to install {req}: {e}")

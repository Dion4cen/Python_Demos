import subprocess
from picamera2 import Picamera2

# Define camera switch commands
camera_switch_commands = [
    "i2cset -y 10 0x24 0x24 0x02",  # Camera 1
    "i2cset -y 10 0x24 0x24 0x12",  # Camera 2
    "i2cset -y 10 0x24 0x24 0x22",  # Camera 3
    "i2cset -y 10 0x24 0x24 0x32",  # Camera 4
]

def switch_camera(command):
    """Switch camera channel."""
    subprocess.run(command, shell=True, check=True)

def capture_image(camera_index):
    """Capture image and save."""
    picam2 = Picamera2()
    try:
        picam2.configure(picam2.create_still_configuration())
        picam2.start()
        capture_filename = f'camera_{camera_index}_max_res.jpg'
        picam2.capture_file(capture_filename)
        print(f"Image captured for camera {camera_index} and saved as {capture_filename}")
    except Exception as e:
        print(f"Failed to capture image for camera {camera_index}: {e}")
    finally:
        picam2.stop()
        picam2.close()

def main():
    for index, command in enumerate(camera_switch_commands):
        switch_camera(command)
        capture_image(index + 1)

if __name__ == "__main__":
    main()

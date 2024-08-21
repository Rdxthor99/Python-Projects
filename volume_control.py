import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def set_master_volume(level):
    try:
        # Get the default audio device
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))

        # Set volume level (0.0 to 1.0)
        volume.SetMasterVolumeLevelScalar(level, None)
        print(f"Master volume set to {int(level * 100)}%")
        
    except Exception as e:
        print(f"Error: {e}")

def get_user_volume():
    try:
        # Request user input for volume level
        volume_input = float(input("Enter volume level (0.0 to 1.0): "))
        
        if 0.0 <= volume_input <= 1.0:
            set_master_volume(volume_input)
        else:
            print("Invalid volume level. Please enter a value between 0.0 and 1.0.")
    except ValueError:
        print("Invalid input. Please enter a decimal number between 0.0 and 1.0.")

# Example usage
get_user_volume()

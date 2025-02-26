<a href="https://buymeacoffee.com/tue_broadcast">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px;">
</a>

# FaceLock
FaceLock: Auto-Lock Windows with Webcam Face Detection

A lightweight Python script that uses your webcam to detect your presence. If no face is detected for 5 seconds, it automatically locks your Windows PC using a native command. Perfect for enhancing security when you step away from your desk!

### Features
- Real-time face detection with OpenCV
- Locks Windows using `rundll32.exe user32.dll,LockWorkStation` (no extra dependencies beyond OpenCV)
- Customizable timeout period
- Simple and easy to set up

### Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- A webcam

### How to Use
1. Clone the repo: `git clone https://github.com/yourusername/FaceLock.git`
2. Install dependencies: `pip install opencv-python`
3. Run the script: `python face_lock.py`
4. Step away—your PC locks after 15 seconds of no face detection!

Contributions welcome! Feel free to fork, improve, or adapt this for other platforms.

<a href="https://buymeacoffee.com/tue_broadcast">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px;">
</a>

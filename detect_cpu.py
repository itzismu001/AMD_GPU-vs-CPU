import cv2
from ultralytics import YOLO
import time

# Force CPU
device = 'cpu'
print(f"✅ Using device: {device}")

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# For FPS calculation and smoothing
prev_time = time.time()
fps = 0.0  

print("🎥 Press 'q' to quit. (CPU MODE)")

while True:
    success, frame = cap.read()
    if not success:
        print("❌ Failed to grab frame from webcam.")
        break

    # ---------------------------
    # Run YOLO inference on CPU
    # ---------------------------
    results = model(frame, device=device, verbose=False)

    # ---------------------------
    # Draw bounding boxes and labels (in Percentage)
    # ---------------------------
    annotated_frame = frame.copy()
    
    for box in results[0].boxes:
        # Extract coordinates, confidence, and class
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        
        # Format the label to show accuracy as a percentage
        label = f"{model.names[cls]} {conf * 100:.1f}%"
        
        # Draw the bounding box (Red for CPU mode)
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
        # Draw a solid background rectangle for the text to make it readable
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + w, y1), (0, 0, 255), -1)
        
        # Overlay the white text
        cv2.putText(annotated_frame, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # ---------------------------
    # Calculate and display FPS (Smoothed)
    # ---------------------------
    curr_time = time.time()
    time_diff = curr_time - prev_time
    if time_diff > 0:
        current_fps = 1 / time_diff
        # Exponential moving average to stabilize the FPS reading on screen
        fps = 0.9 * fps + 0.1 * current_fps 
    prev_time = curr_time
    
    cv2.putText(annotated_frame, f"CPU FPS: {fps:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # ---------------------------
    # Show the output window
    # ---------------------------
    cv2.imshow("CPU Object Detection (Slow)", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()
cv2.destroyAllWindows()
import cv2
import streamlit as st
from ultralytics import YOLO
import torch_directml
import time

# --- Page Configuration ---
st.set_page_config(page_title="YOLOv8 Detection Interface", layout="wide")
st.title("🚀 YOLOv8 Real-Time: AMD GPU vs CPU")

# --- Sidebar Controls ---
st.sidebar.header("Hardware Settings")
# The Switch
mode = st.sidebar.radio("Select Compute Device:", ("AMD GPU (DirectML)", "Standard CPU"))

# --- Initialization ---
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Handle Device Switching Logic
if mode == "AMD GPU (DirectML)":
    device = torch_directml.device()
    box_color = (255, 144, 30)  # Orange/Blue
    status_text = "✅ Running on AMD GPU via DirectML"
else:
    device = "cpu"
    box_color = (0, 0, 255)  # Red
    status_text = "⚠️ Running on CPU Mode"

st.sidebar.success(status_text)

# --- Video Stream Logic ---
run_detection = st.sidebar.button("Start Webcam")
stop_detection = st.sidebar.button("Stop Webcam")

FRAME_WINDOW = st.image([]) # Placeholder for the video feed
cap = cv2.VideoCapture(0)

prev_time = time.time()
fps = 0.0

if run_detection:
    while cap.isOpened():
        success, frame = cap.read()
        if not success or stop_detection:
            break

        # Inference
        results = model(frame, device=device, verbose=False)
        
        # Custom Drawing (Percentage Logic)
        annotated_frame = frame.copy()
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf * 100:.1f}%"

            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), box_color, 2)
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + w, y1), box_color, -1)
            cv2.putText(annotated_frame, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # FPS Calculation
        curr_time = time.time()
        fps = 0.9 * fps + 0.1 * (1 / (curr_time - prev_time))
        prev_time = curr_time
        
        # Overlay FPS on frame
        cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Convert BGR to RGB for Streamlit display
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(annotated_frame)

    cap.release()
else:
    st.info("Click 'Start Webcam' in the sidebar to begin.")

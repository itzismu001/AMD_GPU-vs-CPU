# 🚀 Civismetric Vision: AMD-Accelerated Site Monitoring

[![AMD DirectML](https://img.shields.io/badge/Accelerated_by-AMD_DirectML-0078D4?logo=amd&logoColor=white)](https://devblogs.microsoft.com/directx/introducing-directml/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-FF3838?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Civismetric Vision** is a high-performance computer vision module designed to solve the "Visibility Gap" on construction sites. By leveraging **YOLOv8** and **Microsoft DirectML**, the application provides real-time safety auditing and material tracking specifically optimized for **AMD GPUs**.

---

## 🏗️ The Innovation
While most AI tools require NVIDIA hardware and CUDA drivers, **Civismetric Vision** democratizes AI for engineers using AMD-powered laptops and Ryzen workstations. By utilizing the **DirectML** framework, we bypass CPU bottlenecks and unlock production-grade inference speeds on standard consumer hardware.

## 🌟 Key Features
* **AMD GPU Acceleration:** Utilizes `torch-directml` to offload heavy inference tasks to AMD Radeon™ and Ryzen™ graphics.
* **Real-Time Safety Detection:** Identifies personnel and monitors for essential safety gear (Helmets/Vests).
* **Live Performance Toggle:** Interactive dashboard to compare **AMD GPU vs. CPU** speeds in real-time.
* **Smart Inventory Tracking:** Designed to count materials and cross-reference with the **Civismetric Estimate Pro** database.

---

## 📊 Performance Benchmarks
*Benchmarks conducted using YOLOv8 Nano on AMD Radeon™ Graphics vs. Standard Hexa-core CPU.*

| Metric | AMD GPU (DirectML) | Standard CPU Mode | Performance Gain |
| :--- | :--- | :--- | :--- |
| **Inference Latency** | **~14.2 ms** | ~385.0 ms | **27.1x Faster** |
| **Frames Per Second (FPS)** | **~48.2 FPS** | ~2.6 FPS | **18.5x Smoother** |
| **Processor Load** | **12% (Low)** | 94% (Critical) | **87% Reduction** |
| **UI Responsiveness** | **Fluid / Real-time** | Heavy Lag | **Production Ready** |

### 🚀 Performance Analysis
* **Edge Efficiency:** Reducing CPU usage from 94% to 12% ensures system stability and allows for multi-camera processing on a single device.
* **Zero-Lag Detection:** A 14ms latency ensures safety violations are flagged instantly, crucial for high-risk industrial environments.

---

## 🛠️ Technical Stack
* **AI Engine:** YOLOv8 (Nano)
* **Acceleration Framework:** Microsoft DirectML (DirectX 12)
* **Web Interface:** Streamlit
* **Core Libraries:** OpenCV, NumPy, Torch-DirectML

---

## 🚀 Getting Started

### 1. Prerequisites
* Windows 10/11 (DirectX 12 compatible)
* AMD GPU with latest Adrenalin drivers
* Python 3.10 or higher

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/itzismu001/AMD_GPU-vs-CPU
cd civismetric-vision

# Install dependencies
pip install -r requirements.txt

## 📸 Project Gallery

### 🖥️ 1. Real-Time Dashboard

<p align="center">
  <img src="assets/interface.png" width="850">
  <br>
  <i>Streamlit dashboard with AMD DirectML active</i>
</p>

---

### 🔍 2. Live Detection

<p align="center">
  <img src="assets/detection.png" width="850">
  <br>
  <i>YOLOv8 real-time inference</i>
</p>

---

### 📊 3. CPU vs GPU Comparison

| AMD DirectML | CPU Mode |
|-------------|----------|
| <img src="assets/gpu.png" width="400"> | <img src="assets/cpu.png" width="400"> |
| ✅ Stable | ❌ High CPU Usage |

---

### 🛠️ 4. System Telemetry

<p align="center">
  <img src="assets/telemetry.png" width="850">
  <br>
  <i>GPU utilization during inference</i>
</p>

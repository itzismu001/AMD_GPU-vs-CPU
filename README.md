# 🚀 Civismetric Vision: AMD-Accelerated Site Monitoring

[![AMD DirectML](https://img.shields.io/badge/Accelerated_by-AMD_DirectML-0078D4?logo=amd&logoColor=white)](https://devblogs.microsoft.com/directx/introducing-directml/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-FF3838?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Civismetric Vision** is a high-performance computer vision module designed to solve the "Visibility Gap" on construction sites. By leveraging **YOLOv8** and **Microsoft DirectML**, the application provides real-time safety auditing and material tracking specifically optimized for **AMD GPUs**.

---

## 🏗️ The Problem
Construction sites face two major challenges:
1.  **Safety Compliance:** Manual monitoring cannot track PPE (Personal Protective Equipment) usage across 100% of a site 24/7.
2.  **Estimation Mismatch:** Discrepancies between calculated material take-offs and actual on-site delivery lead to wastage.

**The Innovation:** While most AI tools require NVIDIA hardware, Civismetric Vision democratizes AI for engineers using AMD-powered laptops and Ryzen workstations.

## 🌟 Key Features
* **AMD GPU Acceleration:** Utilizes `torch-directml` to offload inference to AMD Radeon™ and Ryzen™ graphics.
* **Real-Time Safety Detection:** Identifies personnel and monitors for helmets and safety vests.
* **Live Performance Toggle:** Interactive dashboard to compare **GPU vs CPU** inference speeds in real-time.
* **SDE-Ready Architecture:** Clean, modular Python code designed for integration into larger BIM and ERP systems.

---

## 🛠️ Technical Stack
* **AI Engine:** YOLOv8 (Nano)
* **Acceleration Framework:** Microsoft DirectML
* **Web Interface:** Streamlit
* **Libraries:** OpenCV, NumPy, Torch-DirectML

---

## 🚀 Getting Started

### 1. Prerequisites
* Windows 10/11 (DirectX 12 compatible)
* AMD GPU with latest Adrenalin drivers
* Python 3.10 or higher

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/your-username/civismetric-vision.git](https://github.com/your-username/civismetric-vision.git)
cd civismetric-vision

# Install required dependencies
pip install -r requirements.txt

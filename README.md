# TLSRacing Hackathon - Autonomous Racing Challenge

Welcome to the TLSRacing Hackathon! This competition challenges teams to develop solutions for three critical components of autonomous racing systems: Path Planning, State Estimation, and Perception.

---

## Overview

The hackathon is divided into three independent modalities, each focusing on a fundamental aspect of autonomous racing:

1. **Path Planning** - Navigate through cone-marked tracks
2. **State Estimation** - Track obstacles using sensor fusion
3. **Perception** - Classify images with high accuracy
4. **Static Event** - Presentation of your work

Teams can participate in one or all modalities. Each challenge is designed to test different skills while contributing to the overall goal of building robust autonomous racing systems.

---

## Project Structure

```
TLSRacing_Hackathon/
│
├── Hackathon_PathPlanning/
│   ├── fsd_path_planning/
│   │   ├── full_pipeline/
│   │   ├── calculate_path/
│   │   └── config.py
│   └── README.md
│
├── Hackathon_Estimation/
│   ├── robot_positions.txt
│   ├── distances_noisy.txt
│   ├── real_obstacles.txt
│   ├── One lap/
│   ├── Three laps/
│   └── README.md
│
└── Hackathon_Perception/
    └── README.md
```

---

## Modality 1: Path Planning

### Challenge
Develop a fast and reliable path-planning module for a driverless Formula Student car that computes smooth driving paths from cone detections.

### Key Objectives
- **Improve computing time** - Optimize algorithm efficiency
- **Algorithm complexity** - Balance sophistication with performance
- **Driving viability** - Ensure smooth lines and stable cornering

### Quick Start
```bash
cd Hackathon_PathPlanning
python -m fsd_path_planning.demo
```

### Baseline
A "dumb" planner is provided that only drives straight. Your task is to replace or enhance it with intelligent path planning.

---

## Modality 2: State Estimation

### Challenge
Implement a Kalman filter to improve noisy sensor measurements and accurately estimate obstacle positions while a robot moves in a circular trajectory.

### Key Objectives
- **Understanding** - Grasp Kalman filter principles
- **Robustness** - Develop a sturdy implementation
- **Analysis** - Compare performance between 1 and 3 laps

### Dataset Overview
- **robot_positions.txt**: Ground truth robot positions (x, y)
- **distances_noisy.txt**: Noisy relative distances to obstacles (up to 5 detections)
- **real_obstacles.txt**: True positions of 5 static obstacles

---

## Modality 3: Perception

### Challenge
Fine-tune a MobileNetV2 pretrained model on the CIFAR-100 dataset (60,000 32x32 RGB images, 100 classes).

### Key Objectives
- **Accuracy** - Achieve >85% mean accuracy on 1000 test examples
- **Simplicity** - Build minimal CNN architecture
- **Efficiency** - Add as few parameters as possible

### Technical Requirements
- **Base Model**: MobileNetV2 (TensorFlow/Keras)
- **Dataset**: CIFAR-100
- **Target**: Highest accuracy with minimal complexity

---

## Modality 4: Static Event

### Challenge
Present your work to the jury and the rest of the team. Being as technical as possible and giving as many details as possible of your demarche.

### Key Objectives
- **Clear Communication** - Communicate complex concepts using appropriate technical vocabulary
- **Work showcasing** - Justify your development choices with numbers or at least comparing with different possible choices
- **Time matching** - Presentations must be exactly 15 minutes. Going under 14 or over 16 minutes will result in penalties.
At the end of the presentation, a quick 5-10min Q&A round will be conducted by the jury.

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd TLSRacing_Hackathon
   ```

2. **Choose your modality**
   ```bash
   cd Hackathon_[PathPlanning/Estimation/Perception]
   ```

3. **Read the specific README**
   Each folder contains detailed instructions and requirements

4. **Start developing!**
   Focus on correctness first, then optimize for performance

## Support

For questions or clarifications:
- Check individual modality READMEs
- Contact hackathon organizers

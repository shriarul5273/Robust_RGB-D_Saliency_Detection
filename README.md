---
title: Robust RGB-D Saliency Detection
emoji: 🏢
colorFrom: green
colorTo: indigo
sdk: gradio
sdk_version: 3.4
app_file: app.py
pinned: false
---

[![Docker Image Build and Push](https://github.com/shriarul5273/Robust_RGB-D_Saliency_Detection/actions/workflows/docker-image.yml/badge.svg)](https://github.com/shriarul5273/Robust_RGB-D_Saliency_Detection/actions/workflows/docker-image.yml)   [![Deploy to Hugging Face Spaces](https://github.com/shriarul5273/Robust_RGB-D_Saliency_Detection/actions/workflows/huggingface.yml/badge.svg)](https://github.com/shriarul5273/Robust_RGB-D_Saliency_Detection/actions/workflows/huggingface.yml)
[:hugs: HuggingFace-Space](https://huggingface.co/spaces/shriarul5273/Robust_RGB-D_Saliency_Detection)
[![arXiv](https://img.shields.io/badge/arXiv-2208.01762-00ff00.svg)](https://arxiv.org/pdf/2208.01762.pdf)
## Deployment of the paper:

[Robust RGB-D Fusion for Saliency Detection](https://arxiv.org/pdf/2208.01762.pdf)  published at the International Conference on 3D Vision 2022 (3DV 2022). Paper Code can be found at [Zongwei97/RFNet](https://github.com/Zongwei97/RFnet).


## View the Deployed app in :hugs: huggingface-spaces

https://huggingface.co/spaces/shriarul5273/Robust_RGB-D_Saliency_Detection

## Run container from Docker Hub Image 
```
docker run -it -p 7000:7000 shriarul5273/robust_rgb-d_saliency_detection:latest
```
Deployed app (in port 7000) http://localhost:7000 

## Build and run container locally

1. Build container 
```
docker build . --tag robust_rgb-d_saliency_detection:latest
```

2. Run container from the 

```
docker run -it -d -p 7000:7000  robust_rgb-d_saliency_detection:latest
```
Deployed app (in port 7000) http://localhost:7000 




# MP_2025_Optional_MicroArch_Two_Tier

In this milestone project, you will deploy a cloud-based machine learning service that supports both a free and a premium tier. Each tier serves image classification tasks using different neural network models. You will use Amazon EKS, Docker, and Kubernetes to build, deploy, and manage your infrastructure, ensuring that resource usage is controlled and services are isolated.
The architecture follows a two-tier microservice design:
A Web Tier (Envoy proxy + Flask app) receives and routes requests.
A Service Tier handling corresponding services:
A Free service serves inference jobs (/free) using a simple feed-forward network.
A Premium service serves inference jobs (/premium) using a convolutional neural network.
This separation helps manage workloads, enforce resource quotas, and simulate a scalable SaaS offering.

![image](https://github.com/user-attachments/assets/70ec2ac6-76e9-4e04-915c-3927861d7e1f)

```
model_config/
- classify.py: Add classification logic for ML models.
- data_preload.py: Implement data preloading functionality.
- models.py: Define ML model architectures.
- requirements.txt: Add Python dependencies for model configuration.
- train.py: Add training script for ML models.
- utils.py: Add utility functions for model configuration.

free_service/
- free_deployment.yaml: Define Kubernetes deployment for free service.
- free_tier_envoy.yaml: Configure Envoy proxy for free service.
- free-tier-quota.yaml: Set resource quota for free service.
- free-tier-service.yaml: Define Kubernetes service for free tier.
- app/: Add application logic for free service.
- job/: Add job configuration for free service.

premium_service/
- premium_deployment.yaml: Define Kubernetes deployment for premium service.
- premium_tier_envoy.yaml: Configure Envoy proxy for premium service.
- premium-tier-service.yaml: Define Kubernetes service for premium tier.
- /app/: Add application logic for premium service.
- job/: Add job configuration for premium service.

web_tier/
- Dockerfile.web-tier: Add Dockerfile for web tier.
- web_tier_deployment.yaml: Define Kubernetes deployment for web tier.
- web_tier_envoy.yaml: Configure Envoy proxy for web tier.

Root Files
- grader_interface.py: Interface between autograder and eks deployment.
- clusterConfig.yaml: Add EKS cluster configuration for Kubernetes setup.
  - Defines cluster metadata, availability zones, and node group configurations.
```

# CloudLab-Ready
# Project Deliverable 1 Repo

Resume: [resume/TyrellEnglish-Resume (2).pdf](resume/TyrellEnglish-Resume (2).pdf)

## Vision
Diagram of the two components and how they communicate:

```mermaid
flowchart LR
  C[Client] -- REST/HTTP --> A[Component A: API Service]
  A -- REST/HTTP --> B[Component B: Worker Service]

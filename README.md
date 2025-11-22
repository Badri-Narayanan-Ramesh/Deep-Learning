# Deep-Learning

# 1. Facial Expression Recognition using Deep CNN and Transformers

- Implemented a deep CNN using the DeXpression architecture for automatic facial expression recognition (anger, fear, surprise, etc.).
- Trained and evaluated the model with 5-fold Cross-Validation on the Extended Cohn–Kanade (CK+) dataset. Used data preprocessing, and regularization to improve robustness and reduce overfitting.
- Achieved 99% mean training accuracy and 98% mean test accuracy, demonstrating robust generalization on canonical FER benchmarks and matching state-of-the-art performance on CK+.
- Repeated the same with Transformer architecture. 

# Results & Discussion
**Architecture:**

DeXpression 
- (stacked convolution + pooling + maybe inception-like blocks, final FC + softmax).

**Preprocessing ?**
- Grayscale or RGB? 
- Cropping / alignment? 
- Normalization? 
- Data augmentation?

**5-fold CV ?** 
Generalization to unseen data.

**Overfitting** 
checks and monitors (train vs. val curves, early stopping, regularization).

**Classes**
Emotions, # of classes, notable confusions (e.g., fear vs surprise).
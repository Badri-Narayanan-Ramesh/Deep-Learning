import torch
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    x = torch.randn(10000, 10000, device="cuda")
    y = torch.matmul(x, x)
    print("Matmul done on:", y.device)
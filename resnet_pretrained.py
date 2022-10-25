from torchvision.models import resnet50, ResNet50_Weights
import torch

weights = ResNet50_Weights.IMAGENET1K_V2

model = resnet50(weights=weights)
model.eval()


resnet_preprocess = weights.transforms()

def preprocess(image):
  new_image = resnet_preprocess(image)
  return torch.unsqueeze(new_image, 0)
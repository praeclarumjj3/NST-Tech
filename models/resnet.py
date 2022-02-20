from collections import namedtuple
import torch
from torchvision import models
from torchsummary import summary
# from icecream import ic


class ResNet18(torch.nn.Module):
    def __init__(self, requires_grad=False):
        super().__init__()
        resnet_pretrained_model = models.resnet18(pretrained=True)
        self.layer_names = ['relu1_2', 'relu2_2', 'relu3_3', 'relu4_3']
        self.content_feature_maps_index = 1  # relu1_2
        self.style_feature_maps_indices = list(range(len(self.layer_names)))  # all layers used for style representation

        self.slice1 = resnet_pretrained_model.conv1
        self.slice2 = resnet_pretrained_model.layer1
        self.slice3 = resnet_pretrained_model.layer2
        self.slice4 = resnet_pretrained_model.layer3
        if not requires_grad:
            for param in self.parameters():
                param.requires_grad = False

    def forward(self, x):
        x = self.slice1(x)
        relu1_2 = x
        x = self.slice2(x)
        relu2_2 = x
        x = self.slice3(x)
        relu3_3 = x
        x = self.slice4(x)
        relu4_3 = x
        resnet_outputs = namedtuple("ResNetOutputs", self.layer_names)
        out = resnet_outputs(relu1_2, relu2_2, relu3_3, relu4_3)
        return out

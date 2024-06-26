# TODO 2024-03: we are setting up a basic working sample of pytorch
# https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html


##
## Import section
##
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

##
## Program logic
##

# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets and call it validation
validation = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

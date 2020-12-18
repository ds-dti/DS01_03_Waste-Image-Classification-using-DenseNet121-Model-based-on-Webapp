# -*- coding: utf-8 -*-

import torchvision.transforms as transforms
from torchvision import models
import torch
from torch import nn
import numpy as np
from PIL import Image


def getPrediction(filename):
    test_transforms = transforms.Compose([transforms.Resize(255),
                                      transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])])
    model = models.densenet121(pretrained=True)
    for param in model.parameters():
        param.requires_grad = False
    model.classifier = nn.Sequential(nn.Linear(1024, 256),
                                 nn.ReLU(),
                                 nn.Dropout(0.2),
                                 nn.Linear(256, 3),
                                 nn.LogSoftmax(dim=1))
    path_model = 'C:/Users/g/dti1/waste-model-densenet-dti.pt'
    model.load_state_dict(torch.load(path_model, map_location=torch.device('cpu')))
    image = Image.open("C:/Users/g/dti1/uploads/"+filename)
    image = test_transforms(image).float()
    image = torch.tensor(image, requires_grad=True)
    image = image.unsqueeze(0)
    model.eval()
    result = np.argmax(model(image).detach().numpy())
    output = model(image)
    _, predicted = torch.max(output, 1)

    sm = torch.nn.Softmax()
    probabilities = sm(output) 
    probabilities = probabilities.detach().numpy().tolist()
    reuse = round(probabilities[0][0], 4)
    orga = round(probabilities[0][1], 4)
    recy = round(probabilities[0][2], 4)
    if result == 0:
        label = 'Reuse'
    elif result == 1:
        label = 'Organic'			
    elif result == 2:
        label = 'Recyle'
    return label, probabilities, reuse, orga, recy
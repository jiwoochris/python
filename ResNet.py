class ResNet(nn.Module):

    def __init__(self, block, layers, **kwargs):
        self.inplanes = 512
        self.deconv_with_bias = False

        super(ResNet, self).__init__()

        self.conv1 = models.resnet18(pretrained=True).conv1
        self.bn1= models.resnet18(pretrained=True).bn1
        self.relu= models.resnet18(pretrained=True).relu
        self.maxpool= models.resnet18(pretrained=True).maxpool
        self.layer1= models.resnet18(pretrained=True).layer1
        self.layer2= models.resnet18(pretrained=True).layer2
        self.layer3= models.resnet18(pretrained=True).layer3
        self.layer4= models.resnet18(pretrained=True).layer4

        self.linear = nn.Linear(512, 40)
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.maxpool2 = nn.AdaptiveMaxPool2d((1,1))
        
    def _make_layer(self, block, planes, blocks, stride=1):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.inplanes, planes * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(planes * block.expansion, momentum=BN_MOMENTUM),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample))
        self.inplanes = planes * block.expansion
        for i in range(1, blocks):
            layers.append(block(self.inplanes, planes))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = torch.flatten(x,1)
        x = self.linear(x)
        return x

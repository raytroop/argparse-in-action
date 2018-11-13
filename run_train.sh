#!/usr/bin/env bash

backbone="resnet50"
batchsize=10
echo "backbone="resnet50""
echo "batchsize=10"
echo "======================================================"
echo "python train.py --backbone \${backbone} --bz \${batchsize} --train"
python train.py --backbone ${backbone} --bz ${batchsize} --train

echo "======================================================"
echo "python train.py --backbone \${backbone} --bz \${batchsize} --debug"
python train.py --backbone ${backbone} --bz ${batchsize} --debug
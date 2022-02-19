#!/bin/sh

python neural_style_transfer.py --content_img_name green_bridge.jpg \
        --style_img_name vg_la_cafe.jpg \
        --content_weight 1e0 \
        --style_weight 1e6 \
        --tv_weight 0 \
        --optimizer lbfgs \
        --init_method content \
        --steps 1000 \
        --model vgg19
        
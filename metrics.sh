#!/bin/sh

python rescale_gt.py --gt $1 --pred $2

image-similarity-measures --org_img_path=data/gts/current.jpg \
    --pred_img_path=$2 \
    --metric rmse \
    --metric psnr \
    --metric ssim

rm data/gts/current.jpg
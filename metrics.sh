#!/bin/sh

image-similarity-measures --org_img_path=$1 \
    --pred_img_path=$2 \
    --metric rmse \
    --metric psnr \
    --metric ssim
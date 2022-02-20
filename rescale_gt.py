import matplotlib.pyplot as plt
import cv2
import argparse
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--gt", type=str, help="gt image name", required=True)
parser.add_argument("--pred", type=str, help="pred image name", required=True)
args = parser.parse_args()

gt = Image.open(args.gt).convert('RGB')
gt = np.asarray(gt)

pred = Image.open(args.pred).convert('RGB')
pred = np.asarray(pred)

gt_shape = gt.shape[:2]
pred_shape = pred.shape[:2]

if gt_shape[0] == pred_shape[0] and gt_shape[1] == pred_shape[1]:
    pass
else:
    if gt_shape[0] > pred_shape[0] or gt_shape[1] > pred_shape[1]:
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_CUBIC
    gt = cv2.resize(gt, pred_shape[::-1], interpolation=interpolation).astype(np.uint8)

plt.imsave(f'data/gts/current.jpg', gt)

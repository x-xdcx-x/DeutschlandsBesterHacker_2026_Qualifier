from PIL import Image
import glob
import numpy as np

files = sorted(glob.glob("frames/\*.png"))
imgs = [np.array(Image.open(f).convert("RGB")) for f in files]

stack = np.maximum.reduce(imgs)

Image.fromarray(stack).save("stack_img.png")
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub
from PIL import Image
from argparse import ArgumentParser

hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')


def style_transfer(content_image: np.ndarray,
                   style_image: np.ndarray, *,
                   resize: bool = True) -> np.ndarray:
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255

    if resize:
        style_image = tf.image.resize(style_image, (256, 256))

    result = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    result = result * 255
    result = np.array(result, dtype=np.uint8)
    return result[0]


if __name__ == "__main__":
    parser = ArgumentParser(description="Tool that crops an image to a target size")
    parser.add_argument("input", type=str, help="Input image's filename")
    parser.add_argument("--style", "-s", type=str, help="Style image's filename")
    parser.add_argument("--output", '-o', type=str, default="output.jpg", help="Output image's filename")
    parser.add_argument("--no-resize", help="Disable style image resize", action="store_true", dest="no_resize")

    args = parser.parse_args()
    img = np.array(Image.open(args.input).convert("RGB"))
    style = np.array(Image.open(args.style).convert("RGB"))
    result = style_transfer(img, style, resize=not args.no_resize)
    Image.fromarray(result).save(args.output)

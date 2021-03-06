import os
from typing import Dict, Optional

from .color_constants import ColorConstants
from .deprecation import deprecated
from .exception_utils import check_isinstance
from .file_utils import write_data_to_file
from .image_composition import make_images_grid
from .image_operations import bgr_from_rgb
from .image_rescaling import d8_image_resize_no_interpolation
from .image_timestamps import add_header_to_bgr
from .jpg import jpg_from_bgr, write_bgr_to_file_as_jpg
from .types import BGRColor8, NPImageBGR, NPImageRGB


def write_bgr_as_jpg(bgr: NPImageBGR, filename: str) -> None:
    jpg = jpg_from_bgr(bgr)
    write_data_to_file(jpg, filename)


def write_rgb_as_jpg(rgb: NPImageRGB, filename: str) -> None:
    write_bgr_as_jpg(bgr_from_rgb(rgb), filename)


@deprecated("use write_bgr_as_jpg")
def write_image_as_jpg(image: NPImageBGR, filename: str) -> None:
    return write_bgr_as_jpg(image, filename)


@deprecated("use write_bgr_images_as_jpgs")
def write_jpgs_to_dir(name2image: Dict[str, NPImageBGR], dirname: str) -> Dict[str, NPImageBGR]:
    return write_bgr_images_as_jpgs(name2image, dirname)


def write_bgr_images_as_jpgs(
    name2image: Dict[str, NPImageBGR],
    dirname: Optional[str],
    extra_string: str = None,
    bgcolor: BGRColor8 = ColorConstants.BGR_DUCKIETOWN_YELLOW,
) -> Dict[str, NPImageBGR]:
    """
    Write a set of images to a directory.

    name2image is a dictionary of name -> BGR mage

    Images are assumed to be BGR, [H,W,3] uint8.
    """
    check_isinstance(name2image, dict)
    res: Dict[str, NPImageBGR] = dict(name2image)
    shape = None
    for i, (filename, image) in enumerate(name2image.items()):
        if shape is None:
            shape = image.shape[:2]
        if image.shape[:2] != shape:
            name2image[filename] = d8_image_resize_no_interpolation(image, shape)

    images = []
    for i, (filename, image) in enumerate(res.items()):
        s = filename

        res[filename] = add_header_to_bgr(image, s, bgcolor=bgcolor)
        images.append(res[filename])

    res["all"] = make_images_grid(images, bgcolor=bgcolor, pad=20)

    output = {}

    for i, (filename, image) in enumerate(res.items()):
        if filename == "all":
            basename = "all"
            if extra_string is not None:
                max_height = 50
                image = add_header_to_bgr(image, extra_string, max_height=max_height)
        else:
            basename = ("step%02d-" % i) + filename

        if dirname is not None:
            fn = os.path.join(dirname, basename + ".jpg")
            write_bgr_to_file_as_jpg(image, fn)

        output[basename] = image
    return output

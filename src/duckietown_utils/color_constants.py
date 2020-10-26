from typing import cast

from .types import BGRColor8, RGBColor01, RGBColor8

__all__ = [
    "bgr_color_from_string",
    "ColorConstants",
    "matplotlib_01_from_rgb",
]


def rgb_color_from_bgr_color(c: BGRColor8) -> RGBColor8:
    B, G, R = 0, 1, 2
    return c[R], c[G], c[B]


class ColorConstants:
    STR_WHITE = "white"
    STR_YELLOW = "yellow"
    STR_RED = "red"
    STR_BLACK = "black"
    STR_GRAY = "gray"
    STR_GREEN = "green"
    STR_BLUE = "blue"

    BLACK = (0, 0, 0)  # XXX
    BGR_RED: BGRColor8 = (0, 0, 255)
    BGR_GREEN: BGRColor8 = (0, 255, 0)
    BGR_WHITE: BGRColor8 = (255, 255, 255)
    BGR_BLACK: BGRColor8 = (0, 0, 0)
    BGR_GRAY: BGRColor8 = (128, 128, 128)
    BGR_BLUE: BGRColor8 = (255, 0, 0)
    BGR_YELLOW: BGRColor8 = (0, 255, 255)
    BGR_DUCKIETOWN_YELLOW: BGRColor8 = (0, 204, 255)

    RGB_RED: RGBColor8 = rgb_color_from_bgr_color(BGR_RED)
    RGB_GREEN: RGBColor8 = rgb_color_from_bgr_color(BGR_GREEN)
    RGB_WHITE: RGBColor8 = rgb_color_from_bgr_color(BGR_WHITE)
    RGB_BLACK: RGBColor8 = rgb_color_from_bgr_color(BGR_BLACK)
    RGB_GRAY: RGBColor8 = rgb_color_from_bgr_color(BGR_GRAY)
    RGB_BLUE: RGBColor8 = rgb_color_from_bgr_color(BGR_BLUE)
    RGB_YELLOW: RGBColor8 = rgb_color_from_bgr_color(BGR_YELLOW)
    RGB_DUCKIETOWN_YELLOW: RGBColor8 = rgb_color_from_bgr_color(BGR_DUCKIETOWN_YELLOW)


def matplotlib_01_from_rgb(c: RGBColor8) -> RGBColor01:
    mcolor = cast(RGBColor01, tuple(x / 255.0 for x in c))
    return mcolor


def bgr_color_from_string(s: str) -> BGRColor8:
    d = {
        ColorConstants.STR_YELLOW: ColorConstants.BGR_YELLOW,
        ColorConstants.STR_WHITE: ColorConstants.BGR_WHITE,
        ColorConstants.STR_BLACK: ColorConstants.BGR_BLACK,
        ColorConstants.STR_BLUE: ColorConstants.BGR_BLUE,
        ColorConstants.STR_RED: ColorConstants.BGR_RED,
        ColorConstants.STR_GRAY: ColorConstants.BGR_GRAY,
        ColorConstants.STR_GREEN: ColorConstants.BGR_GREEN,
    }
    if not s in d:
        msg = "No color %r found in %s" % (s, list(d))
        raise ValueError(msg)
    return d[s]

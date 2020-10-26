from typing import NewType, Tuple, TYPE_CHECKING

import numpy as np

__all__ = ["NPImage", "NPImageBGR", "NPImageRGB", 'NPImageGray', 'BGRColor8', 'RGBColor8', 'RGBColor01']

if TYPE_CHECKING:
    NPImage = NewType("NPImage", np.ndarray)
    NPImageBGR = NewType("NPImageBGR", NPImage)
    NPImageRGB = NewType("NPImageRGB", NPImage)
    NPImageGray = NewType("NPImageGray", NPImage)

else:
    NPImageGray = NPImageBGR = NPImageRGB = NPImage = np.ndarray

BGRColor8 = Tuple[int, int, int]
RGBColor8 = Tuple[int, int, int]
RGBColor01 = Tuple[float, float, float]
""" used by matplotlib """

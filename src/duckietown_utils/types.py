from typing import NewType, TYPE_CHECKING

import numpy as np

__all__ = ["NPImage", "NPImageBGR", "NPImageRGB", 'NPImageGray']

if TYPE_CHECKING:
    NPImage = NewType("NPImage", np.ndarray)
    NPImageBGR = NewType("NPImageBGR", NPImage)
    NPImageRGB = NewType("NPImageRGB", NPImage)
    NPImageGray = NewType("NPImageGray", NPImage)
else:
    NPImageGray = NPImageBGR = NPImageRGB = NPImage = np.ndarray

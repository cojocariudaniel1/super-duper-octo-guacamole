from enum import Enum
from dataclasses import dataclass
from PySide6.QtCore import Qt

class ImageType(Enum):
    USER_AVATAR = 1
    COMMUNITY_AVATAR = 2
    POST_AVATAR = 3
    COMMENT_AVATAR = 4
    BUTTON_ICON = 5
    STATUS_ICON = 6
    BACKGROUND_IMAGE = 7
    COMMUNITY_AVATAR_MINI = 8
    COMMENT_DEPTH_ICON = 9

@dataclass
class ImageConfig:
    size: int
    circular: bool
    aspect_ratio: Qt.AspectRatioMode
    transformation: Qt.TransformationMode

IMAGE_CONFIGS = {
    ImageType.USER_AVATAR: ImageConfig(
        size=40,
        circular=True,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.COMMUNITY_AVATAR: ImageConfig(
        size=35,
        circular=True,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.COMMUNITY_AVATAR_MINI: ImageConfig(
        size=24,
        circular=True,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.POST_AVATAR: ImageConfig(
        size=48,
        circular=True,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.BUTTON_ICON: ImageConfig(
        size=25,
        circular=False,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatio,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.STATUS_ICON: ImageConfig(
        size=16,
        circular=False,
        aspect_ratio=Qt.AspectRatioMode.KeepAspectRatio,
        transformation=Qt.TransformationMode.SmoothTransformation
    ),
    ImageType.BACKGROUND_IMAGE: ImageConfig(
        size=0,  # Will use original size
        circular=False,
        aspect_ratio=Qt.AspectRatioMode.IgnoreAspectRatio,
        transformation=Qt.TransformationMode.FastTransformation
    )
}
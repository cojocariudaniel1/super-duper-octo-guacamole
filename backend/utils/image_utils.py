import logging
import os
from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QIcon
from PySide6.QtCore import Qt

from image_config import ImageType, IMAGE_CONFIGS


def set_configured_image(item, image_name: str, image_type: ImageType, item_type: str) -> bool:
    """Set image with predefined configuration based on image type"""
    config = IMAGE_CONFIGS[image_type]

    if item_type == "label":
        return _set_image(
            label=item,
            image_name=image_name,
            size=config.size,
            circular=config.circular,
            aspect_ratio=config.aspect_ratio,
            transformation=config.transformation
        )
    else:
        return _set_image_button(
            label=item,
            image_name=image_name,
            size=config.size,
            circular=config.circular,
            aspect_ratio=config.aspect_ratio,
            transformation=config.transformation
        )


def set_image_default(label: QLabel, image_name: str, scaling: bool = True) -> bool:
    """Simplified version for basic image loading"""
    return _set_image(
        label=label,
        image_name=image_name,
        size=0,  # Use original size
        circular=False,
        aspect_ratio=Qt.AspectRatioMode.IgnoreAspectRatio,
        transformation=Qt.TransformationMode.FastTransformation,
        scaling=scaling
    )


def _set_image(
        label: QLabel,
        image_name: str,
        size: int = 0,
        circular: bool = False,
        aspect_ratio: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
        transformation: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
        scaling: bool = True
) -> bool:
    """Internal image setting function with all parameters"""
    try:
        image_path = os.path.join("frontend", "assets", "images", image_name)

        if not os.path.exists(image_path):
            logging.warning(f"Image not found: {image_path}")
            return False

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            logging.warning(f"Failed to load image: {image_path}")
            return False

        if size > 0:
            pixmap = pixmap.scaled(
                size, size,
                aspect_ratio,
                transformation
            )

        if circular and size > 0:
            circular_pixmap = QPixmap(size, size)
            circular_pixmap.fill(Qt.GlobalColor.transparent)

            painter = QPainter(circular_pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            label.setPixmap(circular_pixmap)
            label.setFixedSize(size, size)
        else:
            label.setPixmap(pixmap)
            if scaling:
                label.setScaledContents(True)

        return True

    except Exception as e:
        logging.critical(f"Error setting image: {e}")
        return False

def _set_image_button(
        label: QPushButton,
        image_name: str,
        size: int = 0,
        circular: bool = False,
        aspect_ratio: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
        transformation: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
        scaling: bool = True  # not used, but kept for interface consistency
) -> bool:
    """Internal image setting function for QPushButton"""
    try:
        image_path = os.path.join("frontend", "assets", "images", image_name)

        if not os.path.exists(image_path):
            logging.warning(f"Image not found: {image_path}")
            return False

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            logging.warning(f"Failed to load image: {image_path}")
            return False

        if size > 0:
            pixmap = pixmap.scaled(size, size, aspect_ratio, transformation)

        if circular and size > 0:
            circular_pixmap = QPixmap(size, size)
            circular_pixmap.fill(Qt.GlobalColor.transparent)

            painter = QPainter(circular_pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            icon = QIcon(circular_pixmap)
        else:
            icon = QIcon(pixmap)

        label.setIcon(icon)
        if size > 0:
            label.setIconSize(pixmap.rect().size())

        return True

    except Exception as e:
        logging.critical(f"Error setting button image: {e}")
        return False
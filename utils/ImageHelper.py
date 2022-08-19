# -*- coding: utf-8 -*-

import base64
from PIL import Image
import numpy as np
import cv2

def decode_base64(b64_data: str):
    """base64转numpy数组

    Args:
        b64_data (str): base64数据

    Returns:
        _type_: _description_
    """    
    image_bytes = base64.b64decode(b64_data)
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image_np2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    return image_np2
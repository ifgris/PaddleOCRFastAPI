# -*- coding: utf-8 -*-

from typing import List, Set

from pydantic import BaseModel


class OCRModel(BaseModel):
    coordinate: List  # 图像坐标
    result: Set


class Base64PostModel(BaseModel):
    base64_str: str  # base64字符串

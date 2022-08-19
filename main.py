# -*- coding: utf-8 -*-

from paddleocr import PaddleOCR
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.OCRModel import Base64PostModel
from models.RestfulModel import *
from utils.ImageHelper import *
import uvicorn


app = FastAPI(title="Paddle OCR API", description="基于 Paddle OCR 和 FastAPI 的自用接口")

ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# 跨域设置
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post('/ocr/predict-by-path', response_model=RestfulModel, tags=["OCR"], summary="识别本地图片")
def get_ocr_result(image_path: str):
    result = ocr.ocr(image_path, cls=True)
    restfulModel = RestfulModel(resultcode=200, message="Success", data=result, cls=OCRModel)
    return restfulModel

@app.post('/ocr/predict-by-base64', response_model=RestfulModel, tags=["OCR"], summary="识别 Base64 数据")
def get_ocr_result(base64model: Base64PostModel):
    img = decode_base64(base64model.base64_str)
    result = ocr.ocr(img, cls=True)
    restfulModel = RestfulModel(resultcode=200, message="Success", data=result, cls=OCRModel)
    return restfulModel

uvicorn.run(app, host='0.0.0.0', port=8000)
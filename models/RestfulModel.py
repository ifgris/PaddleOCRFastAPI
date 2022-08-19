# -*- coding: utf-8 -*-

from typing import List, Union
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse, Response

from .OCRModel import OCRModel

class RestfulModel(BaseModel):
    resultcode : int = 200 # 响应代码
    message: str = None # 响应信息
    data: Union[List, str] = [] # 数据

def resp_200(*, data: Union[list, dict, str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
    
            'code': 200,
            'message': "Success",
            'data': data,
        }
    )
    
def resp_400(*, data: str = None, message: str="BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
    
            'code': 400,
            'message': message,
            'data': data,
        }
    )
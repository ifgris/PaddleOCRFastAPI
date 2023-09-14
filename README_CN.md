# PaddleOCRFastAPI

一个可 Docker (Compose) 部署的, 基于 `FastAPI` 的简易版 Paddle OCR Web API.

## 版本选择

| PaddleOCR | Branch |
| :--: | :--: |
| v2.5 | [paddleocr-v2.5](https://github.com/cgcel/PaddleOCRFastAPI/tree/paddleocr-v2.5) |
| v2.7 | [paddleocr-v2.7](https://github.com/cgcel/PaddleOCRFastAPI/tree/paddleocr-v2.7) |

## 接口功能

- [x] 局域网范围内路径图片 OCR 识别
- [x] Base64 数据识别
- [x] 上传文件识别

## 部署方式

### 直接部署

1. 复制项目至部署路径

   ```shell
   git clone https://github.com/cgcel/PaddleOCRFastAPI.git
   ```

   > *master 分支为项目中支持的 PaddleOCR 的最新版本, 如需安装特定版本, 请克隆对应版本号的分支.*

2. (可选) 新建虚拟环境, 避免依赖冲突
3. 安装所需依赖

   ```shell
   pip3 install -r requirements.txt
   ```

4. 运行 FastAPI

   ```shell
   uvicorn main:app --host 0.0.0.0
   ```

### Docker 部署

在 `Centos 7`, `Ubuntu 20.04`, `Ubuntu 22.04`, `Windows 10`, `Windows 11` 中测试成功, 需要先安装好 `Docker`.

1. 复制项目至部署路径

   ```shell
   git clone https://github.com/cgcel/PaddleOCRFastAPI.git
   ```

   > *master 分支为项目中支持的 PaddleOCR 的最新版本, 如需安装特定版本, 请克隆对应版本号的分支.*

2. 制作 Docker 镜像

   ```shell
   docker build -t paddleocrapi:<your_tag> .
   ```

3. 编辑 `docker-compose.yml`

   ```yaml
   version: "3"

   services:

     PaddleOCR:
       container_name: paddle_ocr_api # 自定义容器名
       image: paddleocrapi:<your_tag> # 第2步自定义的镜像名与标签
       environment:
         - TZ=Asia/Hong_Kong
       ports:
        - 8000:8000 # 自定义服务暴露端口, 8000 为 FastAPI 默认端口, 不做修改
       restart: unless-stopped
   ```

4. 生成 Docker 容器并运行

   ```shell
   docker-compose up -d
   ```

5. Swagger 页面请访问 localhost:\<port\>/docs

## 运行截图

![Swagger](https://raw.githubusercontent.com/cgcel/PaddleOCRFastAPI/dev/screenshots/Swagger.png)

## License

```
Copyright 2023 GC Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

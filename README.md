# SimplePaddleOCRApi

一个可 Docker(compose) 部署的, 基于 `FastAPI` 的简易版 Paddle OCR Web API.

## 接口功能

- [x] 局域网范围内路径图片 OCR 识别
- [x] Base64 数据识别
- [x] 上传文件识别

## 部署方式

在 `Centos7` 的服务器中测试成功, 需要先安装好 `Docker`

1. 复制项目至部署路径

   ```shell
   git clone https://github.com/cgcel/SimplePaddleOCRApi.git
   ```

2. 制作 Docker 镜像

   ```shell
   docker build -t paddleocrapi:<your_tag> .
   ```

3. 编辑 `docker-compose.yml`

   ```yaml
   version: "2"

   services:

     PaddleOCR:
       container_name: paddle_ocr_api # 自定义容器名
       image: paddleocrapi:latest # 第2步自定义的镜像名与标签
       environment:
         - TZ=Asia/Hong_Kong
       ports:
        - 10778:8000 # 自定义服务暴露端口, 8000为FastAPI默认端口, 不做修改
       restart: unless-stopped
   ```

4. 生成 Docker 容器并运行

   ```shell
   docker-compose up -d
   ```
   
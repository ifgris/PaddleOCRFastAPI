# PaddleOCRFastAPI

[中文](https://github.com/cgcel/PaddleOCRFastAPI/blob/master/README_CN.md)

A Docker (Compose) deployable, simple version of the `FastAPI` based Paddle OCR Web API.

## Support Version

| PaddleOCR | Branch |
| :--: | :--: |
| v2.5 | [paddleocr-v2.5](https://github.com/cgcel/PaddleOCRFastAPI/tree/paddleocr-v2.5) |
| v2.7 | [paddleocr-v2.7](https://github.com/cgcel/PaddleOCRFastAPI/tree/paddleocr-v2.7) |

## Features

- [x] Local path image recognition
- [x] Base64 data recognition
- [x] Upload file recognition

## Deployment Methods

### Deploy Directly

1. Copy the project to the deployment path

   ```shell
   git clone https://github.com/cgcel/PaddleOCRFastAPI.git
   ```

   > *The master branch is the most recent version of PaddleOCR supported by the project. To install a specific version, clone the branch with the corresponding version number.*

2. (Optional) Create new virtual environment to avoid dependency conflicts
3. Install required dependencies

   ```shell
   pip3 install -r requirements.txt
   ```

4. Run FastAPI

   ```shell
   uvicorn main:app --host 0.0.0.0
   ```

### Docker Deployment

Test completed in `Centos 7`, `Ubuntu 20.04`, `Ubuntu 22.04`, `Windows 10`, `Windows 11`, requires `Docker` to be installed.

1. Copy the project to the deployment path

   ```shell
   git clone https://github.com/cgcel/PaddleOCRFastAPI.git
   ```

   > *The master branch is the most recent version of PaddleOCR supported by the project. To install a specific version, clone the branch with the corresponding version number.*

2. Building a Docker Image

   ```shell
   docker build -t paddleocrapi:<your_tag> .
   ```

3. Edit `docker-compose.yml`

   ```yaml
   version: "3"

   services:

     PaddleOCR:
       container_name: paddle_ocr_api # Custom Container Name
       image: paddleocrapi:<your_tag> # Customized Image Name & Label in Step 2
       environment:
         - TZ=Asia/Hong_Kong
       ports:
        - 8000:8000 # Customize the service exposure port, 8000 is the default FastAPI port, do not modify
       restart: unless-stopped
   ```

4. Create the Docker container and run

   ```shell
   docker compose up -d
   ```

5. Swagger Page at `localhost:<port>/docs`

## Screenshots

![Swagger](https://raw.githubusercontent.com/cgcel/PaddleOCRFastAPI/dev/screenshots/Swagger.png)

## Todo

- [ ] support ppocr v4
- [ ] GPU mode
- [ ] Image url recognition

## License

```License
Copyright 2023 GC Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

# PaddleOCRFastAPI

![GitHub](https://img.shields.io/github/license/cgcel/PaddleOCRFastAPI)

[中文](https://github.com/cgcel/PaddleOCRFastAPI/blob/master/README_CN.md)

A simple way to deploy `PaddleOCR` based on `FastAPI`.

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
   docker build -t paddleocrfastapi:<your_tag> .
   ```

3. Edit `docker-compose.yml`

   ```yaml
   version: "3"

   services:

     paddleocrfastapi:
       container_name: paddleocrfastapi # Custom Container Name
       image: paddleocrfastapi:<your_tag> # Customized Image Name & Label in Step 2
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
- [x] Image url recognition

## License

**PaddleOCRFastAPI** is licensed under the MIT license. Refer to [LICENSE](https://github.com/cgcel/PaddleOCRFastAPI/blob/master/LICENSE) for more information.

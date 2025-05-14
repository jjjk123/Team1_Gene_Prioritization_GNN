### Run XGDAG using Docker

#### Dir contents

Dockerfile_quick_2025-05-14 - a dockerfile that integrates small mods in the XGDAG codebase for a quick deployment - but may stop working with future XGDAG releases.

#### Instructions for Dockerfile_quick_2025-05-11

**1. Download the XGDAG repository and prepare the Dockerfile**
```bash
mkdir test
cd test
git clone https://github.com/GiDeCarlo/XGDAG
nano Dockerfile
```
Paste the provided Dockerfile content and save the file.

**2. Build and run the Docker image**
```bash
docker build -t xgdag_test .
docker run -it xgdag_test
```

**3. Test if it works**
```bash
python TrainerScript.py
```

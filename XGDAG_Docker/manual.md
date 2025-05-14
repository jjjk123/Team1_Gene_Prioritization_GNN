### Run XGDAG using Docker

**1. Download the XGDAG repository and prepare the Dockerfile**
```bash
mkdir test
cd test
git clone https://github.com/GiDeCarlo/XGDAG
cd XGDAG
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

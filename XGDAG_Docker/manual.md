### Run XGDAG using Docker

### Choose one of the paths

A) Dockerfile_quick_2025-05-14 - has the mods integrated for a quick deployment - but may stop working with future XGDAG releases.
B) Dockerfile - requires manual changes to the XGDAG code as accessed on 2025-05-14, detailed in the manual below.


### A - Instructions for Dockerfile_quick_2025-05-14

1. Download the XGDAG repository and prepare the Dockerfile
```bash
mkdir test
cd test
git clone https://github.com/GiDeCarlo/XGDAG
nano Dockerfile
```
Paste the contents of the 'Dockerfile_quick_2025-05-14' file provided here into your 'Dockerfile'.

2. Build and run the Docker image
```bash
docker build -t xgdag_test .
docker run -it xgdag_test
```

3. Test if it works
```bash
python TrainerScript.py
```


### B - Instructions for Dockerfile

1. Download the XGDAG repository and prepare the Dockerfile

```bash
mkdir test
cd test
git clone https://github.com/GiDeCarlo/XGDAG
```

2. Modify the XGDAG codebase before it is copied into the container

#### Add a missing __init__.py file
```bash
touch XGDAG/SubgraphX/__init__.py
```
#### Fix relative import in SubgraphX.py
```bash
sed -i 's/from SubgraphXshapley/from .SubgraphXshapley/' XGDAG/SubgraphX/SubgraphX.py
```
3. Create a docker file - paste the content of provided 'Dockerfile'
```bash
nano Dockerfile
```

4. Build and run the Docker image
```bash
docker build -t xgdag_test .
docker run -it xgdag_test
```

5. Test if it works
```bash
python TrainerScript.py
```

## Run XGDAG using Docker

### Choose one of the paths

A) Dockerfile_quick_2025-05-14 - has the mods integrated for a quick deployment - but may stop working with future XGDAG releases.
B) Dockerfile - requires manual changes to the XGDAG code as accessed on 2025-05-14, detailed in the manual below.


### A - Instructions for Dockerfile_quick_2025-05-14

1. Download the XGDAG repository
```bash
mkdir test
cd test
git clone https://github.com/GiDeCarlo/XGDAG
```

2. Create 'Dockerfile' in the same dir and paste the contents from 'Dockerfile_quick_2025-05-14' and save
```bash
nano Dockerfile
```

3. Build the Docker image
```bash
docker build -t xgdag_test .
```

4. Run a Docker container
```bash
docker run -it xgdag_test
```

5. Test if XGDAG works
```bash
python TrainerScript.py
```


### B - Instructions for Dockerfile

1. Download the XGDAG repository
   
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
3. Create a docker file - paste the content of provided 'Dockerfile' and save
```bash
nano Dockerfile
```

4. Build the Docker image
```bash
docker build -t xgdag_test .
```

5. Run a Docker container
```bash
docker run -it xgdag_test
```

6. Test if XGDAG works
```bash
python TrainerScript.py
```

# A Simple Web App utilizing NOAA Weather API:

Basic Usage:
```
python app.py **lat** **lon** [--weekly-text] [--hourly-text] [--weekly-graphical] [--hourly-graphical] [--raw]
```
> Note, must include flag that specifies the nature of the output.  (one of the first 4)

see the reports folder afterwards for results, depending on what you ran.

The python notebooks in 'notebooks' can be changed to your liking.  Uses a special extension to accomplish passing variables to the notebook.

## Virtual Environment:
```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

# Building the docker image:
From the main folder:
```
podman build -t monarch:dev .
```

# Troubleshooting the container while building:
```
podman run -ti --rm monarch:dev /bin/bash
```
> This'll allow you to enter the container in a bash shell and auto-removes the <br>
> container when done.

# Running the program:

```
podman run --volume ./reports:/app/reports \
    --rm monarch:dev \
    python3 app.py [LATITUDE] [LONGITUDE] --weekly-text
```

```
# In root project folder:
podman run --volume $(pwd)/reports:/app/reports \
    --volume $(pwd)/notebooks:/app/notebooks \
    --rm monarch:dev \
    python3 app.py [LATITUDE] [LONGITUDE] --weekly-text
```
> Note: SELinux is an issue with mounting volumes. <br>
> The easiest work-around is disabling SELinux with 'setenforce 0' on the host machine.
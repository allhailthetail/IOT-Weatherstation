# Basic Usage:
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

# Running the program (No SELinux):
```
# In root project folder:
podman run --volume $PROJ_DIR/reports:/app/reports  \
    --rm monarch:dev python3 app.py [LAT] [LONG] \
    --weekly-text --hourly-text --raw \
    --weekly-graphical
```
> Note: SELinux is an issue with mounting volumes. <br>
> The easiest work-around is disabling SELinux with 'setenforce 0' on the host machine.

# Running the program (SELinux):
```
# Install necessary utilities for working with SELinux Permissions:
sudo dnf install policycoreutils container-selinux

sudo semanage fcontext -a -t container_file_t /some_dir/monarch/reports/

# Verify it took with ls -ldZ ../reports

# In root project folder:
podman run --volume $PROJ_DIR/reports:/app/reports:Z  \
    --rm monarch:dev python3 app.py [LAT] [LONG] \
    --weekly-text --hourly-text --raw \
    --weekly-graphical
```
> Podman/Docker and SELinux have some reconciling to do when it comes to SELinux <br>
> and security...  Specifically, special labeling is required to inform SELinux of <br>
> what Docker is doing... 

# Configuring Systemd:
Now, the goal is to have this weather report run on a schedule. i.e. every few hours <br>
This automation can be achieved on most Linux systems using systemd. <br>
More specifically, since this is a userspace app, systemd should be configured using the <br>
userspace version of systemd as shown:

Steps:
1. Create the appropriate `~/.config/systemd/user/` folder
2. Move the systemd .service and .timer [scripts](../scripts/) into this folder.
3. Refresh daemon `systemctl --user daemon-reload`
4. Enable the service and timers as shown:

``` shell
# Enable the timer, which will run on frequency accoriing to .timer file:
systemctl --user enable weather-report.timer

# Run the timer on-demand, triggering immediately:
systemctl --user start weather-report.timer

# Query the status of the service itself:
systemctl --user status weather-report.service
```

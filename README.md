# UrbanCode Deploy in Docker
UrbanCode Deploy is an IBM product for automating software deployments. The basic architecture is server-agent. This project allows you to run IBM UCD in containers using Docker Compose.

### Supported Version
Currently tested on version 6.2.1 of UrbanCode Deploy.

### Dependencies
- Docker Compose 1.6 or above
- Docker 1.10 or above
- There is an external dependency on the software itself, however you can download a free evaluation license (60 days) that works with this just fine [from the IBM website right here]. 
- You also need python (2.7) installed.

### Platforms
If you are on Linux this should work out of the box. Users on Windows or OSX will either need Docker Machine installed and configured correctly, or be running the beta native Docker versions for their respective platform.

### Instructions
1. Clone this repo
2. Download the software from the above link
3. Extract the `ibm-ucd-install` folder and place it at the top-level of the cloned repo
4. Run `initial_config.py` (either by double-clicking or switching into the directory and running in a terminal, you may need to make it executable on Linux platforms)
5. Run `docker-compose up`.

In a couple of minutes you should have both containers up and running. Verify by opening a web browser to `https://<localhost-or-address-of-docker-machine>:8443`.

You can scale the agent by moving into the project directory and typing `docker-compose scale agent=X`.

You only need to run `initial_config.py` on first run / build. After that use the [native docker-compose commands].


[from the IBM website right here]: <https://www14.software.ibm.com/webapp/iwm/web/preLogin.do?source=RATLe-UCDeploy-EVAL&S_CMP=web_dw_rt_swd>
[native docker-compose commands]: <https://docs.docker.com/compose/reference/overview/>
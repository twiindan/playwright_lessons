
1. Build jenkins docker image

```bash
docker build -t myjenkins .
```

2. Docker compose up

```bash
docker compose -f docker-compose-jenkins.yml up
```

3. Configure initial steps in Jenkis
4. Install the following plugins:
- Docker
- Docker commons
- Docker pipelines
- Docker API
- Allure

5. Reebot Jenkins
6. Manage Jenkins --> Cloud --> New Cloud
   1. Select Docker
   2. Put in Docker Host URI: unix:///var/run/docker.sock
   3. Click on enable

7. Manage Jenkins --> Tools
   1. Docker installation
      1. Install automatically
      2. Docker version latest
      3. From docker.com
   2. Allure Commandline installation
      1. Install automatically
      2. From maven central 2.32.2

8. New Task
   1. Pipeline
   2. Pipeline from SCM (https://github.com/twiindan/playwright_lessons.git)
   3. Branch --> */main
   4. Script Path --> Jenkinsfile_docker

    
# Readme

## GitLab

### Root user

Username: `root`
Password: `devops2019`

### Ann's User

Username:


### Current Gitlab

https://devops-2019-jhu-fall.s3.amazonaws.com/gitlab-ce.tar

Google Drive Link:
https://drive.google.com/open?id=1OdQsmSEFhLoWNjBkM-K--dG5n48KyQEl

### Notes 11/13/2019 - GitLab + Docker Registry

Useful guides:

* https://docs.docker.com/registry/deploying/
* http://clusterfrak.com/sysops/app_installs/gitlab_container_registry/
* https://docs.docker.com/registry/insecure/

Setting up a registry should be a simple as running:
```
sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

Seems that GitLab wants a domain name for the registry. Sounds like we can modify our `/etc/hosts` file to create a fake domain name and map it to an IP address.

GitLab may come packaged with nginx. I don't think we need nginx unless we're using SSL.

I think we can disable SSL by setting our registry as an insecure registry in Docker's daemon config, `/etc/docker/daemon.json`:
```
{
  "insecure-registries" : ["myregistrydomain.com:5000"]
}
```
(Then restart Docker.)
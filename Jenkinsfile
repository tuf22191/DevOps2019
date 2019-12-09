pipeline {
  agent any
  stages {
    stage('Build image') {
      steps {
        echo 'Building docker image'
        script {
          sh 'docker build -t 34.201.236.34:6000/root/project'
        }
      }
    }
    stage('Push image') {
      steps {
        script {
          sh 'docker push 34.201.236.34:6000/root/project'
        }
      }
    }
    stage('snyk scan') {
      tools {
        snyk 'snyk-latest'
      }
      steps {
        snykSecurity(
          organisation: 'cloudbees',
          severity: 'high',
          snykInstallation: 'snyk-latest',
          snykTokenId: 'snyk',
          targetFile: 'Dockerfile',
          failOnIssues: 'true'
        )
      }
    }
  }
}

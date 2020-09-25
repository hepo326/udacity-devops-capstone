pipeline {
     environment { 
        registry = "minageorge/udacity-devops-capstone" 
        registryCredential = 'dockerhub' 
        dockerImage = '' 
    }

	agent any
	stages {

      stage('Building Docker Image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":latest" 
                }
            } 
        }

        stage('Push Docker Image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                }
            } 
        }

        stage('Test Docker Image') { 
            steps { 
                script { 
                    docker container run -p 300:80 registry
                }
            } 
        }
    }
}
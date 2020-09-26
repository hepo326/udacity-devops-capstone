pipeline {
     environment { 
        registry = "minageorge/udacity-devops-capstone" 
        registryCredential = 'dockerhub' 
        awsCredential = 'aws-eks' 
        cluster = 'Udacity-Capstone-cluster' 
        region = 'us-west-2'
        dockerImage = '' 
        deploymentType = 'blue'
    }

	agent any
	stages {

    stage('Building Docker Image') { 
        steps { 
            script { 
                
                dockerImage = docker.build registry
                docker.withRegistry( '', registryCredential ) { 
                    dockerImage.push() 
                  }
                }
            } 
        }

    stage('Detect Deployment Type') { 
        steps { 
            script { 
                
                if (env.BRANCH_NAME == 'development' || env.CHANGE_TARGET == 'development') {
                       env.deploymentType = 'blue'
                 }
                
                else if (env.BRANCH_NAME == 'master' || env.CHANGE_TARGET == 'master') {
                       env.deploymentType = 'green'
                 }
    
            }
        } 
        
        }

     stage('Deployment') {
        steps {
            withAWS(region: region, credentials: awsCredential) {
                sh '''
                    aws eks --region ${region} update-kubeconfig --name  ${cluster}
                    kubectl config use-context arn:aws:eks:${region}:209202834263:cluster/${cluster}
                    kubectl apply -f ./${deploymentType}-controller.json
                    kubectl apply -f ./${deploymentType}-service.json
                '''
               }
             }
		}
  

    }
}
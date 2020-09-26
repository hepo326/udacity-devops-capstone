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

    stage('Detect Deployment Type') { 
        steps { 
            script { 
                
                if (env.BRANCH_NAME == 'development' || env.CHANGE_TARGET == 'development') {
                       env.DEPLOYMENT_TYPE = 'blue'
                 }
                
                else if (env.BRANCH_NAME == 'master' || env.CHANGE_TARGET == 'master') {
                       env.DEPLOYMENT_TYPE = 'green'
                 }
    
            }
        } 
        
        }

     stage('Deployment') {
        steps {
            withAWS(region:'us-west-2', credentials:'aws-eks') {
                sh '''
                    aws eks --region us-west-2 update-kubeconfig --name Udacity-Capstone-cluster
                    kubectl config use-context arn:aws:eks:us-west-2:209202834263:cluster/Udacity-Capstone-cluster
                    kubectl apply -f ./${DEPLOYMENT_TYPE}-controller.json
                    kubectl apply -f ./${DEPLOYMENT_TYPE}-service.json
                '''
               }
             }
		}
  

    }
}
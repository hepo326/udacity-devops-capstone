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

    stage('Cluster config') {
        steps {
            withAWS(region:'us-west-2', credentials:'aws-eks') {
                sh '''
                    aws eks --region us-west-2 update-kubeconfig --name Udacity-Capstone-cluste
                '''
               }
             }
		}    

     stage('Kubectl context') {
        steps {
            withAWS(region:'us-west-2', credentials:'aws-eks') {
                sh '''
                    kubectl config use-context arn:aws:eks:us-west-2:209202834263:cluster/Udacity-Capstone-cluste
                '''
               }
             }
		}     

     stage('Blue deployment') {
        steps {
            withAWS(region:'us-west-2', credentials:'aws-eks') {
                sh '''
                    kubectl apply -f ./blue-controller.json
                    kubectl apply -f ./blue-service.json
                '''
               }
             }
		}
  

    }
}
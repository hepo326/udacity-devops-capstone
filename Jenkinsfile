pipeline {
     environment { 
        registry = "minageorge/udacity-devops-capstone" 
        registryCredential = 'dockerhub' 
        awsCredential = 'aws-eks' 
        cluster = 'Udacity-Capstone-cluster' 
        region = 'us-west-2'
        dockerImage = '' 
        imageVersion = 'latest' 
    }

	agent any
	stages {


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

    stage('Building Docker Image') { 
        steps { 
            script { 
                
                dockerImage = docker.build ('${registry}:${imageVersion}')
                docker.withRegistry( '', registryCredential ) { 
                    dockerImage.push() 
                
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
                    kubectl apply -f ./${DEPLOYMENT_TYPE}-controller.json
                    kubectl apply -f ./${DEPLOYMENT_TYPE}-service.json
                    kubectl rollout restart replicationcontroller/${DEPLOYMENT_TYPE}
                '''
               }
             }
		}
  

    }
}
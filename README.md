## SageMaker endpoint with custom container

Light-weight sample of a SageMaker endpoint with custom container.

This repo contains all the code related to this blog post on Medium.

#### Configuring into AWS Session

#### Pushing into ECR
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 887612375756.dkr.ecr.ap-southeast-1.amazonaws.com
docker build -t rag_penal_test .
docker tag rag_penal_test:latest 887612375756.dkr.ecr.ap-southeast-1.amazonaws.com/rag_penal_test:latest
docker push 887612375756.dkr.ecr.ap-southeast-1.amazonaws.com/rag_penal_test:latest
# Build and Test Image

docker build --platform linux/amd64 -t docker-lambda-python:latest .

docker run --platform linux/amd64 -p 9000:8080 docker-lambda-python:latest

curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

# Login ECR

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 381491872181.dkr.ecr.us-east-1.amazonaws.com

# Create ECR Repo (Only Once)

aws ecr create-repository --repository-name hello-world --region us-east-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

# Push Image to ECR

docker tag docker-image:test 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

docker push 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

# Create Lambda (Only Once)

aws lambda create-function \
  --function-name hello-world \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest \
  --role arn:aws:iam::111122223333:role/lambda-ex

# Invoke Lambda

aws lambda invoke --function-name hello-world response.json
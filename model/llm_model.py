import boto3
from sagemaker import get_execution_role, Model

def deploy_llm_model():
    # Set up SageMaker session and role
    sagemaker_session = boto3.Session()
    role = get_execution_role()

    # Specify your LLM model and entry script
    model = Model(
        model_data='s3://your-s3-bucket/path/to/your/model.tar.gz',
        image_uri='LLM CONTAINER HERE',
        role=role,
        sagemaker_session=sagemaker_session,
    )

    # Deploy the model to an endpoint
    predictor = model.deploy(
        instance_type='ml.m5.large',
        endpoint_name='END POINT HERE',
    )

    print(f"Model deployed successfully to endpoint: {predictor.endpoint_name}")

if __name__ == "__main__":
    deploy_llm_model()

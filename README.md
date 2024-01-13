# ML-Ops-Pipeline-for-Text-Generation

The README file provides detailed instructions and documentation for setting up and using the project. It includes information on prerequisites, installation, configuration, and usage.

This project aims to deploy and evaluate a text-generation language model (LLM) using Amazon SageMaker for deployment and GitHub Actions for continuous integration and continuous deployment (CI/CD). The pipeline includes monitoring, logging, and performance evaluation using BLEU score.

# Explanation:
llm_model.py:This script deploys the text-generation language model using Amazon SageMaker. It connects to a given AWS account, specifies the model location, and deploys it to an endpoint.

monitoring_logging/llm_monitoring_setup.py: This script sets up monitoring and logging for the deployed model using Amazon CloudWatch for real-time monitoring and AWS CloudTrail for logging API calls. Adjustments can be made based on specific metrics and logging requirements.

performance_monitor/performance_eval.py: This script evaluates the performance of the text-generation model using BLEU score, comparing the model's output to a baseline output. Adjust the script based on your specific evaluation criteria.

.github/workflows/llm_model.yml: This GitHub Actions workflow is triggered on pushes to the main branch. It automates the deployment process, running linting, testing, and the model deployment script.

requirements.txt: This file lists the Python dependencies for your this project. It includes libraries like boto3 for AWS interactions and nltk for BLEU score calculation.


# Setup Instructions:

Follow these steps to set up and use the project:

AWS Setup:

1. AWS SageMaker Deployment:
- Train your text-generation model and store artifacts in an S3 bucket.
- Update llm_model.py with the S3 path and model configurations.
- Run python llm_model.py to deploy the model to SageMaker.
2. GitHub Actions Setup:
- Add AWS credentials as secrets in your GitHub repository.
- Adjust workflow settings in llm_model.yml if needed.
- Push changes to the main branch to trigger the workflow.
3. Monitoring and Logging:
- Run python monitoring_and_logging/llm_monitoring_setup.py to set up CloudWatch and CloudTrail.
4. Performance Evaluation:
- Update performance_eval.py with your model and baseline outputs.
- Run python performance_evaluation/performance_eval.py to calculate BLEU score.

# Usage Instructions:

1. Model Deployment:
- Use the llm_model.py script to deploy your text-generation model to SageMaker.
2. Continuous Integration/Continuous Deployment:
- Push changes to the main branch to trigger the GitHub Actions workflow.
- The workflow will automatically run linting, testing, and deploy the model on AWS.
3. Monitoring and Logging:
- Run the monitoring_and_logging/llm_monitoring_setup.py script to configure CloudWatch and CloudTrail.
4. Performance Evaluation:
- Update performance_eval.py with your model and baseline outputs.
- Run performance_evaluation/performance_eval.py to calculate BLEU score.


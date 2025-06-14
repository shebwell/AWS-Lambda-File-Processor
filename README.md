# AWS-Lambda-File-Processor
# 📦 Project 3: AWS Lambda File Processor

A serverless file processing system built on AWS that triggers a Lambda function whenever a file is uploaded to an S3 bucket. The system is fully provisioned using Terraform and exposes the Lambda function through a public HTTP endpoint via API Gateway.

---

## 📌 Project Overview

This project demonstrates how to build an event-driven, serverless architecture on AWS using infrastructure-as-code and CI/CD automation tools.

**Key Features:**
- Automatically triggers an AWS Lambda function when a file is uploaded to an S3 bucket.
- Infrastructure provisioned and managed using Terraform.
- Lambda function deployment automated via Jenkins or GitHub Actions.
- Publicly accessible HTTP endpoint exposed through AWS API Gateway.

---

## 🛠️ Tech Stack

- **AWS Lambda**
- **Amazon S3**
- **AWS API Gateway**
- **IAM Roles & Policies**
- **Terraform**
- **GitHub Actions (for CI/CD)**

---

## 📄 Project Requirements

- Use Terraform to:
  - Create an S3 bucket.
  - Create an AWS Lambda function.
  - Set up necessary IAM roles and permissions.
  - Configure API Gateway to expose the Lambda function.

- Deploy the Lambda function using:
  - **Jenkins** _or_
  - **GitHub Actions**

- Expose the Lambda function via a public HTTP endpoint using API Gateway.

---

## 🚀 Deployment

1. Clone the repository.
2. Configure AWS credentials and region in your environment.
3. Run `terraform init`, `terraform plan`, and `terraform apply` to provision infrastructure.
4. Deploy the Lambda function using your chosen CI/CD tool.
5. Test file uploads to the S3 bucket and verify Lambda invocation via logs or API Gateway responses.

---

## 📎 License

This project is for educational and portfolio-building purposes.

---

## 👤 Author

Sheilla W / [@shebwell](https://github.com/shebwell)

# S3文件自动同步到EC2实例方案

## 方案架构

![alt text](https://github.com/zhixueli/s3-lambda-runcmd/blob/main/img/arch.jpeg?raw=true)

## 操作步骤

### 1. 为lambda创建execution role，允许lambda调用System Manager run command，除了为这个role添加基本的AWSLambdaBasicExecutionRole managed policy之外，需要额外添加如下policy：

、、、
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ssm:SendCommand",
            "Resource": "*"
        }
    ]
}
、、、

### 2. 创建lambda函数（代码如src目录下所示），并将lambda execution role配置为第1步骤中所创建的role

### 3. 按需创建源文件存储桶（或使用已有存储桶），并配置将All object create events notification指向第2步中创建的lambda函数

### 4. 开启一台EC2实例，通过EC2 role或者其他方式授权实例访问第3步中配置的存储桶，并将实例id配置为第2步中创建的lambda函数的环境变量
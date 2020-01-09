"""
Authored by Kim Clarence Penaflor
08/01/2019
version 0.0.1
Documented via reST

AWS S3 Controller
"""


import boto3

class S3:
    """
    S3 Boto3 Controller
    """

    def __init__(self, bucketName, awsCred):
        """
        Initialize S3 Bucket
        :param bucketName: AWS S3 Bucketname
        :param awsCred: AWS Credentials (id and secret token)
        :type bucketName: string
        :type awsCred: Dictionary {'aws_id': '<aws ID>', 'aws_secret' : '<aws secret token'}
        """

        self.bucketName = bucketName
        self.S3_c = boto3.client(
            's3',
            aws_access_key_id = awsCred['aws_id'],
            aws_secret_access_key = awsCred['aws_secret'],
            region_name = 'ap-southeast-1'
        )
        self.S3_r = boto3.resource(
            's3',
            aws_access_key_id = awsCred['aws_id'],
            aws_secret_access_key = awsCred['aws_secret'],
            region_name = 'ap-southeast-1'
        )

    def load_resource_content(self, key):
        """
        Load s3 resource
        :param key: resource full dir name
        :type key: string
        :returns: resource content
        :rtype: string
        """

        s3Object = self.S3_r.Object(self.bucketName, key)
        sContent = s3Object.get()['Body'].read().decode('utf-8')
        return sContent

    def save_resource(self, key, body, cType='text/plain'):
        """
        Save s3 resource
        :param key: resource full dir name
        :param body: resource object content
        :param cType: resource content type
        :type key: string
        :type body: depends on the content type
        :type cType: string
        """
        s3Object = self.S3_r.Object(self.bucketName, key)
        s3Object.put(
            ContentType = cType,
            Body = body
        )


# aws-lambda-kinesis-windowseventlog

Author Marthijn van den Brand
Fox-IT

AWS lambda to transform the json from AWS kinesis agent to useful json documents for elasticsearch

By default the AWS kinesis agent consumes windows eventlogs and pushes records to AWS kinesis firehose. Unfortunately the
usefull information is embedded in one 'description' field. With this lambda the json records are dissected to
separate fields so the Destition (f.e. ElastisSearch) can process the fields seperately allowing for easy usuage.

This lambda was created to support sysmon eventlogs to elasticsearch transfer.

Sysmon (Microsoft) -> Windows EventLog -> AWS Kinesis -> ElasticSearch


This AWS lambda is to be used as a kinesis firehose lambda en needs firehose permissions to be able to handle the incoming records. 
The output of the lamba is the same as the input but the json dict is dissected to seperate key values. 

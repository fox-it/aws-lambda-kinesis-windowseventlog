# aws-lambda-kinesis-windowseventlog
# Author Marthijn van den Brand
# Fox-IT

AWS lambda to transform the json from AWS kinesis agent to useful json documents for elasticsearch

By default the AWS kinesis agent consumes windows eventlogs and pushes records to AWS kinesis firehose. Unfortunately the
usefull information is embedded in one 'description' field. With this lambda the json records are dissected to
separate fields so the Destition (f.e. ElastisSearch) can process the fields seperately allowing for easy usuage.

This lambda was created to support sysmon eventlogs to elasticsearch transfer.

Sysmon (Microsoft) -> Windows EventLog -> AWS Kinesis -> ElasticSearch
                                               ^
                                            lambda

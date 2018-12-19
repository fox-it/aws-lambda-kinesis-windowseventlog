from __future__ import print_function

import base64
import json

print('Loading function')

def lambda_handler(event, context):
    output = []
    succeeded_record_cnt = 0
    failed_record_cnt = 0

    for record in event['records']:
        payload = base64.b64decode(record['data'])
        output_record = json.loads(payload.decode("utf-8","ignore"))

        try:
            if 'Description' in output_record:
                desc_text = output_record['Description']
                tmp = desc_text.split("\r\n")
                first = True
                for item in tmp:
                    fields = item.split(":",1)
                    if first:
                        output_record['Event'] = fields[0].strip()
                        first = False
                    else:
                        output_record[fields[0].strip()] = fields[1].strip()
                del output_record['Description']

            if 'Hashes' in output_record:
                hashes = output_record['Hashes']
                tmp = hashes.split(",")
                for item in tmp:
                    i = item.split("=")
                    output_record[i[0].strip()] = i[1].strip()
                del output_record['Hashes']

            succeeded_record_cnt += 1
            rescode = 'Ok'
        except:
            failed_record_cnt += 1
            rescode = 'ProcessingFailed'

        output_rec = {
            'recordId': record['recordId'],
            'result': rescode,
            'data': base64.b64encode(json.dumps(output_record))
        }
        output.append(output_rec)

    print('Processing completed.  Successful records {}, Failed records {}.'.format(succeeded_record_cnt, failed_record_cnt))
    return {'records': output}


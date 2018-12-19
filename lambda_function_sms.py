from __future__ import print_function

import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')


def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))

    attributes = event['placementInfo']['attributes']

    phone_number = attributes['phoneNumber']
    message = attributes['message']

    for key in attributes.keys():
        message = message.replace('{{%s}}' % (key), attributes[key])
    message = message.replace('{{*}}', json.dumps(attributes))

    dsn = event['deviceInfo']['deviceId']
    click_type = event['deviceEvent']['buttonClicked']['clickType']
    message += '\n(DSN: {}, {})'.format(dsn, click_type)

    sns.publish(PhoneNumber=phone_number, Message=message)

    logger.info('SMS has been sent to ' + phone_number)

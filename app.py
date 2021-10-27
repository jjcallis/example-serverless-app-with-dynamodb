# app.py

import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

if os.environ.get('IS_OFFLINE'):
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')

@app.route("/")
def hello():
    return "Up and running!"


@app.route("/product/<string:profile_id>")
def get_profile(profile_id):
    resp = client.get_item(
        TableName=DYNAMODB_TABLE,
        Key={
            'productId': { 'S': profile_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'Product does not exist'}), 404

    return jsonify({
        'productId': item.get('productId').get('S'),
        'productTitle': item.get('productTitle').get('S')
    })


@app.route("/product", methods=["POST"])
def create_profile():
    profile_id = request.json.get('productId')
    productTitle = request.json.get('productTitle')
    if not profile_id or not productTitle:
        return jsonify({'error': 'Please provide productId and productTitle'}), 400

    res = client.put_item(
        TableName=DYNAMODB_TABLE,
        Item={
            'productId': {'S': profile_id },
            'productTitle': {'S': productTitle }
        }
    )

    return jsonify({
        'productId': profile_id,
        'productTitle': productTitle
    })

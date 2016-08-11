import boto3

client = boto3.client('elb')

response = client.create_load_balancer(
    LoadBalancerName='sample-load-balancer-1',
    Listeners=[
        {
            'Protocol': 'http',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'http',
            'InstancePort': 80
        },
    ],
    AvailabilityZones=[
        'us-west-2a',
        'us-west-2b'
    ],
    SecurityGroups=[
        'sg-b39eb7d5',
    ]
)

print(response)

for key in response:
    print(key, type(key))

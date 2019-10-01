from aws_cdk import core, aws_ec2, aws_ecs, aws_ecs_patterns


class CdkPyconFlaskStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = aws_ec2.Vpc.from_lookup(self, 'cdkVPC', vpc_id='vpc-06bc80b08769c2824')
        # vpc = aws_ec2.Vpc(self, 'FargateFlaskVPC', cidr='10.0.0.0/16', nat_gateways=1)
        
        # ECS cluster
        cluster = aws_ecs.Cluster(self, 'Cluster', vpc=vpc)
        svc = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self, 'FargateService',
            cluster=cluster,
            image=aws_ecs.ContainerImage.from_asset('flask-docker-app'),
            container_port=5000,
            environment={
                'PLATFORM': 'AWS Fargate :-)'
            }
        )

        core.CfnOutput(self, 'SericeURL', value="http://{}".format(
            svc.load_balancer.load_balancer_dns_name))
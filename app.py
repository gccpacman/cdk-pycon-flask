#!/usr/bin/env python3

from aws_cdk import core

from cdk_pycon_flask.cdk_pycon_flask_stack import CdkPyconFlaskStack


app = core.App()
CdkPyconFlaskStack(app, "cdk-pycon-flask", env={'account': '959696344829', 'region': 'ap-northeast-2'})

app.synth()

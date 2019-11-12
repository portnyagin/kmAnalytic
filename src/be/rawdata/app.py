# -*- coding: utf-8 -*-
import logging

from injector import Module, Injector, inject, singleton
from flask import Flask, Request, jsonify
from flask_injector import FlaskInjector
from flask_marshmallow import Marshmallow

import connexion
from connexion.resolver import RestyResolver
from os import environ

from be.rawdata.providers.provider import ClientProvider
from be.rawdata.repository.client_repository import ClientRepository


il = logging.getLogger('injector')
il.addHandler(logging.StreamHandler())
il.level = logging.DEBUG

"""
This is an example of using Injector (https://github.com/alecthomas/injector) and Flask.
Flask provides a lot of very nice features, but also requires a lot of globals
and tightly bound code. Flask-Injector seeks to remedy this.
"""

 #
 # def configure_for_testing(binder):
 #    configuration = Configuration(':memory:')
 #    binder.bind(Configuration, to=configuration, scope=singleton)



class AppModule(Module):
    def __init__(self, app):
        self.app = app

    """Configure the application."""

    def configure(self, binder):
        cp = ClientProvider()

        cl_repo = ClientRepository()
        binder.bind(ClientProvider, to=cp, scope=singleton)
        binder.bind(ClientRepository, to=cl_repo, scope=singleton)

def main():
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    app.add_api('rawdata_service_docs.yaml', resolver=RestyResolver('api'))
    app.debug = True

    injector = Injector([AppModule(app)])

    FlaskInjector(app=app.app, injector=injector)
    # ma = Marshmallow(app)



    client = app.app.test_client()

    # response = client.get('/v1.0')
    # print('%s\n%s%s' % (response.status, response.headers, response.data))

    response = client.get('/v1.0/clients')
    print('%s\n%s%s' % (response.status, response.headers, response.data))


    response = client.get('/v1.0/clients/30002')
    print('%s\n%s%s' % (response.status, response.headers, response.data))

    app.run(port=int(environ.get('PORT', 8080)))


if __name__ == '__main__':
    main()
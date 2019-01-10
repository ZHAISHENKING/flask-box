#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import bson.binary
import bson.objectid
import bson.errors
from bson.objectid import ObjectId
from flask import redirect, current_app, Response, send_from_directory
from flask_restful import Resource
from util.common import trueReturn, falseReturn, ms, catch_exception
from .models import Demo
from mongoengine.queryset.visitor import Q


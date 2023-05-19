from flask import Flask, render_template, request, jsonify
from functools import wraps
import bcrypt
import configparser
import io

from . import passwords

app = passwords.create_app()

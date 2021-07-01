# Importing general dependencies/libraries
import pandas as pd
import numpy as np
import datetime as dt

# Import sqlalchemy and related content
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

# Import Flask
import flask
from flask import Flask, jsonify

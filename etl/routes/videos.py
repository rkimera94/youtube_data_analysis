
from urllib import request
from flask import Flask, jsonify, request, Blueprint

from flask_sqlalchemy import SQLAlchemy


from controllers.video_tags import tag_durations

video_tag = Blueprint('video_tag', __name__)


video_tag.route('/tag-avg-duration', methods=['GET'])(tag_durations)

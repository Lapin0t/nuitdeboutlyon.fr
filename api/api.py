import hmac
from os import path
import subprocess

from flask import Flask, request, abort, jsonify
import requests
import yaml


WATCHED_TAGS = ('news', 'compte-rendu')


with open('config.yml') as s:
    config = yaml.load(s)


app = Flask(__name__)


@app.errorhandler(400)
def error_400(err):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(401)
def error_401(err):
    return jsonify({'error': 'Bad signature'}), 401

@app.errorhandler(500)
def error_500(err):
    return jsonify({'error': 'Unknown error'}), 500


@app.route('/v1', methods=['POST'])
def webhook():
    data = request.json

    if not data:
        abort(400)

    sig = hmac.new(bytes(config['secret_key'], 'utf-8'), request.data,
                   'sha256').hexdigest()
    header = request.headers.get('X-Discourse-Event-Signature', '')
    if not (header.startswith('sha256=')
            and hmac.compare_digest(sig, header[7:])):
        abort(401)

    if data['post']['post_number'] != 1:
        return 'Ok'

    t_id = data['topic']['id']
    raw = requests.get(config.discourse_url + '/raw/%i' % t_id).text

    for t in WATCHED_TAGS:
        if t in data['topic']['tags']:
            return HANDLER[t](data, raw)

    return 'Ok'


def handle_news(data, raw):
    meta = get_common_meta(data)


    event_spec, *raw_ = raw.split('\n\n')
    raw = '\n\n'.join(raw_)
    meta.update(yaml.load(event_spec))


    with open(path.join(config.repo_path, 'news', get_filename(meta))):
        for k, v in meta.items():
            s.write('%s: %s\n' % (k.capitalize(), v))
        s.write('\n')
        s.write(raw)

    #TODO: commit the change to the repo

    return 'Ok'


def handle_cr(data, raw):
    meta = get_common_meta(data)

    with open(path.join(config.repo_path, 'news', get_filename(meta))):
        for k, v in meta.items():
            s.write('%s: %s\n' % (k.capitalize(), v))
        s.write('\n')
        s.write(raw)

    #TODO: commit the change to the repo

    return 'Ok'


def get_filename(meta):
    return '%s-%s' % (meta['date'].split(' ')[0], meta['slug'])


def get_common_meta(data):
    meta = {}
    meta['slug'] = data['topic']['slug']
    meta['date'] = fmt_date(data['topic']['created_at'])
    meta['modified'] = fmt_date(data['topic']['modified_at'])
    meta['tags'] = [t for t in data['topic']['tags'] if not t in WATCHED_TAGS]
    meta['authors'] = data['details']['created_by']['username']
    meta['title'] = data['topic']['title']
    return meta

def fmt_date(s):
    return '%s %s' % (s[:10], s[11:16])


HANDLERS = {'news': handle_news, 'compte-rendu': handle_cr}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

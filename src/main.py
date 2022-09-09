import sys
import optparse
import connexion
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from connexion.resolver import RestyResolver


def main():
    default_port = 5000
    default_host = '0.0.0.0'
    parser = optparse.OptionParser()
    msg = 'Hostname of Flask app [{}]'.format(default_host)
    parser.add_option("-H", "--host",
                      help=msg,
                      default=default_host)
    msg = 'Port for Flask app [{}]'.format(default_port)
    parser.add_option("-P", "--port",
                      help=msg,
                      type=int,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    app = connexion.App(__name__, port=options.port, specification_dir='swagger/')
    app.add_api('my_apis.yaml', resolver=RestyResolver('api'))

    flask_app = app.app
    flask_app.wsgi_app = ProxyFix(flask_app.wsgi_app)
    flask_app.config["JSON_SORT_KEYS"] = False              # Keep values on dict sort by created
    flask_app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True  # New line in json result
    flask_app.config['TESTING'] = True

    # region logger
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s  |  %(name)s  |  %(levelname)s  |  %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    # endregion

    return app


app = main()

if __name__ == '__main__':
    app.run()

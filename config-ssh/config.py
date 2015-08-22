# user configuration start

_mode = 'server' # 'server' or 'client'
_password = 'example'
_hostname = 'myserver.com' # 'Common Name' entered in make_key.pem
_host = '1.2.3.4' # ip of your server

# user configuration end
# DO NOT modify any code below

assert _mode in ('server', 'client')

SERVER = dict(
    run = (_mode == 'server'),
    listen = ('0.0.0.0', 443),
    connect = ('127.0.0.1', 22),
    password = _password.encode(),
    certfile = 'cert.pem'
    )

CLIENT = dict(
    run = (_mode == 'client'),
    listen = ('127.0.0.1', 2222),
    connect = (_host, 443),
    password = _password.encode(),
    hostname = _hostname,
    cafile = 'ca.crt'
    )

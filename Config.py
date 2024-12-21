import configparser
import requests
'''初始化信息'''
def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    # 获取默认设置
    server_alive_interval = config.get('DEFAULT', 'ServerAliveInterval')
    compression = config.getboolean('DEFAULT', 'Compression')
    print(f'ServerAliveInterval: {server_alive_interval}')
    print(f'Compression: {compression}')

    # 获取特定部分的设置
    user = config.get('bitbucket.org', 'User')
    port = config.getint('topsecret.server.com', 'Port')
    print(f'User: {user}')
    print(f'Port: {port}')

    ip = config.get('target_ip', 'IP')
    print(f'IP: {ip}')

    return config

def write_config(file_path):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'ServerAliveInterval': '45',
        'Compression': 'yes',
        'CompressionLevel': '9',
        'ForwardX11': 'yes'
    }
    config['bitbucket.org'] = {
        'User': 'hg'
    }
    config['topsecret.server.com'] = {
        'Port': '50022',
        'ForwardX11': 'no'
    }

    with open(file_path, 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    read_config('config.ini')
    # write_config('config.ini')

    # API端点URL
    url = 'https://10.192.62.114:443/v1/cs/auth-service/oauth/token'

    # 自定义头信息
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Authorization': 'Bearer your_token_here',  # 如果需要认证
        'X-HW-ID': 'guanggu__io.cs', # 自定义头信息
        'X-HW-APPKEY': '8-BWqQ!q@92I#3yVN9s2442@-rU1P!VY%$.Wm!0p3X-imcV-GVj7%+98!919667v'
    }

    # 请求体数据
    data = {
        'grant_type': 'client_credentials',
        'scope': 'all',
        'client_id': 'testxj',
        'client_secret': 'testxj'
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data, verify=False)

    # 打印响应状态码和内容
    print(f'Status Code: {response.status_code}')
    print(f'Response Body: {response.text}')


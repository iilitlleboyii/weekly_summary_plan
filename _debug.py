from deepfos.options import OPTION

# ab7e4870-6fa2-4507-aa4b-bda02099c676
# -----------------------------------------------------------------------------
# 从系统中获取以下参数
#: 环境参数
# para1 = {'app': 'xkffcv001', 'space': 'xkffcv', 'user': 'ab7e4870-6fa2-4507-aa4b-bda02099c676', 'language': 'zh-cn', 'token': 'E0C8D31E8C788544457C1916ED3108EB417290795A6678A446EBB438B6BFBA69', 'cookie': 'alpha_deepfos_users=%7B%22color%22%3A%224%22%2C%22email%22%3A%22xianhao.yu%40deepfinance.com%22%2C%22invitationActivation%22%3Atrue%2C%22mobilePhone%22%3A%2217671003464%22%2C%22nickName%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22nickname%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22token%22%3A%22E0C8D31E8C788544457C1916ED3108EB417290795A6678A446EBB438B6BFBA69%22%2C%22tokenKey%22%3A%22alpha_deepfos_token%22%2C%22type%22%3A1%2C%22userId%22%3A%22ab7e4870-6fa2-4507-aa4b-bda02099c676%22%2C%22username%22%3A%22Axian%22%7D; alpha_deepfos_token=E0C8D31E8C788544457C1916ED3108EB417290795A6678A446EBB438B6BFBA69', 'envUrl': 'http://web-gateway'}
para1 = {'app': 'xkffcv001', 'space': 'xkffcv', 'user': 'ab7e4870-6fa2-4507-aa4b-bda02099c676', 'language': 'zh-cn',
         'token': '4DF72E590A1E9448021DDF99A56AFF130C46B432E9AF5B8F4FA0433E1E4FCFA4',
         'cookie': 'cloud_deepfos_token=98DE97A98C001D8F4166F0DDA27C6E9844BBD7D804D9B122FA481782A31A6B8A; cloud_deepfos_users=%7B%22color%22%3A%224%22%2C%22email%22%3A%22xianhao.yu%40deepfinance.com%22%2C%22invitationActivation%22%3Atrue%2C%22mobilePhone%22%3A%2217671003464%22%2C%22nickName%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22nickname%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22token%22%3A%2298DE97A98C001D8F4166F0DDA27C6E9844BBD7D804D9B122FA481782A31A6B8A%22%2C%22tokenKey%22%3A%22cloud_deepfos_token%22%2C%22type%22%3A1%2C%22userId%22%3A%228001ce0d-7b0c-404f-b29e-b7eb5c6812f6%22%2C%22username%22%3A%22yuxianhao%22%7D; alpha_deepfos_users=%7B%22color%22%3A%224%22%2C%22email%22%3A%22xianhao.yu%40deepfinance.com%22%2C%22invitationActivation%22%3Atrue%2C%22mobilePhone%22%3A%2217671003464%22%2C%22nickName%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22nickname%22%3A%22%E4%BD%99%E5%85%88%E6%B5%A9%22%2C%22token%22%3A%224DF72E590A1E9448021DDF99A56AFF130C46B432E9AF5B8F4FA0433E1E4FCFA4%22%2C%22tokenKey%22%3A%22alpha_deepfos_token%22%2C%22type%22%3A1%2C%22userId%22%3A%22ab7e4870-6fa2-4507-aa4b-bda02099c676%22%2C%22username%22%3A%22Axian%22%7D; alpha_deepfos_token=4DF72E590A1E9448021DDF99A56AFF130C46B432E9AF5B8F4FA0433E1E4FCFA4',
         'envUrl': 'http://web-gateway'}
#: 业务参数
para2 = [{'Entity1': None, 'year': '2025', 'period': '1w01'}]
# para2 = [{'record_id': '158c60a21fac11edbc550a76748fe6fa'}, {'record_id': '158e5a561fac11edbc550a76748fe6fa'}]

#: 环境域名，根据自己的使用环境更改
host = "https://alpha.deepfos.com"

# -----------------------------------------------------------------------------
# 下面的代码是固定的

OPTION.general.use_eureka = False
OPTION.server.base = f"{host}/seepln-server"
OPTION.server.app = f"{host}/seepln-server/app-server"
OPTION.server.system = f"{host}/seepln-server/system-server"
OPTION.server.space = f"{host}/seepln-server/space-server"
OPTION.server.platform_file = f"{host}/seepln-server/platform-file-server"
OPTION.api.header = para1
OPTION.api.dump_on_failure = True

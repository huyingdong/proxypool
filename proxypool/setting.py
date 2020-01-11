# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 5
MIN_SCORE = 0
AVAILABLE_MIN_SCORE = 4
INITIAL_SCORE = 2

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

# 检查周期
TESTER_CYCLE = 3000
# 获取周期
GETTER_CYCLE = 6000

# 测试API，建议抓哪个网站测哪个
TEST_URLs = [
    'https://www.baidu.com/',
    'https://www.sogou.com/',
]

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

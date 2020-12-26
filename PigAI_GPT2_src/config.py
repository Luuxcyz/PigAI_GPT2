import sys
import pytz
from os.path import join, dirname
from environs import Env
from loguru import logger

env = Env()
env.read_env()
"""
======================== ʕ•ﻌ•ʔ ========================
(·▽·)欢迎使用PigAI，请跟随提示合理配置项目启动参数
======================== ʕ•ﻌ•ʔ ========================
"""
# (√) 强制填写；(*)可选项
# ---------------------------------------------------
# TODO (√)TexLen -- 文本词数区间起点
# 合成的文章词数不会小于TexLen，一般情况下会超出20至80个词。
# 建议区间 TEXT_LENGTH∈[120, 460]
# ---------------------------------------------------
TEXT_LENGTH = 320

# ---------------------------------------------------
# TODO (√)CHROMEDRIVER_PATH -- ChromeDriver的路径
# 1.本项目内置的ChromeDriver可能与您的Chrome版本不适配。若您发现内置的ChromeDriver不能驱动项目，请根据下方提供的链接下载对应版本的文件
# 推荐`driver随chrome`，既根据现用的Chrome版本找对应的driver而不是对Chrome随意地升降版本(特别是linux环境)
# >> http://npm.taobao.org/mirrors/chromedriver/

# 2.本项目内置了Linux版本和Windows版本的ChromeDriver；显然您需要根据具体的部署环境下载相应的ChromeDriver
# 并将下载好的文件替换掉`./PigAI_GPT2_src/middleware/` 下的`chromedriver.exe`或`chromedriver`

# 3.本项目基于Windows10环境开发，Linux环境测试，可正常运行
# 若您的系统基于MacOS或其他，~可能~无法正常运行本项目
# ---------------------------------------------------

"""
========================== ʕ•ﻌ•ʔ ==========================
如果您并非<PigAI>项目开发者 请勿修改以下变量的默认参数
========================== ʕ•ﻌ•ʔ ==========================

                                  Enjoy it -> ♂main.py
"""
# ---------------------------------------------------
# 服务器工程目录,基于Windows10
# ---------------------------------------------------

# 工程根目录::Windows10写法
ROOT_DIR_PROJECT = dirname(__file__)

# 用户信息配置文件
ROOT_PATH_YAML_CONFIG = join(ROOT_DIR_PROJECT, 'config.yaml')

# 插件目录
ROOT_DIR_MIDDLEWARE = join(ROOT_DIR_PROJECT, 'middleware')

# 模型路径
ROOT_PATH_MODEL_GPT2 = join(ROOT_DIR_MIDDLEWARE, 'gpt2.model')

# chromedriver 路径
if 'win' in sys.platform:
    CHROMEDRIVER_PATH = join(ROOT_DIR_MIDDLEWARE, 'chromedriver.exe')
elif 'linux' in sys.platform:
    CHROMEDRIVER_PATH = join(ROOT_DIR_MIDDLEWARE, 'chromedriver')

# 数据文件路径
ROOT_DIR_DATABASE = join(ROOT_DIR_PROJECT, 'dataBase')

# 操作历史
ROOT_PATH_ACTION_HISTORY = join(ROOT_DIR_DATABASE, 'action_history.csv')

# 提交结果持久化目录（用于存放.mhtml文件）
ROOT_DIR_PAPER_SCORE = join(ROOT_DIR_DATABASE, 'paper_score')

# 替代方案: 语料集
ROOT_DIR_FAKE_CORPUS = join(ROOT_DIR_DATABASE, 'fake_corpus')
ROOT_PATH_FAKE_CORPUS = join(ROOT_DIR_FAKE_CORPUS, 'Beyond Good and Evil.txt')

# 日志路径
ROOT_DIR_LOGS = join(ROOT_DIR_DATABASE, 'logs')
logger.add(
    env.str("LOG_RUNTIME_FILE", join(ROOT_DIR_LOGS, "runtime.log")),
    level="DEBUG",
    rotation="1 week",
    retention="20 days",
    encoding="utf8",
)
logger.add(
    env.str("LOG_ERROR_FILE", join(ROOT_DIR_LOGS, "error.log")),
    level="ERROR",
    rotation="1 week",
    encoding="utf8",
)
# ---------------------------------------------------
# Engine params.Don't change.
# ::Linux Google Chrome v85.0.4183.102
# ---------------------------------------------------
SILENCE = True if 'linux' in sys.platform else False  # 静默启动：windows环境下默认为False
DEBUG = False  # 此项目不允许开启DEBUG模式
ANTI = True  # 目标网站是否包含高强度反爬虫系统：此项目下必须为True
TIMEZONE_CN = pytz.timezone('Asia/Shanghai')  # 设置时区

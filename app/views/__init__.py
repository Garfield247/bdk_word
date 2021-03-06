# -*- coding: utf-8 -*-
from .main import main


# 蓝本配置
DEFAULT_BLUEPRINT = (
    # 蓝本，前缀
    (main, ''),
)



# 封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)

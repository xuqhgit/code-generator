
from web.util import config_util,template_util,file_util

from web.service.strategy import  strategy_map
import  json

class Generator(object):
    """
    代码构建
    """

    def generate(self,input_data):
        """
        :param input_data: 前端表单数据
        :return:
        """
        code = input_data['code']
        config, config_ext = config_util.get_extend_config_json(code)
        input_handle_strategy_name = config["generate"]["input_handle_strategy"]
        strategy_data = None
        # 数据处理策略
        if bool(input_handle_strategy_name) and input_handle_strategy_name in strategy_map:
            strategy_data = strategy_map[input_handle_strategy_name]["object"].handle(input_data, config)
        # 账户信息
        account_info = {"account": input_data['account']}
        context = {"user": account_info, "config": config, "strategyData": strategy_data}
        # 获取数据模板 用模板构建出数据
        parent_module_code =  config_util.get_parent_module_code_arr(config,code)
        format_data = template_util.render_data_template_by_modules(parent_module_code, context)
        # 数据 =
        format_data = json.loads(format_data)
        # 最后生成代码
        # parent_module = config["generate"]["parent_module"]
        template_list = input_data.get("templates")
        account = account_info.get("account")
        file_util.clear_workplace_file(code,account)
        for t in template_list:
            template_name = t.get("templateName")
            template_info = config.get("templates").get(template_name)
            try:
                if template_info.get("type") == "all":
                    content = template_util.render_template(t["moduleCode"], template_name, {"list":format_data})
                    path = template_util.render_str(template_info["path"], context)
                    file_type = template_name.split(".")[1]
                    file_name = template_util.render_str(template_info["fileName"], context)
                    file_util.write_workplace_file(code,path, content, file_name, file_type, account)
                else:
                    for td in format_data:
                        content = template_util.render_template(t["moduleCode"], template_name, td)
                        path = template_util.render_str(template_info["path"], td)
                        file_type = template_name.split(".")[1]
                        file_name = template_util.render_str(template_info["fileName"], td)
                        file_util.write_workplace_file(code, path, content, file_name, file_type, account)
            except Exception as e:
                print("%s:%s e:%s" % (t["moduleCode"],template_name,e))







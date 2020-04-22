
import web
import os
import zipfile

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


def edit_file_content(path,file_name,content):
    file_object = open('%s/%s/%s' % (web.template_module,path, file_name), 'w', encoding='utf8')
    file_object.write(content)

def write_workplace_file(module_code,path,content,file_name,file_type,account):
    """

    :param module_code:
    :param path:
    :param content:
    :param file_name:
    :param file_type:
    :param account:
    :return:
    """
    if account is None:
        raise Exception("account info  None")
    path = '%s/%s/%s/file/%s' % (web.workplace,account,module_code.replace("/","_"), path.replace(".", "/"))
    mkdir(path)
    file_object = open('%s/%s.%s' % (path, file_name, file_type), 'w', encoding='utf8')
    file_object.write(content)
    file_object.close()

def clear_workplace_file(module_code,account):
    """

    :param module_code:
    :param path:
    :param content:
    :param file_name:
    :param file_type:
    :param account:
    :return:
    """
    path = '%s/%s/%s' % (web.workplace, account, module_code.replace("/", "_"))
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))






def create_zip(module_code,account):
    root_path = '%s/%s/%s' % ( web.workplace,account,module_code.replace("/","_"))
    start_dir = '%s/file' % root_path
    new_file = '%s/%s.zip' % (root_path, account)
    z = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_name in os.walk(start_dir):
        path = dir_path.replace(start_dir, '')
        path = path and path + os.sep or ''
        for f in file_name:
            z.write(os.path.join(dir_path, f), path + f)
    z.close()
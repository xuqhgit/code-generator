
import web
import os
import zipfile
import datetime

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


def edit_file_content(path,file_name,content):
    file_object = open('%s/%s/%s' % (web.template_module_dir,path, file_name), 'w', encoding='utf8')
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
    path = '%s/%s/file/%s/%s' % (web.workspace_dir,account,module_code.replace("/","_"), path.replace(".", "/"))
    mkdir(path)
    file_object = open('%s/%s.%s' % (path, file_name, file_type), 'w', encoding='utf8')
    file_object.write(content)
    file_object.close()

def clear_workplace_file(module_code,account):
    """

    :param module_code:
    :param account:
    :return:
    """
    path = '%s/%s/file/%s' % (web.workspace_dir, account, module_code.replace("/", "_"))
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def create_zip(module_code,account):
    root_path = '%s/%s/file/%s' % ( web.workspace_dir,account,module_code.replace("/","_"))
    zip_path = get_zip_path(account)
    new_file_path = '%s/%s.zip' % (zip_path,"%s$%s" % (module_code.replace("/","_"),datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    mkdir(zip_path)
    z = zipfile.ZipFile(new_file_path, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_name in os.walk(root_path):
        path = dir_path.replace(root_path, '')
        path = path and path + os.sep or ''
        for f in file_name:
            z.write(os.path.join(dir_path, f), path + f)
    z.close()
    del_other_zip(account)
    return new_file_path


def get_user_zip(account):
    zip_dir = get_zip_path(account)
    relative_path = "%s/%s/zip" % (web.static_workspace,account)
    zip_arr=[]
    for dir_path, dir_name, file_name in os.walk(zip_dir):
        for name in file_name:
            arr = name.split(".")
            if len(arr)!=2 or arr[1].upper()!='ZIP':
                continue
            zip_arr.append([relative_path,name])
    new_zip_arr = sorted(zip_arr, key=lambda k:k[1].split("$")[1])
    new_zip_arr.reverse()
    return new_zip_arr

def del_other_zip(account):
    zip_dir = get_zip_path(account)
    zip_arr = []
    for dir_path, dir_name, file_name in os.walk(zip_dir):
        for name in file_name:
            arr = name.split(".")
            if len(arr) != 2 or arr[1].upper() != 'ZIP':
                continue
            zip_arr.append(name)
    new_zip_arr = sorted(zip_arr, key=lambda k: k.split("$")[1])
    if bool(new_zip_arr) and len(new_zip_arr) > 5:
            new_zip_arr.reverse()
            for i in range(5, len(new_zip_arr)):
                os.remove(os.path.join(zip_dir, new_zip_arr[i]))


def get_zip_path(account):
    return "%s/%s/zip" % (web.workspace_dir, account)

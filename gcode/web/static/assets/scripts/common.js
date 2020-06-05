/**
 * 避免和jinja2模板冲突 所以js模板边界符由原来{{}} 改成 {[ ]}
 * @type {RegExp}
 */
template.defaults.rules[1].test = /{\[([@#]?)[ \t]*(\/?)([\w\W]*?)[ \t]*\]}/;

/**
 * 判断是否有小写字母
 * @param str
 * @returns {boolean}
 */
function isLower(str) {
    for (var i = 0; i < str.length; i++) {
        var c = str.charAt(i);
        if (c >= 'a' && c <= 'z')
            return true;
    }
    return false;
}
/**
 * 将字符串转成驼峰命名
 * 例如：sys_user_info -> userInfo
 * @param str
 * @param prefix 前缀处理
 * @param connector 连接符
 * @returns {*}
 */
function convertCamelCase(str, prefix, connector) {
    var _str = str;
    if (prefix != undefined) {
        var _prefix;
        if ((typeof prefix == 'object') && prefix.constructor == Array) {
            for (var i = 0; i < prefix.length; i++) {
                if (_str.indexOf(prefix[i]) == 0) {
                    _prefix = prefix[i];
                    break
                }
            }
        }
        else {
            _prefix = prefix;
        }
        if (_prefix != undefined) {
            _str = _str.replace(_prefix, "")
        }
    }
    if (!isLower(str)) {
        _str = _str.toLowerCase();
    }
    if (connector != undefined && _str.indexOf(connector) > -1) {
        var flag = false;
        var field = '';
        for (var i = 0; i < _str.length; i++) {
            var c = _str.charAt(i);
            if (c == connector && i < _str.length)
                flag = true;
            else {
                field = field + (flag ? c.toUpperCase() : c);
                flag = false;
            }
        }
        _str = field;

    }
    return _str;
}


function initialUpper(str){
    return str.charAt(0).toUpperCase() + str.slice(1)
}

$.fn.serializeObject = function () {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function () {
        if (o[this.name]) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};
var $frame = {};
var $app = {};


$app.cacheSave = function (key, val) {
    if (val instanceof Array) {
        localStorage.setItem(key, JSON.stringify(val));
    }
    if (typeof(val) == "object") {
        localStorage.setItem(key, JSON.stringify(val));
    }
    else {
        localStorage.setItem(key, val);
    }
};
$app.cacheGet = function (key, type) {
    var s = localStorage.getItem(key);
    if (s) {
        if (type == "json") {
            return JSON.parse(s);
        }
    }
    return s;
};
$app.cacheRemove = function (key) {
    localStorage.removeItem(key);
};
toastr.options = {
  "closeButton": false,
  "debug": false,
  "positionClass": "toast-top-right",
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};
$app.alert = function (data,message,title) {
    if(data.code==0){
        $app.errorAlert(message!=undefined?message:data.message,title);
        return
    }
    if(data.code==1){
        $app.successAlert(message!=undefined?message:data.message,title);
        return
    }
    $app.infoAlert(message!=undefined?message:data.message,title);
};

$app.successAlert = function (message,title) {
    toastr['success'](message, title)
};

$app.errorAlert = function (message,title) {
    toastr['error'](message, title)
};

$app.infoAlert = function (message,title) {
    toastr['info'](message, title)
};
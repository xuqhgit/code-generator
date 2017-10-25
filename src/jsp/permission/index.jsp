
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="shiro" uri="http://shiro.apache.org/tags" %>
<html>
<head>
    <title>管理</title>
    <%@include file="../../common.jsp" %>
</head>
<body>


<div class="container-fluid ">
    <h3>列表</h3>

    <div class="row-fluid ">
        <div class="span12 search-form">
            <form id="form" class="form-horizontal" role="form">
                <div class="form-group">
                
                    <label class="col-sm-1 control-label" for="code">权限编码：</label>
                    <div class="col-sm-2">
                        <input class="form-control" id="code" name="code" type="text" placeholder="权限编码"/>
                    </div>
                            
                    <div class="col-sm-1">
                            <button type="button" class="btn btn-primary" id="search"
                                    data-toggle="button"><span class="glyphicon glyphicon-search"></span>搜索
                            </button>
                    </div>
                </div>
            </form>
        </div>
        <div class="span12">
            <div id="toolbar" class="btn-group">
                <shiro:hasPermission name=":add:index">
                    <a role="button" id="addPermission" class="btn btn-default">
                        <i class="glyphicon glyphicon-plus"></i>添加
                    </a>
                </shiro:hasPermission>

                <shiro:hasPermission name=":deleteBatch">
                    <a href="#addPermissionModal" role="button" class="btn btn-default" id="deleteBatchButton">
                        <i class="glyphicon glyphicon-trash"></i>批量删除
                    </a>
                </shiro:hasPermission>
            </div>
            <table id="permissionTable"></table>
        </div>
    </div>
</div>





<%@include file="../../common_script.jsp" %>
<script>

    var bt;
    var permissionValidConfig={
    
        code:{
            rule:{
                required:True,
                codeValid:true 
            },
            message:{
                required:'必填项'
            }
        },
    };
    $(function () {
    
    jQuery.validator.addMethod("codeValid", function(value,element) {
        var p = /^[a-zA-Z0-9_-]{4,16}$/;
        return p.test(value);
    }, "请输入格式为:字母、数字、下划线、减号、冒号，1至32位字符");

    var params = {
            url: '/permission/grid',
            queryParams: function (params) {
                var temp = {
                    pageSize: params.limit,   //页面大小
                    pageNum: params.offset / params.limit + 1,  //页码
                    sort: params.sort,  //排序列名
                    sortOrder: params.order//排位命令（desc，asc）
                };
                return $.extend(temp, $('#form').serializeObject());
            },
            columns: [
                {checkbox: true},
                 
                {title: '权限编码', field: 'code', align: 'center', width: '100'},
                
                {title: '', field: 'createTime', align: 'center', width: '100'},
                
                {title: '', field: 'creatorId', align: 'center', width: '100'},
                
                {title: '', field: 'icon', align: 'center', width: '100'},
                
                {title: '', field: 'id', align: 'center', width: '100'},
                
                {title: '', field: 'name', align: 'center', width: '100'},
                
                {title: '', field: 'pid', align: 'center', width: '100'},
                
                {title: '', field: 'rank', align: 'center', width: '100'},
                
                {title: '', field: 'state', align: 'center', width: '100'},
                
                {title: '', field: 'type', align: 'center', width: '100'},
                
                {title: '', field: 'updateTime', align: 'center', width: '100'},
                
                {title: '', field: 'url', align: 'center', width: '100'},
                
                {
                    title: '操作', field: 'opt', align: 'center', width: '120', formatter: function (index, row) {
                    var opts = "";
                    <shiro:hasPermission name=":get">
                        opts += "<a href='javascript:void(0);' class='btn btn-xs' onclick=\"detailPermission(\'" + row.id + "\')\">查看</a>|";
                    </shiro:hasPermission>
                    <shiro:hasPermission name=":edit:index">
                        opts += "<a href='javascript:void(0);' class='btn btn-xs' onclick=\"editPermission(\'" + row.id + "\')\">编辑</a>|";
                    </shiro:hasPermission>
                    <shiro:hasPermission name=":delete">
                        opts += "<a href='javascript:void(0);' class='btn btn-xs' onclick=\"deletePermission(\'" + row.id + "\')\">删除</a>";
                    </shiro:hasPermission>
                    return opts;
                }
                }
            ]
        };
        bt = anchor.bootstrapTable("permissionTable", params);
        $('#search').click(function () {
            bt.bootstrapTable('refresh');
        });
        //回车事件绑定
        document.onkeydown = function (event) {
            var e = event || window.event || arguments.callee.caller.arguments[0];
            if (e && e.keyCode == 13) {
                $('#search').click();
            }
        };

        $('#addPermission').click(function () {
            var addFormId = "addPermissionForm";
            var addDialog = $.dialog({
                title: '',
                content: 'url:/permission/add',
                columnClass:'medium',
                onContentReady:function(){
                    var validateConfig =anchor.validFieldConfig(permissionValidConfig,anchor.formField(addFormId));
                    validateConfig['id']= addFormId;
                    var valid = anchor.validate(validateConfig);
                    $('#savePermission').click(function () {
                        if(valid.form()){
                            <shiro:hasPermission name="auth:permission:add">
                                anchor.request("/permission/add", $('#'+addFormId).serializeObject(), function (data) {
                                if(data.code==1){
                                    bt.bootstrapTable('refresh');
                                    anchor.alert("保存成功");
                                    addDialog.close();
                                }
                                else{
                                    anchor.alert(data.message);
                                }
                            }, null);
                            </shiro:hasPermission>

                        }
                    });
                }

            });
        });

        /**
         * 批量删除操作
         *
         */
        $('#deleteBatchButton').click(function () {

            var ids = $.map(bt.bootstrapTable('getSelections'), function (row) {
                return row.id;
            });
            if (ids.length == 0) {
                anchor.alert("请选择删除数据");
                return;
            }
            anchor.confirm("确定要删除【" + ids.length + "】条数据么？", function () {
                anchor.request("/permission/deleteBatch", {ids: ids}, function (data) {
                    bt.bootstrapTable('refresh');
                }, null);
            });

        });

    });
    /**
     * 详情
     */
    function detailPermission(permissionId) {
        $.dialog({
            title: '',
            content: 'url:/permission/edit/'+permissionId,
            type:'blue',
            columnClass:'medium',
            onContentReady:function(){

            }
        });
    }
    /**
     * 删除
     */
    function deletePermission(permissionId) {
        anchor.confirm("确认要删除该用户么?", function () {
            anchor.request("/permission/delete/"+permissionId, {}, function (data) {
                anchor.alert(data.message);
                bt.bootstrapTable('refresh');
            }, null);
        });
    }
    /**
     * 编辑
     */
    function editPermission(permissionId) {
        var editFormId = "editPermissionForm";
        var dialog = $.dialog({
            title: '',
            content: 'url:/permission/edit/'+permissionId,
            columnClass:'medium',
            onContentReady:function(){
                var validateConfig =anchor.validFieldConfig(permissionValidConfig,anchor.formField(editFormId));
                validateConfig['id']= editFormId;
                var valid = anchor.validate(validateConfig);
                $('#editPermission').click(function () {
                    if(valid.form()){
                        anchor.request("/permission/edit", $('#'+editFormId).serializeObject(), function (data) {
                            bt.bootstrapTable('refresh');
                            anchor.alert("保存成功");
                            dialog.close();
                        }, null);
                    }
                });
            }
        });
    }
</script>
</body>
</html>
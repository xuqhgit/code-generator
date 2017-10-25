<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<div class="form-dialog">
    <div class="box box-info">
        <div class="box-header ">
            <h3 class="box-title">新增</h3>
        </div>
        <form id="addPermissionForm" class="form-horizontal" role="form">

            <div class="box-body">
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">权限编码：</label>
                    <div class="col-sm-9">
                        <input type="text" name="code" class="form-control" placeholder="请输入格式为:字母、数字、下划线、减号、冒号，1至32位字符">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="createTime" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="creatorId" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="icon" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="id" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="name" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="pid" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="rank" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="state" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="type" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="updateTime" class="form-control" placeholder="">
                    </div>
                </div>
                
                
                <div class="form-group">
                    <label class="col-sm-3 control-label">：</label>
                    <div class="col-sm-9">
                        <input type="text" name="url" class="form-control" placeholder="">
                    </div>
                </div>
                
                
            </div>
            <div class="box-footer">
                <%--<button type="submit" class="btn btn-default">Cancel</button>--%>
                <a id="savePermission" class="btn btn-info pull-right">保存</a>
            </div>
        </form>
    </div>
</div>


package com.anchor.ms.auth.model;


import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;

/**
 * @ClassName: Permission
 * @Description: 
 * @author xuqh
 * @date 2017-10-25 19:01:02
 * @since version 1.0WW
 */
public class Permission extends BaseModel{
    public static final String CODE_PATTERN = "^[a-zA-Z0-9_-]{4,16}$";
    public static final String CODE_PATTERN_MESSAGE = "请输入格式为:字母、数字、下划线、减号、冒号，1至32位字符";
    public static final String CODE_REQUIRED_MESSAGE = "必填项";
    public static final String CREATE_TIME_REQUIRED_MESSAGE = "必填项";
    public static final String CREATOR_ID_REQUIRED_MESSAGE = "必填项";
    public static final String ICON_REQUIRED_MESSAGE = "必填项";
    public static final String ID_REQUIRED_MESSAGE = "必填项";
    public static final String NAME_REQUIRED_MESSAGE = "必填项";
    public static final String PID_REQUIRED_MESSAGE = "必填项";
    public static final String RANK_REQUIRED_MESSAGE = "必填项";
    public static final String STATE_REQUIRED_MESSAGE = "必填项";
    public static final String TYPE_REQUIRED_MESSAGE = "必填项";
    public static final String UPDATE_TIME_REQUIRED_MESSAGE = "必填项";
    public static final String URL_REQUIRED_MESSAGE = "必填项";

    
    /**
     * 权限编码
     */
    @NotNull@Pattern(regexp=CODE_PATTERN,message=CODE_PATTERN_MESSAGE)
    private String code;
    /**
     * 创建者ID
     */
    
    private String creatorId;
    /**
     * 图标
     */
    
    private String icon;
    /**
     * 权限名称
     */
    
    private String name;
    /**
     * 权限父ID
     */
    
    private Long pid;
    /**
     * 排序 默认为1
     */
    
    private String rank;
    /**
     * 权限状态 0 无效 1有效
     */
    
    private String state;
    /**
     * 权限类型 0 为菜单 1 为功能
     */
    
    private String type;
    /**
     * 权限路径
     */
    
    private String url;
    public void setCode(String code){
        this.code = code;
    }
    public String getCode(){
        return this.code;
    }
    public void setCreatorId(String creatorId){
        this.creatorId = creatorId;
    }
    public String getCreatorId(){
        return this.creatorId;
    }
    public void setIcon(String icon){
        this.icon = icon;
    }
    public String getIcon(){
        return this.icon;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setPid(Long pid){
        this.pid = pid;
    }
    public Long getPid(){
        return this.pid;
    }
    public void setRank(String rank){
        this.rank = rank;
    }
    public String getRank(){
        return this.rank;
    }
    public void setState(String state){
        this.state = state;
    }
    public String getState(){
        return this.state;
    }
    public void setType(String type){
        this.type = type;
    }
    public String getType(){
        return this.type;
    }
    public void setUrl(String url){
        this.url = url;
    }
    public String getUrl(){
        return this.url;
    }
}
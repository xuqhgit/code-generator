package com.sf.pass.data.platform.model.route2;

import com.sf.pass.data.platform.annotation.CSVColumn;
import com.sf.pass.data.platform.annotation.Cvs;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import java.io.Serializable;

/**
 * @Description: 报表
 * @author 000001
 * @date 
 */
@Cvs
@Setter
@Getter
public class TestVo  implements Serializable {

    private static final long serialVersionUID = -5841686246151023617L;
    private long id;


    
    
    /**
     * 
     */
    @ApiModelProperty(value = "")
    @CSVColumn(name = "",index = -1)
    private String characterSetName;
    
    /**
     * 
     */
    @ApiModelProperty(value = "")
    @CSVColumn(name = "",index = 0)
    private String defaultCollateName;
    
    /**
     * 
     */
    @ApiModelProperty(value = "")
    @CSVColumn(name = "",index = 1)
    private String description;
    
    /**
     * 
     */
    @ApiModelProperty(value = "")
    @CSVColumn(name = "",index = 2)
    private Long maxlen;


}
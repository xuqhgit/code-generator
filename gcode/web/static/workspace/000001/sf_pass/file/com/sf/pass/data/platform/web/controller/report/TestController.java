package com.sf.pass.data.platform.controller.report.route2;

import com.sf.idsp.common.base.BaseResponse;
import com.sf.pass.data.platform.model.BaseResponseList;
import com.sf.pass.data.platform.model.ReportEnum;
import com.sf.pass.data.platform.model.route2.TestQuery;
import com.sf.pass.data.platform.model.route2.TestVo;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import javax.ws.rs.core.MediaType;

/**
 * @Description: 
 * @author 000001
 * @date 
 */
@RequestMapping("/opdp/data")
@RestController
@Slf4j
@Api(value = "TestController",tags = "")
public class TestController extends ReportBaseController<TestVo, TestQuery> {


    @PostMapping(value = "/queryTestRpt", produces = MediaType.APPLICATION_JSON)
    @ApiOperation(value = "查询报表", notes = "查询报表")
    @ResponseBody
    @Override
    public BaseResponse<BaseResponseList<TestVo>> queryReport(@RequestBody TestQuery params) throws Exception {
        params = validateSrcCodePremission(params);
        return queryList(params);
    }

    @PostMapping(value = "/exportTestRpt", produces = MediaType.APPLICATION_JSON)
    @ApiOperation(value = "导出报表", notes = "导出报表")
    @ResponseBody
    @Override
    public BaseResponse<Integer> exportReport(@RequestBody TestQuery params) {
        params = validateSrcCodePremission(params);
        return exportToCsv(params);
    }

    @Override
    public ReportEnum getReportEnum() {
        return ReportEnum.CHARACTER_SETS_REPORT;
    }

    @Override
    public String getName() {
        return ReportEnum.CHARACTER_SETS_REPORT.getReportName();
    }
}
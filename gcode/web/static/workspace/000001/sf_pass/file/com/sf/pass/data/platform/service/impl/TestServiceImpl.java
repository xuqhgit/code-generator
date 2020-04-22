package com.sf.pass.data.platform.service.impl;

import com.alibaba.fastjson.JSON;
import com.github.pagehelper.Page;
import com.sf.pass.data.platform.manager.route.ReportManager;
import com.sf.pass.data.platform.model.ReportEnum;
import com.sf.pass.data.platform.model.route2.TestQuery;
import com.sf.pass.data.platform.model.route2.TestVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;
/**
 * @Description: 报表-serviceImpl
 * @author 000001
 * @date 
 */
@Service("testServiceImpl")
public class TestServiceImpl extends AbstractMysqlReportService<TestVo, TestQuery> {

    @Autowired
    @Qualifier("testManagerImpl")
    private ReportManager<TestVo, TestQuery> manager;

    @Override
    Page<TestVo> getData(TestQuery params) {
        return (Page<TestVo>) manager.selectList(params);
    }

    @Override
    int getTotalRows(TestQuery params) {
        return manager.count(params);
    }

    @Override
    String toQueryString(TestQuery params) {
        return JSON.toJSONString(params);
    }

    @Override
    ReportEnum getReportEnum() {
        return ReportEnum.CHARACTER_SETS_REPORT;
    }

    @Override
    public String getName() {
        return "";
    }
}
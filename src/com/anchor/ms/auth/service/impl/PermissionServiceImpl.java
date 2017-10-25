package com.anchor.ms.auth.service.impl;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;

import com.anchor.ms.auth.mapper.PermissionMapper;
import com.anchor.ms.auth.model.Permission;

/**
 * @ClassName: PermissionServiceImpl
 * @Description: 
 * @author xuqh
 * @date 2017-10-25 19:01:02
 * @since version 1.0
 */
@Service
public class PermissionServiceImpl extends BaseServiceImpl<Permission> implements IPermissionService{

	@Autowired
	private PermissionMapper permissionMapper;


}
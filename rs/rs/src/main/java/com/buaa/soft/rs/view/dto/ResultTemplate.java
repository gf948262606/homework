package com.buaa.soft.rs.view.dto;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Copyright (c) 2017-2018 All Rights Reserved.
 * @Description: TODO
 * @author garfield
 * @email wangjian@sunlands.com 
 * @date 2018年6月6日 上午11:54:49
 */
public class ResultTemplate {
	private static final String SUCCESS_FLAG = "1";
	private static final String ERROR_FLAG = "0";

	public static Map<String, Object> getSuccessResultTemplate(Object data, String message) {
		Map<String, Object> rs = new HashMap<String, Object>();
		rs.put("data", data);
		rs.put("flag", SUCCESS_FLAG);
		rs.put("error", message);
		return rs;
	}

	public static Map<String, Object> getFailResultTemplate(Map data, String message) {
		Map<String, Object> rs = new HashMap<String, Object>();
		rs.put("data", data);
		rs.put("flag", ERROR_FLAG);
		rs.put("error", message);
		return rs;
	}
	
	public static Map<String, Object> getResultTemplate(List data,String code, String message) {
		Map<String, Object> rs = new HashMap<String, Object>();
		rs.put("code", code);
		rs.put("message", message);
		rs.put("data", data);
		return rs;
	}
	

}
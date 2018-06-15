package com.buaa.soft.rs.dto;

import java.util.List;
import java.util.Map;

public class RecommendReturnDTO {
	/** 变量描述：用户在系统中的id. */
	private int flag;

	/** 变量描述：抓取到的用户标签信息集合. */
	private String message;

	private List<Map<String, String>> data;

	public int getFlag() {
		return flag;
	}

	public void setFlag(int flag) {
		this.flag = flag;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public List<Map<String, String>> getData() {
		return data;
	}

	public void setData(List<Map<String, String>> data) {
		this.data = data;
	}

}

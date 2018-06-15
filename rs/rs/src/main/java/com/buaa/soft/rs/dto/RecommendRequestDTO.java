package com.buaa.soft.rs.dto;

/**
 * 功能描述：入参 . <BR>
 * 历史版本: <Br>
 * 开发者: garfield <BR>
 * 时间：2018年06月06日 上午11:47:59 <BR>
 * 变更原因： <BR>
 * 变化内容 ：<BR>
 * 首次开发时间：2018年06月06日 上午11:47:59 <BR>
 * 描述： <BR>
 * 版本：V1.0
 */

public class RecommendRequestDTO {
	/** 变量描述：用户在系统中的id. */
	private long stuId;

	/** 变量描述：抓取到的用户标签信息集合. */
	private String tagSet;

	public long getStuId() {
		return stuId;
	}

	public void setStuId(long stuId) {
		this.stuId = stuId;
	}

	public String getTagSet() {
		return tagSet;
	}

	public void setTagSet(String tags) {
		this.tagSet = tags;
	}
}

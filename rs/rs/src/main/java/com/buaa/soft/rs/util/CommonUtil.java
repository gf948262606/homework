package com.buaa.soft.rs.util;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Properties;



public class CommonUtil {

	/**
	 * 加载配置文件
	 * 
	 * @return
	 */
	public static Properties loadConfig(String propertyName) {

		Properties props = new Properties();
		try {
			props.load(CommonUtil.class.getResourceAsStream("/" + propertyName));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return props;
	}
	/**
	 * 判读str是否为null
	 * @return
	 */
	public static boolean strIsNull(String str){
		
		boolean flag = false;
		if(str == null){
			flag = true;
		}else if(str.trim().length() ==0){
			flag = true;
		}else if("null".equals(str.trim())){
			flag = true;
		}
		return flag;
	}
	/**
	 * 指标参数获取
	 * @param propertyName 配置文件名称
	 * @param paramName	参数名称
	 * @return
	 */
	public static String getParamValue(String propertyName,String paramName){
		String paramValue = "";
		Properties prop = loadConfig(propertyName);
		paramValue = prop.getProperty(paramName);
		return paramValue;
	}
	/**
	 * str转list
	 * @return
	 */
	public static List<String> strToList(String str){
		List<String> strList = null;
		if(!strIsNull(str)){
			strList = new ArrayList<String>();
			String[] strArr = str.split(",");
			for(int i=0; i<strArr.length; i++){
				strList.add(strArr[i]);
			}
		}
		return strList;
	}
	/** 
	 * 随机指定范围内N个不重复的数 
	 * 最简单最基本的方法 
	 * @param min 指定范围最小值 
	 * @param max 指定范围最大值 
	 * @param n 随机数个数 
	 */  
	public static int[] randomIntegers(int min, int max, int n){  
	    if (n > (max - min) || max < min|| n<=0) {  
	           return null;  
	       }  
	    int[] result = new int[n];
	    for(int i=0;i<n;i++){
	    	result[i]=-1;
	    }
	    int count = 0;  
	    while(count < n) {  
	        int num = (int) (Math.random() * (max - min)) + min;  
	        boolean flag = true;  
	        for (int j = 0; j < count+1; j++) {  
	            if(num == result[j]){  
	                flag = false;  
	                break;  
	            }  
	        }  
	        if(flag){  
	            result[count] = num;  
	            count++;  
	        }  
	    }  
	    return result;  
	}  
	/**
	 * 
	 * 功能描述：获取当天日期
	 *
	 * @return
	 * 
	 * @author garfield
	 *
	 * @since 2018年01月02日
	 *
	 * @update:[变更日期YYYY-MM-DD][更改人姓名][变更描述]
	 */
	public static String getNowDate(){
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
		Calendar  localTime = Calendar.getInstance();
		Date nowDate = localTime.getTime();
		return formatter.format(nowDate);
	}
}

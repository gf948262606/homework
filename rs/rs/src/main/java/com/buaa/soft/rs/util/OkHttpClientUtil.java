package com.buaa.soft.rs.util;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/**
 * 功能描述：  . Http客户端工具类 <BR>
 * 历史版本: <Br>
 * 开发者: garfield  <BR>
 * 时间：2017年11月1日 下午5:40:22  <BR>
 * 变更原因：    <BR>
 * 变化内容 ：<BR>
 * 首次开发时间：2017年11月1日 下午5:40:22 <BR>
 * 描述：   <BR>
 * 版本：V1.0
 */

public class OkHttpClientUtil {
	 private static final OkHttpClient mOkHttpClient;
	 private final static long READ_TIMEOUT=30;
	 private final static long CONNECT_TIMEOUT=30;
	 private final static long WRITE_TIMEOUT=30;
	 
	 static {  
	        OkHttpClient.Builder ClientBuilder=new OkHttpClient.Builder();  
	        ClientBuilder.readTimeout(READ_TIMEOUT, TimeUnit.SECONDS);//读取超时  
	        ClientBuilder.connectTimeout(CONNECT_TIMEOUT, TimeUnit.SECONDS);//连接超时  
	        ClientBuilder.writeTimeout(WRITE_TIMEOUT, TimeUnit.SECONDS);//写入超时  
	        mOkHttpClient=ClientBuilder.build();  
	    }  
	public static String get(String url) throws IOException {
		Request request = new Request.Builder().url(url).build();
		Response response = mOkHttpClient.newCall(request).execute();
		if (response.isSuccessful()) {
			return response.body().string();
		} else {
			throw new IOException("Unexpected code " + response);
		}
	}
}

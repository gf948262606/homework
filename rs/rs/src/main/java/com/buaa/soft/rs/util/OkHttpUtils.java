package com.buaa.soft.rs.util;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/**
 * 功能描述：  . Http工具类 <BR>
 * 历史版本: <Br>
 * 开发者: garfield  <BR>
 * 时间：2017年11月1日 下午3:40:02  <BR>
 * 变更原因：    <BR>
 * 变化内容 ：<BR>
 * 首次开发时间：2017年11月1日 下午3:40:02 <BR>
 * 描述：   <BR>
 * 版本：V1.0
 */
public class OkHttpUtils {
	 private static final byte[] LOCKER = new byte[0];  
	 private static OkHttpUtils mInstance;  
	 private OkHttpClient mOkHttpClient;
	 private final static long READ_TIMEOUT=30;
	 private final static long CONNECT_TIMEOUT=30;
	 private final static long WRITE_TIMEOUT=30;
	 
	 private OkHttpUtils() {  
	        okhttp3.OkHttpClient.Builder ClientBuilder=new okhttp3.OkHttpClient.Builder();  
	        ClientBuilder.readTimeout(READ_TIMEOUT, TimeUnit.SECONDS);//读取超时  
	        ClientBuilder.connectTimeout(CONNECT_TIMEOUT, TimeUnit.SECONDS);//连接超时  
	        ClientBuilder.writeTimeout(WRITE_TIMEOUT, TimeUnit.SECONDS);//写入超时  
	        mOkHttpClient=ClientBuilder.build();  
	    }  
	  
	    public static OkHttpUtils getInstance() {  
	        if (mInstance == null) {  
	            synchronized (LOCKER) {  
	                if (mInstance == null) {  
	                    mInstance = new OkHttpUtils();  
	                }  
	            }  
	        }  
	        return mInstance;  
	    }  
	
	public String post(String url) throws IOException {
		FormBody body = new FormBody.Builder()
	     .add("legionId", "1084,1067")
	     .add("devicePut", "mb")
	     .build();

	    Request request = new Request.Builder().url(url).post(body).build();
	    

	    Response response = mOkHttpClient.newCall(request).execute();
	    if (response.isSuccessful()) {
	        return response.body().string();
	        
	    } else {
	        throw new IOException("Unexpected code " + response);
	    }
	}
	public String get(String url) throws IOException {
		Request request = new Request.Builder().url(url).build();
		
		Response response = mOkHttpClient.newCall(request).execute();
		if (response.isSuccessful()) {
			return response.body().string();
			
		} else {
			throw new IOException("Unexpected code " + response);
		}
	}

   public static void main( String[] args )
   {
   	try {
   		String uri1= "http://192.168.0.55:9200/_sql?format=csv&sql=SELECT COUNT(*) as dealOrderNum, COUNT(DISTINCT cf.stu_id.raw) as studentNum, SUM(cf.educate_amount) as dealOrderFlow  FROM f_mid_order where cf.status_code.raw in ('PAID','PRODCHANGED','CANCELED','FREEZED','STUCHANGED','EXPIRED') and cf.delete_flag.raw=0 and cf.payment_date='2017-07-20'";
			String res = OkHttpUtils.getInstance().get(uri1);
			String[] resArray = res.split("\t");
			for(String str : resArray){
				System.out.println(str);
				String[] dd = str.split(",");
				for(String cc : dd){
					System.out.println(cc);
				}
			}
//			String res1 = OkHttpUtils.getInstance().get(uri);
			
			
//			System.out.println(res);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
   }
}

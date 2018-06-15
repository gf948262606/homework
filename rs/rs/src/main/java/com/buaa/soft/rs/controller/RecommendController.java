package com.buaa.soft.rs.controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.huaban.analysis.jieba.JiebaSegmenter;
import com.huaban.analysis.jieba.SegToken;
import com.huaban.analysis.jieba.JiebaSegmenter.SegMode;




import redis.clients.jedis.JedisCluster;



@RestController
@RequestMapping("/movie-recommend")
public class RecommendController {
	private static final Logger logger = LoggerFactory
			.getLogger(RecommendController.class);

	private static Set<String> stopWordSet = new HashSet<String>();
	private static final int MAX_RETURN_LIST_SIZE = 3;
	
	@Autowired
	private JedisCluster jedisCluster;

	static {
		InputStream in = RecommendController.class
				.getResourceAsStream("/stopword.dic");
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		String line = null;
		try {
			while ((line = br.readLine()) != null) {
				stopWordSet.add(line);
			}
			br.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	// 分词构造标签数据集合
	public static HashSet<String> get_fenci_result(String str)
			throws IOException {

		JiebaSegmenter segmenter = new JiebaSegmenter();
		List<SegToken> result = segmenter.process(str, SegMode.SEARCH);
		HashSet<String> retSet = new HashSet<String>();
		for (SegToken tok : result) {
			System.out.println(tok.toString());
			retSet.add(tok.word);
		}
		return retSet;
	}
	
	// 推荐核心，推荐电影包信息
	private List<String> recommendPackageId(final Set<String> userTagSet) {

		// 返回值 三個 返回
		List<String> topCorrelateIds = new ArrayList<String>();

		// 这里设计 redis 四个表
		// recommend_blackset set 包含所有停用词
		// recommend_packages zset 包含所有电影id和电影播放量近三个月 排序
		// recommend_packagetags|电影id zset 包含所有电影id 对应的所有标签和对应词频权重
		// recommend_packageinfo|电影id hmap 包含所有电影id 对应的所有电影key value表信息

		// 获取所有的销售课程 id
		String recommendKey = "recommend_packages";
		Set<String> packagesSet = jedisCluster.zrevrange(recommendKey, 0, -1);

		// 轮询获取对应的权重
		List<Integer> maxCorrelate = new ArrayList<Integer>();
		// String maxCorrelateId = "1824042";
		for (String packageIdStr : packagesSet) {
			Set<String> resultSet = new HashSet<String>();
			resultSet.addAll(userTagSet);
			// 这里根据 packageIdStr 获取对应的电影包的 Set 数据
			Set<String> packageTagSet = jedisCluster.zrevrange(
					"recommend_packagetags|" + packageIdStr, 0, -1);
			resultSet.retainAll(packageTagSet);
			boolean haveWrite = false;
			int idx = 0;
			for (Integer correlateVal : maxCorrelate) {
				if (correlateVal < resultSet.size()) {
					maxCorrelate.add(idx, resultSet.size());
					topCorrelateIds.add(idx, packageIdStr);
					logger.info("result add:" + idx + " " + packageIdStr + ":"
							+ correlateVal + "<" + resultSet.size());
					haveWrite = true;
					break;
				}
				if (idx++ >= MAX_RETURN_LIST_SIZE) {
					break;
				}
			}
			if (idx < MAX_RETURN_LIST_SIZE && resultSet.size() > 0
					&& !haveWrite) {
				maxCorrelate.add(idx, resultSet.size());
				topCorrelateIds.add(idx, packageIdStr);
				logger.info("result add:" + idx + " " + packageIdStr + ":0<"
						+ resultSet.size());
			}
		}
		int retSize = (topCorrelateIds.size() < MAX_RETURN_LIST_SIZE) ? topCorrelateIds
				.size() : MAX_RETURN_LIST_SIZE;

				return topCorrelateIds.subList(0, retSize);
}
}

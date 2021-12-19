USE seiii;

DELETE FROM entity;
INSERT INTO entity (eid, pid, name, type, property) VALUES
("11111", 1,"詹姆·斯图尔特", "Character", "{'出生': '英格兰', '血统': '麻瓜', '婚姻状况': '已婚', '物种': '人类', '性别': '男', '职业': ['石匠', '伊尔弗莫尼魔法学校校长及创办者']}"),
("21111", 1,"玛莎·斯图尔特", "Character", "{'血统': '麻瓜', '婚姻状况': '已婚', '物种': '人类', '性别': '女性'}"),
("31111", 1,"伊索特·塞耶", "Character", "{'出生': '约1603年 伊尔弗莫尼小屋，柯姆洛格拉谷地，凯里郡，爱尔兰 ', '逝世': '晚于1703年年', '血统': '纯血统', '婚姻状况': '已婚', '物种': '人类', '性别': '女', '职业': ['伊尔弗莫尼魔法学校校长及创办者'], '学院': '长角水蛇学院'}"),
("41111", 1,"查威克·布特", "Character", "{'出生': '约1618年，爱尔兰', '血统': '混血统或纯血统', '婚姻状况': '已婚', '物种': '人类', '性别': '男', '职业': ['作家'], '学院': '雷鸟学院'}"),
("51111", 1,"韦伯·布特", "Character", "{'出生': '约1620年，爱尔兰', '逝世': '英国', '血统': '混血统或纯血统', '婚姻状况': '已婚', '物种': '人类', '性别': '男', '职业': ['雇佣傲罗'], '学院': '猫豹学院'}"),
("61111", 1,"玛莎·斯图尔特二世", "Character", "{'出生': '约1634年伊尔弗莫尼魔法学校，格雷洛克山，美国', '血统': '哑炮', '婚姻状况': '已婚', '物种': '人类', '性别': '女'}"),
("71111", 1,"雷欧娜·斯图尔特", "Character", "{'出生': '约1634年伊尔弗莫尼城堡，格雷洛克山，马萨诸塞州，美国', '血统': '混血统', '婚姻状况': '未婚', '物种': '人类', '性别': '女', '职业': ['伊尔弗莫尼魔法学校黑魔法防御术教师']}"),
("81111", 1,"伊尔弗莫尼魔法学校", "Group", "{}"),
("91111", 1,"威廉·塞耶", "Character", "{'逝世': '约1608年', '血统': '纯血统', '婚姻状况': '已婚', '物种': '人类', '性别': '男'}"),
("101111", 1,"雷欧娜·塞耶", "Character", "{'逝世': '约1608年', '血统': '纯血统', '婚姻状况': '已婚', '物种': '人类', '性别': '女'}"),
("111111", 1,"葛姆蕾·冈特", "Character", "{'出生': '爱尔兰', '逝世': '约1634年', '血统': '纯血统', '婚姻状况': '未婚', '物种': '人类', '性别': '女', '学院': '斯莱特林学院'}"),
("121111", 1,"莫瑞根", "Character", "{'出生': '爱尔兰', '血统': '纯血统', '物种': '人类', '性别': '女'}"),
("131111", 1,"萨拉查·斯莱特林", "Character", "{'出生': '中世纪', '逝世': '中世纪', '血统': '纯血统', '物种': '人类', '性别': '男', '头发颜色': '灰色', '眼睛颜色': '灰色', '皮肤颜色': '浅色', '职业': ['霍格沃茨教授 (约10世纪)'], '学院': '斯莱特林学院'}");


DELETE FROM relation;
INSERT INTO relation (pid, source_id, target_id, source, target, relation, type, hash_id) VALUES
(1, "11111", "21111", "詹姆·斯图尔特", "玛莎·斯图尔特", "妻子", "connection", "e0" ),
(1, "11111", "31111", "詹姆·斯图尔特", "伊索特·塞耶", "老师", "connection", "e123" ),
(1, "61111", "81111", "玛莎·斯图尔特二世", "伊尔弗莫尼魔法学校", "学院", "group", "sdliajds" ),
(1, "71111", "81111", "雷欧娜·斯图尔特", "伊尔弗莫尼魔法学校", "学院", "group", "e1codli23" ),
(1, "11111", "61111", "詹姆·斯图尔特", "玛莎·斯图尔特二世", "父亲", "connection", "cliaen" ),
(1, "11111", "71111", "詹姆·斯图尔特", "雷欧娜·斯图尔特", "父亲", "connection", "sadvvs" ),
(1, "71111", "101111", "詹姆·斯图尔特", "雷欧娜·塞耶", "朋友", "connection", "sssac" ),
(1, "71111", "111111", "詹姆·斯图尔特", "葛姆蕾·冈特", "好友", "connection", "fessws" ),
(1, "91111", "101111", "威廉·塞耶", "雷欧娜·塞耶", "丈夫", "connection", "fessws" ),
(1, "71111", "111111", "詹姆·斯图尔特", "葛姆蕾·冈特", "好友", "connection", "fessws" ),
(1, "41111", "51111", "查威克·布特", "韦伯·布特", "兄弟", "connection", "cewewwe" ),
(1, "121111", "131111", "莫瑞根", "萨拉查·斯莱特林", "嫂子", "connection", "bnmvcnm" ),
(1, "41111", "61111", "查威克·布特", "玛莎·斯图尔特二世", "好友", "connection", "xxzcwd" );

DELETE FROM position;
INSERT INTO position (id, pid, x, y) VALUES
("11111", 1, 269.05429063897554, -856.6604646064388),
("21111", 1, 402.14926635710526, 965.6494421468306),
("31111", 1, 903.968804722484, 743.0099466160189),
("41111", 1, 151.65542054242792, 94.94169319732009),
("51111", 1, 589.9939014188105, 933.2108694406518),
("61111", 1, 91.70476478259047, 959.0918928851936),
("71111", 1, 420.4709927345616, -935.6165811900845),
("81111", 1, -751.5466484107881, 547.5337755789058),
("91111", 1, 547.8329889279889, 620.6347280356331),
("101111", 1, -81.57241668957988, -277.31985165524463),
("111111", 1, -247.9076976504797, 253.81223199047986),
("121111", 1, 338.0587592178333, -963.0760362771605),
("131111", 1, -836.9007763727325, -516.3742189620816);

DELETE FROM `project`;
INSERT INTO `project` value (1, 1, '哈利波特');

DELETE FROM `user`;
INSERT INTO `user` value (1, '123456', '123@qq.com');
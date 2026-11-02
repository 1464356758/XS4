# CH003《第七炉有人》待登记完整草稿说明

- 正文：`drafts/CH003_pending_lock.txt`
- 实测汉字：9578（与V4.3采用的汉字范围校验口径相同）
- 承接：CH001、CH002冻结正文，只读；当前冻结基线2章。
- 正式状态：仅将完整文本保存为待审draft，没有调用candidate、release-check、adopt或daily finish；不能称为正式采用。
- 当前阻断：`book/daily/active.json` 的CH003旧自动化控制者 `xs4_20261102_a92f7c41`，run_id `ec2d137cbc4c4f81926a343adf67a9a5`，platform_run_id为null，status=blocked。旧任务真实平台运行已结束，但正常stopped_proof要求旧controller有非空platform_run_id，因此不能由新会话沿普通begin恢复。未伪造旧ID、未篡改旧锁、未建立维护授权。
- 本稿必须在取得合法控制者执行权之后：运行正式brief-request/brief-check、history-search、writer context；以本文登记candidate及reader context；实际反向提纲、八项与narrative审读、真实引文检查；必要时局部repair且不重置次数；只用执行器finalize冻结。
- 人物余波：阿禾从西检修廊救出但手掌烫伤、吸烟呛咳；主角左眼未治、右腿旧伤持续、右臂新烫伤、短刀落失，并被护矿人暂押；余三斗拉止风杠，承担炉炭损失。全章未恢复灵根。
- 双牌：阿禾救出两片来源尚待核的破木牌，两片均有乙七前号，材质、孔位及余后字形不同；这能排除「只有一片板反复挂用」的简单解释，但尚不能锁定谁换车或有权使用的日期；原炉房交接页被烧，后续须找其他来源验证。
- 承诺：P-FURNACE-003有救援实体结果但不是永久脱险；P-DOUBLE-004有两片不同的实物与持有人口供，但真正换车人不明；需要审核判断是否达到约定的独立核验标准，不能预先批填complete。
- 未实际执行GitHub Actions审查，当前无正式run_id，不更改自动任务启用状态、书籍主分支、source state、冻结正文、索引或发布回执。

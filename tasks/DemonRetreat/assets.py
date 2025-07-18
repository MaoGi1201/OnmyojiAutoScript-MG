from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DemonRetreatAssets: 


	# Image Rule Assets
	# 神社 
	I_SHRINE = RuleImage(roi_front=(870,624,65,61), roi_back=(870,624,65,61), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_shrine.png")
	# 首领退治 
	I_HUNT = RuleImage(roi_front=(418,162,186,166), roi_back=(418,162,186,166), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_hunt.png")
	# 检查是否成功进入首领退治 
	I_HUNT_CHECK = RuleImage(roi_front=(572,10,144,46), roi_back=(572,10,144,46), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_hunt_check.png")
	# 集结 
	I_DEMON_GATHER = RuleImage(roi_front=(26,487,76,48), roi_back=(26,487,76,48), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_demon_gather.png")
	# 非退治时间进行检查 
	I_DEMON_BACK_CHECK = RuleImage(roi_front=(27,26,42,36), roi_back=(14,2,86,86), threshold=0.7, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_demon_back_check.png")
	# 迟到直接进入战斗 
	I_ENTER_FIRE = RuleImage(roi_front=(1141,579,100,68), roi_back=(1141,579,100,68), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_enter_fire.png")
	# 取消退出 
	I_QUIT_BACK = RuleImage(roi_front=(488,401,100,44), roi_back=(488,401,100,44), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_new.png")
	# 退治排行榜 
	I_RANK_LSIT = RuleImage(roi_front=(538,6,200,54), roi_back=(538,6,200,54), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_rank_lsit.png")
	# 全部领取 
	I_REWARD_ALL = RuleImage(roi_front=(534,540,178,60), roi_back=(534,540,178,60), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_reward_all.png")
	# 祈愿 
	I_PRAY = RuleImage(roi_front=(1178,380,42,70), roi_back=(1178,380,42,70), threshold=0.8, method="Template matching", file="./tasks/DemonRetreat/DemonRetreat/DemonRetreat_pray.png")


	# Ocr Rule Assets
	# 检查是否迟到 
	O_LATER_ENTER_CHECK = RuleOcr(roi=(928,16,48,35), area=(928,16,48,35), mode="Single", method="Default", keyword="", name="later_enter_check")



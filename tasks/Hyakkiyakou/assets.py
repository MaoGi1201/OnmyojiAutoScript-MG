from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class HyakkiyakouAssets: 


	# Click Rule Assets
	# description 
	C_HSELECT_1 = RuleClick(roi_front=(200,318,115,273), roi_back=(200,318,115,273), name="hselect_1")
	# description 
	C_HSELECT_2 = RuleClick(roi_front=(570,307,142,285), roi_back=(570,307,142,285), name="hselect_2")
	# description 
	C_HSELECT_3 = RuleClick(roi_front=(934,298,115,306), roi_back=(934,298,115,306), name="hselect_3")
	# 日常使用 
	C_FRIEND_1 = RuleClick(roi_front=(445,231,160,58), roi_back=(445,231,160,58), name="friend_1")
	# 日常使用 
	C_FRIEND_2 = RuleClick(roi_front=(716,230,160,56), roi_back=(716,230,160,56), name="friend_2")
	# description 
	C_FRIEND_3 = RuleClick(roi_front=(240,310,183,66), roi_back=(240,310,183,66), name="friend_3")
	# description 
	C_FRIEND_4 = RuleClick(roi_front=(504,311,184,62), roi_back=(504,311,184,62), name="friend_4")
	# 日常使用 
	C_FRIEND_5 = RuleClick(roi_front=(241,395,178,61), roi_back=(241,395,178,61), name="friend_5")
	# 日常使用 
	C_FRIEND_6 = RuleClick(roi_front=(508,394,182,62), roi_back=(508,394,182,62), name="friend_6")
	# 回归活动使用 
	C_FRIEND_1_RECALL = RuleClick(roi_front=(234,228,180,56), roi_back=(234,228,180,56), name="friend_1_recall")
	# 回归活动使用 
	C_FRIEND_2_RECALL = RuleClick(roi_front=(506,228,178,54), roi_back=(532,226,178,54), name="friend_2_recall")


	# Image Rule Assets
	# 邀请按钮 
	I_HINVITE = RuleImage(roi_front=(139,593,63,39), roi_back=(105,535,129,147), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hinvite.png")
	# 进入 
	I_HACCESS = RuleImage(roi_front=(1055,551,100,100), roi_back=(1055,551,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_haccess.png")
	# 开始 
	I_HSTART = RuleImage(roi_front=(1117,549,100,100), roi_back=(1117,549,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hstart.png")
	# 押注 
	I_HSELECTED = RuleImage(roi_front=(980,265,41,44), roi_back=(226,53,836,348), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hselected.png")
	# 结束 
	I_HEND = RuleImage(roi_front=(81,164,86,300), roi_back=(81,164,86,300), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hend.png")
	# 冰冻 
	I_HFREEZE = RuleImage(roi_front=(1092,665,187,54), roi_back=(1092,665,187,54), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hfreeze.png")
	# description 
	I_HTITLE = RuleImage(roi_front=(578,21,134,48), roi_back=(578,21,134,48), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_htitle.png")
	# description 
	I_HCLOSE_RED = RuleImage(roi_front=(1056,177,54,54), roi_back=(1056,177,54,54), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hclose_red.png")
	# 判断是否是回归活动 
	I_ENSURE_RECALL = RuleImage(roi_front=(1071,151,50,50), roi_back=(877,72,307,211), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_ensure_recall.png")


	# Image Rule Assets
	# 左边概率up 
	I_HYA_STATE_BUFF06 = RuleImage(roi_front=(331,7,126,41), roi_back=(137,1,342,66), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hya_state_buff06.png")
	# 冰冻 
	I_HYA_STATE_BUFF05 = RuleImage(roi_front=(158,5,127,45), roi_back=(147,0,322,62), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hya_state_buff05.png")
	# 左边好友up 
	I_HYA_STATE_BUFF07 = RuleImage(roi_front=(157,7,127,43), roi_back=(143,0,347,80), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hya_state_buff07.png")
	# 左边减速 
	I_HYA_STATE_BUFF02 = RuleImage(roi_front=(157,6,128,39), roi_back=(146,1,348,55), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hya_state_buff02.png")
	# 左边砸豆加速 
	I_HYA_STATE_BUFF03 = RuleImage(roi_front=(326,4,129,44), roi_back=(143,3,326,59), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_hya_state_buff03.png")


	# Image Rule Assets
	# description 
	I_RESF_0 = RuleImage(roi_front=(615,13,30,46), roi_back=(606,11,43,51), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_0.png")
	# description 
	I_RESF_1 = RuleImage(roi_front=(617,13,31,46), roi_back=(610,11,42,50), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_1.png")
	# description 
	I_RESF_2 = RuleImage(roi_front=(611,14,33,47), roi_back=(602,10,47,57), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_2.png")
	# description 
	I_RESF_3 = RuleImage(roi_front=(619,14,28,45), roi_back=(610,12,40,49), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_3.png")
	# description 
	I_RESF_4 = RuleImage(roi_front=(611,14,37,47), roi_back=(608,14,43,47), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_4.png")
	# description 
	I_RESF_5 = RuleImage(roi_front=(612,10,35,48), roi_back=(612,10,35,48), threshold=0.9, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_5.png")
	# description 
	I_RESF_6 = RuleImage(roi_front=(616,10,29,49), roi_back=(616,10,29,49), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_6.png")
	# description 
	I_RESF_7 = RuleImage(roi_front=(611,14,38,44), roi_back=(611,14,38,44), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_7.png")
	# description 
	I_RESF_8 = RuleImage(roi_front=(615,10,32,50), roi_back=(615,10,32,50), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_8.png")
	# description 
	I_RESF_9 = RuleImage(roi_front=(612,12,38,49), roi_back=(612,12,38,49), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resf_9.png")
	# description 
	I_RESR_0 = RuleImage(roi_front=(636,11,34,47), roi_back=(636,11,34,47), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_0.png")
	# description 
	I_RESR_1 = RuleImage(roi_front=(638,13,29,48), roi_back=(638,13,29,48), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_1.png")
	# description 
	I_RESR_2 = RuleImage(roi_front=(639,15,30,39), roi_back=(639,15,30,39), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_2.png")
	# description 
	I_RESR_3 = RuleImage(roi_front=(639,14,30,41), roi_back=(639,14,30,41), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_3.png")
	# description 
	I_RESR_4 = RuleImage(roi_front=(636,13,32,46), roi_back=(636,13,32,46), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_4.png")
	# description 
	I_RESR_5 = RuleImage(roi_front=(639,13,31,46), roi_back=(639,13,31,46), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_5.png")
	# description 
	I_RESR_6 = RuleImage(roi_front=(638,12,32,44), roi_back=(638,12,32,44), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_6.png")
	# description 
	I_RESR_7 = RuleImage(roi_front=(638,15,34,42), roi_back=(638,15,34,42), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_7.png")
	# description 
	I_RESR_8 = RuleImage(roi_front=(638,13,33,47), roi_back=(638,13,33,47), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_8.png")
	# description 
	I_RESR_9 = RuleImage(roi_front=(638,12,32,47), roi_back=(638,12,32,47), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_resr_9.png")


	# Image Rule Assets
	# description 
	I_BEAN0 = RuleImage(roi_front=(150,648,13,22), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean0.png")
	# description 
	I_BEAN1 = RuleImage(roi_front=(134,648,11,22), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean1.png")
	# description 
	I_BEAN2 = RuleImage(roi_front=(134,649,14,21), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean2.png")
	# description 
	I_BEAN3 = RuleImage(roi_front=(134,649,14,21), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean3.png")
	# description 
	I_BEAN4 = RuleImage(roi_front=(135,647,13,23), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean4.png")
	# description 
	I_BEAN5 = RuleImage(roi_front=(135,649,13,22), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean5.png")
	# description 
	I_BEAN6 = RuleImage(roi_front=(132,649,15,21), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean6.png")
	# description 
	I_BEAN7 = RuleImage(roi_front=(133,648,15,22), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean7.png")
	# description 
	I_BEAN8 = RuleImage(roi_front=(132,646,14,23), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean8.png")
	# description 
	I_BEAN9 = RuleImage(roi_front=(133,649,15,21), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean9.png")
	# description 
	I_BEAN05 = RuleImage(roi_front=(387,640,32,35), roi_back=(371,631,86,52), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean05.png")
	# description 
	I_BEAN10 = RuleImage(roi_front=(560,640,32,35), roi_back=(531,634,72,47), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_bean10.png")


	# Image Rule Assets
	# description 
	I_FRIEND_SAME_1 = RuleImage(roi_front=(378,126,100,60), roi_back=(378,126,100,60), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_friend_same_1.png")
	# description 
	I_FRIEND_SAME_1_RECALL = RuleImage(roi_front=(170,126,100,60), roi_back=(154,105,132,94), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_friend_same_2.png")
	# description 
	I_FRIEND_SAME_2 = RuleImage(roi_front=(168,126,100,60), roi_back=(152,112,133,80), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_friend_same_2.png")
	# description 
	I_FRIEND_REMOTE_2 = RuleImage(roi_front=(296,122,100,56), roi_back=(278,115,131,81), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/hya/hya_friend_remote_2.png")


	# Ocr Rule Assets
	# 最坏的情况下来判断豆子的数量 
	O_BEAN_NUMBER = RuleOcr(roi=(119,645,45,29), area=(119,645,45,29), mode="Digit", method="Default", keyword="", name="bean_number")


	# Swipe Rule Assets
	# description 
	S_BEAN_05TO10 = RuleSwipe(roi_front=(390,648,21,22), roi_back=(577,647,21,23), mode="default", name="bean_05to10")
	# description 
	S_BEAN_10TO05 = RuleSwipe(roi_front=(565,647,24,24), roi_back=(390,647,22,22), mode="default", name="bean_10to05")


	# Click Rule Assets
	# description 
	C_CLICK = RuleClick(roi_front=(26,250,33,100), roi_back=(26,250,33,100), name="click")


	# Image Rule Assets
	# 缘结之庭 
	I_TPAGE_1 = RuleImage(roi_front=(238,504,221,123), roi_back=(121,480,950,166), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_1.png")
	# 本丸御殿 
	I_TPAGE_2 = RuleImage(roi_front=(411,506,231,120), roi_back=(132,479,933,171), threshold=0.5, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_2.png")
	# 之境 
	I_TPAGE_3 = RuleImage(roi_front=(748,504,240,118), roi_back=(125,482,937,166), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_3.png")
	# 鲸歌潜岸 
	I_TPAGE_4 = RuleImage(roi_front=(281,507,233,120), roi_back=(124,484,933,163), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_4.png")
	# 杨帆远航 
	I_TPAGE_5 = RuleImage(roi_front=(539,506,238,120), roi_back=(130,483,940,166), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_5.png")
	# 繁影留住 
	I_TPAGE_6 = RuleImage(roi_front=(801,505,232,118), roi_back=(128,493,937,153), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tpage_6.png")
	# description 
	I_TCHECK_1 = RuleImage(roi_front=(19,246,100,100), roi_back=(2,218,135,215), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_1.png")
	# description 
	I_TCHECK_2 = RuleImage(roi_front=(9,216,157,226), roi_back=(0,197,186,263), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_2.png")
	# description 
	I_TCHECK_3 = RuleImage(roi_front=(5,126,138,299), roi_back=(2,110,147,345), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_3.png")
	# description 
	I_TCHECK_4 = RuleImage(roi_front=(7,108,100,332), roi_back=(0,101,120,347), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_4.png")
	# description 
	I_TCHECK_5 = RuleImage(roi_front=(132,28,77,103), roi_back=(94,13,152,234), threshold=0.4, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_5.png")
	# description 
	I_TCHECK_6 = RuleImage(roi_front=(9,107,100,350), roi_back=(3,97,113,369), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_6.png")
	# description 
	I_SWITCH_BACKGROUND = RuleImage(roi_front=(992,649,105,36), roi_back=(969,627,152,72), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_switch_background.png")
	# description 
	I_TCHECK_22 = RuleImage(roi_front=(14,150,100,100), roi_back=(5,139,124,127), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_22.png")
	# description 
	I_TCHECK_32 = RuleImage(roi_front=(35,175,100,100), roi_back=(26,155,123,141), threshold=0.7, method="Template matching", file="./tasks/Hyakkiyakou/train/train_tcheck_32.png")
	# 检查是否在砸豆子 
	I_CHECK_RUN = RuleImage(roi_front=(95,598,92,45), roi_back=(68,578,143,100), threshold=0.8, method="Template matching", file="./tasks/Hyakkiyakou/train/train_check_run.png")


	# Swipe Rule Assets
	# description 
	S_TSWIPE = RuleSwipe(roi_front=(421,521,21,91), roi_back=(273,516,23,100), mode="default", name="tswipe")
	# description 
	S_TBACK = RuleSwipe(roi_front=(259,515,21,100), roi_back=(993,521,22,100), mode="default", name="tback")



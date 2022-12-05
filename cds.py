


def cds():
	# 0.5秒ごとに２０回cdsの状態を読み取り、その合計を計算
	cds_total = 0
	for i in range(20):
		cds_total =  cds_total + read_cds
		time.sleep(0.5)
		
	# その結果からoff、on、満水を判断する。
	if cds_total == 0:
		return 'off'
	if cds_total > 18:
		return 'on'
	return '満水'
	
	

	
		


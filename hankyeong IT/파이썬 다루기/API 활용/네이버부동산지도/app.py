
from flask import Flask, render_template, request, redirect
import ggcode

app=Flask(__name__)

@app.route('/map')
def hello():
	return render_template('map.html')

@app.route("/navermap",methods=['POST'])
def test_p():
	add=request.form['address']
	opt=request.form['radio_info']

	# add 위도/경도 찾기
	gmap=ggcode.Geocode(add)
	lat_lng=f'{gmap.get_lat()},{gmap.get_lng()}'


	# opt별 url 생성
	url_dict={
		'아파트':'http://new.land.naver.com/complexes?ms='+lat_lng+',15&a=APT:ABYG:JGC',
		'빌라':'http://new.land.naver.com/houses?ms='+lat_lng+',15&a=VL:DDDGG:JWJT:SGJT:HOJT',
		'원룸':'http://new.land.naver.com/rooms?ms='+lat_lng+',15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT',
		'상가':'http://new.land.naver.com/offices?ms='+lat_lng+',15&a=SG:SMS:GJCG:APTHGJ:GM:TJ',
		'분양':'https://isale.land.naver.com/iSale/Map/#?SYMap='+lat_lng+',15&a=IA01'
	}
	url=url_dict[opt]
	return redirect(url)

if __name__=='__main__':
	app.run()
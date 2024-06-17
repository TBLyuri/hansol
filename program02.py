#
# 캔들차트 시각화 예시.
#

# 캔들 차트 관련해서는 다음 사이트를 참고해 본다.
# https://github.com/matplotlib/mplfinance/

# 먼저 커맨드라인에서 다음과 같이 라이브러리 설치 필요.
# pip install streamlit
# pip install streamlit-lottie
# pip install finance-datareader
# pip install mplfinance
# pip install bs4

# 필요한 라이브러리를 불러온다.
import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 시장 데이터를 읽어오는 함수들을 정의한다.
def getData(code, datestart, dateend):
    df = fdr.DataReader(code, datestart, dateend ).drop(columns='Change')  # 불필요한 'Change' 컬럼은 버린다.
    return df

def getSymbols(market='KOSPI', sort='Marcap'):
    df = fdr.StockListing(market)
    ascending = False if sort == 'Marcap' else True
    df.sort_values(by=[sort], ascending = ascending, inplace=True)
    return df[ ['Code', 'Name', 'Market'] ]

# code에 해당하는 주식 데이터를 받아온다.
code = '005930'              # 삼성전자.
#code = '373220'             # LG 에너지솔루션.
date_start = (datetime.today()-timedelta(days=30)).date()           # 시분초 떼어내고 년월일 날짜만.
df = getData(code, date_start, datetime.today().date())     

# 캔들차트를 출력해 본다.
chart_style = 'default'                                             # 'default', 'binance', 'classic', 'yahoo', 등 중에서 선택.
marketcolors = mpf.make_marketcolors(up='red', down='blue')         # 양봉/음봉 선택.
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

fig, ax = mpf.plot(
    data=df,                            # 받아온 데이터.      
    volume=False,                       # True 또는 False.                   
    type='candle',                      # 캔들 차트.
    style=mpf_style,                    # 위에서 정의.
    figsize=(10,7),
    fontscale=1.1,
    mav=(5,10,30),                      # 이동평균선 (mav) 3개.
    mavcolors=('red','green','blue'),   # 이동평균선 색상.
    returnfig=True                      # Figure 객체 반환.
)

plt.show()


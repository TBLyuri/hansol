#
# 주식 데이터를 내려받아 주는 예시.
#

# 먼저 커맨드라인에서 다음과 같이 라이브러리 설치 필요.
# pip install streamlit
# pip install streamlit-lottie
# pip install finance-datareader
# pip install mplfinance
# pip install bs4

# 필요한 라이브러리를 불러온다.
import FinanceDataReader as fdr
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

# code에 해당하는 주식 데이터를 받아와서 출력해 준다.
code = '005930'              # 삼성전자.
#code = '373220'             # LG 에너지솔루션.
date_start = (datetime.today()-timedelta(days=30)).date()           # 시분초 떼어내고 년월일 날짜만.
df = getData(code, date_start, datetime.today().date())     

print(df)


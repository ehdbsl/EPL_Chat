### EPL_ChatBot
<hr>
<p>팀장: 황동현</p>
<p>팀원: 김대현, 김도윤, 이종현</p>
<p>목적: 축구에 관심이 많은 팀원들이 해외 축구리그를 모르는 사람들을 위해 채팅 봇 개발</p>
<hr>
<p>EPL이란: 영국 잉글랜드의 최상위 프로 축구 리그. 다른 국가의 축구 리그[2]와는 달리 축구 종주국으로 국가명을 따로 붙이지 않기에 정식 명칭은 'Premier League'지만 편의상 타 리그와 구분을 위해 'PL'보단 앞에 England의(잉글랜드 프리미어 리그) E를 붙인 'EPL'로 쓰는 경우도 있다.</p>
<hr>
<p>사용한 Library</p>
```
fastapi
uvicorn
transformers
torch
```

<hr>
<p>installation</p>
'''
pip install fastapi uvicorn transformers torch
'''

<hr>
<p>기능: 챗봇, 뉴스 기사 제공, 퀴즈</p>

<p>사용 NLP 모델: skt/kogpt2-base-v2, KoBART</p>
<p>skt/kogpt2-base-v2: 부족한 한국어 성능을 극복하기 위해 40GB 이상의 텍스트로 학습</p>
<p>
  <ul>
    <p>KoBART</p>
    <li>BART는 페이스북 AI 연구팀에서 제안한 텍스트 생성 모델</li>
    <li>주로텍스트요약,번역,문장생성등다양한자연어처리작업에사용</li>
    <li>한국어 버전의 BART (Bidirectional and Auto-Regressive Transformers) 모델</li>
  </ul>
</p>



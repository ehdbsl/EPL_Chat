### EPL_ChatBot
<hr>
<p>팀장: 황동현</p>
<p>팀원: 김대현, 김도윤, 이종현</p>
<p>목적: 축구에 관심이 많은 팀원들이 해외 축구리그를 모르는 사람들을 위해 채팅 봇 개발</p>
<hr>
<p>EPL이란: 영국 잉글랜드의 최상위 프로 축구 리그. 다른 국가의 축구 리그[2]와는 달리 축구 종주국으로 국가명을 따로 붙이지 않기에 정식 명칭은 'Premier League'지만 편의상 타 리그와 구분을 위해 'PL'보단 앞에 England의(잉글랜드 프리미어 리그) E를 붙인 'EPL'로 쓰는 경우도 있다.</p>
<hr>
<p>사용한 Library</p>

<p>fastapi</p>
<p>uvicorn</p>
<p>transformers</p>
<p>torch</p>


<hr>
<p>installation</p>

pip install fastapi uvicorn transformers torch


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

<hr>
<p>Trouble Shooting</p>
<p>비주류 팀에 대한 정보의 다양성, 신뢰성 문제</p>
<p>보완: 여러 출처의 데이터를 교차검증하여 정확도 확보</p>
<p>모델 학습 시 높은 validation loss 값, 너무 짧은 학습 시간때문에 발생한 답변 오류, 생성 시간 지연, 문법 오류</p>
<p>보완: 데이터를 적절히 전처리 + early-stopping 방법을 활용</p>
<p>GPT2, T5, BERT 등 여러 모델을 적용해보는 과정에서 결과가 좋지 않아 시간 소요가 많이 됨</p>
<p>보완: 한국어 사전학습 모델인 KoGPT-2 활용, 데이터를 더 확보한다면 품질 개선 가능</p>


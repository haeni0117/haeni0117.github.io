---
title: "[개발자의 글쓰기] 프롤로그 - 개발자의 글쓰기는 달라야한다."
categories:
  - 개발서적
tags:
  - 개발자
  - 글쓰기
last_modified_at: 2021-11-14T08:06:00-05:00
---

# 개발자는 글을 못 쓴다?
- 필자는 글쓰기 강의를 다닐 때 산신령이야기를 통해 간결한 글쓰기를 강의한다.
- 개발과 DB설계를 하는 DBA : "나무꾼,산신령,도끼를 각각 W,G,x로 치환해서 요약해야하는 것 아니냐?"
  - 논리적으로 어긋나는 이야기 X
  - BUT 이런식으로 변수를 적극적으로 사용하는 글쓰기는 비개발자(기획자,관리자)가 보기에 당황스러울 수 있다고 생각

# 글을 쓸 때 가장 중요한 것 : 정확성, 간결성, 가독성
- 개발자의 글쓰기 : 클래스/함수의 이름, 주석, 에러메시지, 릴리스문서, 개발가이드
  - SM(System Management)업무 : 장애보고서 
  - SI(System Integration)업무 : 제안서와 ERD, 기능명세서 등과 같은 개발산출물
- **<mark style="background-color: black;"><span style="color:white">정확성</span></mark> : 틀림이 없이 확실한 것**
- **<mark style="background-color: black;"><span style="color:white">간결성</span></mark> : 글에 군더더기가 없고 간단하고 깔끔한 것, 구구절절이 아닌 핵심만 설명**
- **<mark style="background-color: black;"><span style="color:white">가독성</span></mark> : 쉽게 읽히는 것 by 쉬운 용어, 표나 그림으로 정리, 문서의 체계와 위계**
- 정확성, 간결성, 가독성 : 서로 대치되는 목표
  - 정확성 ↑ ⇒ 간결성, 가독성 ↓ (∵ 부연설명이 늘어나서)
  - 간결성 ↑ ⇒ 정확성, 가독성 ↓ (∵ 너무 간추려버려서) 
  - 가독성 ↑ ⇒ 간결성, 정확성 ↓ (∵ 텍스트를 줄이게 됨, '쉽게 읽힘'을 제일의 목표로 두면 당연히 나머지는 가져갈 수가 X)

## 예시 : 신청자의 나이로 성인인지 아닌지 분류하는 코드
### Ver.1
```
function get(m){
  var result;
  if(m.year<20){
    result = 0;
  }
  else{
    result = 1;
  }
}
```
- 코드설명 : 신청자의 나이가 20세 미만 = 0, 그 이상이면 1로 분류
- 코드 문제
  1. 정확성 ↓ ⇒ ∵ 너무 간결
    - 우리나라 민법의 성년 기준 != 20세, == 만19세
    - 민법 제42조 <u>"사람은 19세로 성년에 이르게 된다"</u> 
      - '만 19세' = 그 해 생일이 되어야 성인이 된다.
  2. result값으로 숫자 사용(0,1...) ⇒ 실수로 값이 바뀌어 에러가능성 有
  3. 가독성 ↓

3번 코드문제를 해결하기 위해 코드를 수정해보자.

### Ver.2
```
function get(m){
  var result;
  var todayMonthAndDay = ...
  if(m.year>19){ //19세 초과라면 성인이 맞다(true)
    result = 1;
  }
  else if(m.year==19){
    if(m.monthAndDay >= todayMonthAndDay){//오늘이 생일이거나, 생일이 이미 지났거나
    result = 1;
  }
  else{
    result = 0; 
    //위 두 조건도 만족하지못함 = 19세인데 생일이 안지났거나 or 18세 이하거나
  }
}
```

### Ver.3
```
const LEGAL_ADULT = 1
const LEGAT_NOT_ADULT = 0
//semantic한 변수를 활용하여 실수에 기반한 버그방지

function checkLegalAdult(m){
  var legalAdult;
  if(m.ageOfMajority > 19){
  //ageOfMajority : 법적 나이X / 일상적 의미의 나이O
    result = LEGAL_ADULT;
  }
  else if(m.ageOfMajority == 19){
    if(m.mondthAndDay >= todayMonthAndDay){
      result = LEGAL_ADULT;
    }
    else{
      result = LEGAL_NOT_ADULT;
    }
  }
  else{
    result = LEGAL_NOT_ADULT;
  }
}
```
- VER.2에 비해 정확성, 가독성 ↑
- VER.2에 비해 간결성 ↓ ⇒ 복잡한 느낌

# 개발자의 글쓰기

그렇다면 '정확하고 간결하고 가독성이 높은 글'은 불가능한걸까? NO!
- 훈련 ⇒ 개발자 누구나 정확하고 간결하고 가독성이 높은 글을 생산가능
- 빠른 속도로 발전하는 기술스택과 도구에 비해 개발자들의 글쓰기 실력은 제자리이다.
  - 대기업 : 테크니컬라이터가 개발가이드 같은 문서를 관리하고 쓸 수 있다.
  - 하지만 내가 속한 조직이 Google, Naver과 같은 대기업이 아니라면? 
  - 테크니컬라이터만큼은 아니더라도 글을 잘쓰는 것은 분명 플러스요인이다. ~~오히려 좋아~~
  - <mark><span style="color:red">주요 이유 : 개발자를 위한 글쓰기 교육의 부재</span></mark>
    - 테크니컬라이터를 두고 있는 대기업도 개발자에게 일반적인 비즈니스 보고서 작성법만 가르친다. 
    - <span style="color:red">즉, 개발자가 현업에서 필요로 하는 글쓰기 방법을 배울 수 없다는 것이다.</span>
    - 개발자 타겟팅 도서 : 코딩기술 위주
    - 변수 이름, 네이밍 컨벤션, 주석, 에러메시지, 릴리스노트, 장애 보고서, 개발 가이드, SI제안서, 기술블로그 쓰는 법을 가르쳐주는 사람 X
  - 개발자 간의 소통 + 유저 및 잠재고객과의 소통하는 일 증가 ⇒ 개발하는 것만큼이나 글 쓸 일 ↑
    - GitHub ⇒ 개발자가 만든 코드 공개
    - 개발자 사이트 ⇒ 외부 개발자와 협력하는 일 ↑
- <u>이 책의 목적 : <span style="color:red">개발자의 글쓰기 능력을 종합적으로 향상시키기 위함</span></u> 
  - 코드 안 : 함수와 변수 네이밍, 주석 쓰는 법, 에러메시지 쓰기
  - 코드 밖 : 릴리스노트, 장애보고서, 개발가이드, SI제안서의 기술 부문을 설득력 있게 쓰는 법(for 외주개발자)
  - 기술블로그 쓰는 법 + 운영하는 팁
- 코딩 ∩ 글쓰기 = 과학 + 기술
- 체계적 배움 ⇒ 누구나 글을 잘 쓸 수 있다!


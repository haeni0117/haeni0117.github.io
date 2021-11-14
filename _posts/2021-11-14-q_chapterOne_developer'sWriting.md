---
title: "[개발자의 글쓰기] 1장 01_문장과 단락을 구조화하는 법"
categories:
  - 개발서적
tags:
  - 개발자
  - 글쓰기
  - 구조화
last_modified_at: 2021-11-14T09:06:00-05:00
---
# 문장을 구조화하는 법
- 문장을 만드는 방법은 다양함
  - ex1 : '나는 김철수다' : 주어 + 서술어
  - ex2 : '김철수가 사랑하는 사람은 이소연이 아니다' : 주어(주어 + 서술어 + 목적어) + 서술어(보어+서술어)
    - Cf) ex3 : '이소연은 김철수가 사ㅏㄹㅇ하는 사람이 아니다' : 주어절과 보어 교체

  - '색상 RGB 값을 각각 사용하기 때문에 입력 데이터는 3차원 벡터다'
    - 주어 = 입력데이터 ∴ 주어를 문장의 처음으로
      - → '입력데이터는 색상 RGB 값을 각각 사용하기 때문에 3차원 벡터다.'
    - 인과관계가 있는 복문 ∴ 두 문장으로 나누기
      - → '입력데이터는 색상 RGB 값을 각각 사용한다. 그래서 입력데이터는 3차원 벡터다.'
    - + ) 그래픽 프로그램을 이해하는 사람에게 굳이 제공하지 않아도 되는 정보는 제외하기
      - → '입력데이터는 3차원 벡터다.' 

# 서술식, 개조식, 도식의 차이
개발자의 생각을 글로 표현하는 방법 3가지 : 서술식, 개조식, 도식
1. 서술식 : '~다'로 끝나는 완전한 문장으로 구성된 글
  - 무엇을 설명하거나 논증할 때 주로 사용하는 방식
  - 개발 가이드 문서
2. 개조식 : 종결어미(예:'~다') 대신 명사(예:완료, 증대 등)나 용언의 명사형(예:'~했음')으로 끝내는 것
  - 신문의 헤드라인을 쓰거나 어떤 사항을 나열할 때 사용
  - 주로 릴리스 문서나 장애 보고서를 쓸 때 사용
  - 여러 사항이 유사한 패턴으로 반복될 때는 개조식으로 쓰는 것이 보기좋고 이해하기 쉽다.
  - 단점 : 중복, 누락
    - 표(table) ⇒ 중복, 누락 방지 + 각 항목의 차이 명확화
3. 도식 : 사물의 구조나 관계, 상태를 그림이나 서식으로 보여주는 것
  - 가장 간단한 형태 : 행과 열로 이루어진 표(table)
  - 도표(graph/chart) : 행렬에 글 + 그림
  - 도식은 주로 표(table)을 의미함

- 가장 중요한 것? 내용과 형식이 일치해야 함
  - 서술식 : 줄거리가 있는 설명 or 이야기
  - 개조식 : 여러 가지 종류의 항목과 내용 반복, 서술식에서 강조가 필요한 내용
  - 도식 : 각 항목 및 사항의 관계를 명확히 규정하고자 함

# 개조식 서술 방식과 글머리 

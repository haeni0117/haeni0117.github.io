---
title: "Teachable Machine으로 AI 과일도감 제작하기 - 1"
categories:
  - Tech_Trend
tags:
  - metaverse
last_modified_at: 2021-10-14T08:06:00-05:00
---

# Teachable Machine으로 AI 과일도감 제작하기

---

## Teachable Machine이란?

Teachable Machine은 구글에서 2019년 출시한 서비스로, 머신러닝 모델의 학습 과정을 쉽게 이해하고 직접 모델을 생성해 활용할 수 있다. <span style="color:purple">코딩을 할 줄 몰라도, 수학을 잘하지 못해도 쉽게 활용할 수 있는 것이 가장 큰 특징이다.</span> 학습에만 머물지 않고, 프로젝트에서 생성한 학습 모델을 다양한 방법과 용도로 활용하는 것도 가능하다.

## Teachable Machine 사이트 접속

따로 회원가입이 필요하지는 않다. 아래 참고자료에 teachablemachine공식문서 링크를 클릭하면 이동할 수 있다. 들어가면 아래와 같은 화면을 볼 수 있다.

![image](https://user-images.githubusercontent.com/69496570/137283833-f94662d3-0ed3-4b0f-81d4-b8db48c6539d.png)

- 이미지프로젝트, 오디오프로젝트, 포즈프로젝트가 있다. 이번 플젝에서는 이미지 프로젝트를 사용할 것이다. 근데 개인저긍로는 저 포즈프로젝트가 되게 흥미로워보인다. 기본적으로 머신러닝(machine learning)기반이다. 머신러닝이라고 하면 이름부터 어렵다고 거부감을 느끼는 사람들이 많을텐데, ui도 되게 심플하고 user-friendly하다고 느꼈다.
- 이미지 프로젝트를 클릭하면 다음과 같은 화면이 나온다. 웹캠, 또는 직접 이미지 업로드를 통해서 인공지능을 학습시킬 수 있다.
  ![image](https://user-images.githubusercontent.com/69496570/137284717-68fbe616-093b-415a-a8e3-17fea3c9b5a1.png)

## 이미지 학습시키기

- 조코딩님은 웹캠을 통해서 토마토와 사과를 구별하는 학습을 진행했다. 얼핏보면 둘 다 비슷한 사이즈인데다 색깔도 붉은색이라서 과연 인공지능이 이걸 구분할 수 있을지 엄청 궁금했다.

- 지금 사과를 학습시키고 있는 중인데, 여러각도에서 본 사과데이터를 입력하여(200장 정도의 이미지) 사과를 인공지능한테 가르쳤다.
  ![image](https://user-images.githubusercontent.com/69496570/137285549-64709fe3-f9be-4e9f-aa78-f722f3e2ecad.png)
- 나는 처음에 지금 가지고 있는 무선마우스와 스마트폰을 이용해서 학습을 진행했는데, 색깔과 모양도 다 다르고 의미없는 일을 하는 것 같아서 샘플을 다 지우고 주제를 바꿨다.
- mask class와 nomask class에 웹캠을 통해 이미지를 샘플링했더니 아까 보다 훨씬 정확하게 이미지 판별을 했다.
  <img width="1440" alt="스크린샷 2021-10-14 오후 6 11 27" src="https://user-images.githubusercontent.com/69496570/137288121-5ca744a9-43fb-45cf-8b51-dedab9564ec8.png">
  <img width="1430" alt="스크린샷 2021-10-14 오후 6 11 43" src="https://user-images.githubusercontent.com/69496570/137288147-a57fdbfa-a93d-4903-acc5-ab8350d599c8.png">
  <img width="1440" alt="스크린샷 2021-10-14 오후 6 11 51" src="https://user-images.githubusercontent.com/69496570/137288159-5b5b2660-66a8-40d6-9cd3-c94ae67da10b.png">
- 이런식으로 딥러닝기반 마스크 출입통제 알고리즘같은 게 만들어지는구나 싶었다.
- 마스크 인식 서비스들을 구글링하니 아래와 같은 플젝을 한 사람을 찾았다. 2학년이라는데, 나도 2학년이니까 열심히 세상에 의미있는 것들을 만들어봐야지.

---

## 참고자료

- 조코딩님 유튜브
  - [세상에서 가장 쉬운 인공지능 만들기 1탄 | Teachable Machine으로 AI 과일도감 제작하기](http://img.youtube.com/vi/USQGTW34lO8&list=PLU9-uwewPMe1AsOwlodmuaap99KH_483a/0.jpg)
    ![image](https://user-images.githubusercontent.com/69496570/137283016-62f3f002-38e5-4be7-8806-83d691d23dff.png)
- [구글에서 발행한 teachable machine 서비스 공식문서](https://teachablemachine.withgoogle.com/train)

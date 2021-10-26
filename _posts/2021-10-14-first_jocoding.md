---
title: "Teachable Machine으로 마스크 썼는지 판별하는 웹사이트 만들기"
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

## 테스트
- 코로나 시국이니 사람이 마스크를 썼는지 안썼는지 판단해보기로 주제 바꿈.
- mask class와 nomask class에 웹캠을 통해 이미지를 샘플링했더니 아까 보다 훨씬 정확하게 이미지 판별을 했다.


## 모델추출(Export)

![image](https://user-images.githubusercontent.com/69496570/138962445-58fc5a1a-32c1-4464-8797-defba12affa9.png)

- 텐서플로(tensorflow)란?
  - <mark>텐서플로(TensorFlow)는 구글(Google)에서 만든, 딥러닝 프로그램을 쉽게 구현할 수 있도록 다양한 기능을 제공해주는 라이브러리</mark>다.
  - 머신러닝에 대해 자세히 알지 못해도 이 라이브러리를 사용하면 쉽게 프로그램에 적용시키는 것이 가능해진다.
  - 텐서플로 자체는 기본적으로 C++로 구현 되어 있으며, 아래의 그림과 같이 Python, Java, Go 등 다양한 언어를 지원한다. 하지만, 파이썬을 최우선으로 지원하며 대부분의 편한 기능들이 파이썬 라이브러리로만 구현되어 있어 Python에서 개발하는 것이 편하다.
  - [TensorFlow 공식 사이트](https://www.tensorflow.org/?hl=ko)

## 모델 다운로드

- 모델은 tesorflow,tensorflow.lite,tensorflow.js로 가져갈 수 있다.
  ![image](https://user-images.githubusercontent.com/69496570/137291033-407a316e-8507-419f-a6e1-ab913f2ba67e.png)
- 다운로드받은 파일을 압축풀기를 한다. 그러면 아래와 같은 3개의 파일이 있다. - 우리가 처음 학습시킬 때 웹캠으로 찍은 이미지를 정말 많이 사용해서 용량이 크지 않을까?리는 생각을 할 수도 있지만, 샘플은 저장되지 않고 샘플을 기반으로 학습한 모델만 export되기 때문에 용량은 그렇게 크지 않다.
  ![image](https://user-images.githubusercontent.com/69496570/137291239-24d80462-bc0f-4e7c-98b3-b37719415e42.png)

## 머신러닝을 사용해서 웹서비스 만들기

- 해당 폴더에 `index.html`이라는 파일을 생성시킨다. 나는 여기에서부터 Vscode를 사용하여 편집했다.
  - visual studio, 메모장 등등 말 그대로 '편집'기이기만 하면 된다.
- html 편집꿀팁 : `! + tab`으로 html의 기본포맷을 가지고 올 수 있다.
  ![image](https://user-images.githubusercontent.com/69496570/137296467-c0a7d032-95e5-4a6f-919c-e459e8f0e337.png)
- body부분에 모델링 js코드를 삽입한다.
  ![image](https://user-images.githubusercontent.com/69496570/137296975-2dfb276b-5cc9-4bf7-ae67-c9861e6254b4.png)
- url코드를 보면 모델링파일들이 my_model이라는 디렉토리 안에 있기 때문에 다운받은 파일 내에 해당 파일 생성 -> 파일 위치 변경
  ![image](https://user-images.githubusercontent.com/69496570/137297556-fa807ed3-7c5e-4dc8-9142-db65165049ce.png)
- 그런데 막상 웹페이지에서 start버튼을 누르면 아무것도 작동하지 않는다. 
  - -> 문제해결을 위해 F12 -> 개발자도구에 들어가보자.
  - issue가 발생한 것을 확인할 수 있다. 
  - ![image](https://user-images.githubusercontent.com/69496570/137298050-a64a8acb-6247-4349-992c-a9767dfde027.png)
  - URL이 http나 https로 시작해야한다는 오류였다.
    ![세상에서 가장 쉬운 인공지능 만들기 1탄 _ Teachable Machine으로 AI 과일도감 제작하기 7-45 screenshot](https://user-images.githubusercontent.com/69496570/137298419-a83f5926-fceb-4157-9efc-7551fdd99a31.png)
    
## 웹페이지 deploy
- [https://app.netlify.com/teams/haeni0117/overview](https://app.netlify.com/teams/haeni0117/overview)
- ![image](https://user-images.githubusercontent.com/69496570/137301727-387eb0ff-3ace-475e-ba1c-79fe10c164c2.png)
- 위의 페이지에서 해당 폴더를 드래그앤드롭해주는 것만으로 웹페이지를 개설할 수 있다.
- ![image](https://user-images.githubusercontent.com/69496570/138963009-a16af394-5b69-4a04-a699-310cfcb5f4b9.png)
- ![image](https://user-images.githubusercontent.com/69496570/138962695-153cd232-03db-4bee-91a5-f78cebd70dd9.png)
- 지금 내가 마스크를 쓰고 웹캠을 켰는데 mask라고 정확하게 인식하는 걸 보니 잘 돌아가고 있음을 알 수 있다.

## HTML/CSS로 꾸며주기
- 포켓몬도감처럼 꾸며보자.
- ![image](https://user-images.githubusercontent.com/69496570/137302956-088b18d4-de65-4088-b2fa-b02add13a833.png)
```
async function predict() {
        // predict can take in an image, video or canvas html element
        const prediction = await model.predict(webcam.canvas);
        if (
          prediction[0].className == "MASK" &&
          prediction[0].probability.toFixed(2) > 0.9
        ) {
          labelContainer.childNodes[0].innerHTML = "마스크 착용중";
        } else if (
          prediction[0].className == "NOMASK" &&
          prediction[0].probability.toFixed(2) > 0.9
        ) {
          labelContainer.childNodes[0].innerHTML =
            "마스크를 착용하지 않으면 출입이 불가능합니다ㅠㅠ";
        } else {
          labelContainer.childNodes[0].innerHTML = "알 수 없음";
        }
        // for (let i = 0; i < maxPredictions; i++) {
        //   const classPrediction =
        //     prediction[i].className +
        //     ": " +
        //     prediction[i].probability.toFixed(2);
        //   labelContainer.childNodes[i].innerHTML = classPrediction;
        // }
      }
```
- deploy창에서 수정사항을 반영해준다.

## 마지막테스트
<img width="1022" alt="스크린샷 2021-10-14 오후 7 48 40" src="https://user-images.githubusercontent.com/69496570/137303816-f0ff044b-e5a9-4488-8e28-569ad753243d.png">
![image](https://user-images.githubusercontent.com/69496570/138963201-6c9ae6e9-90ea-4af4-88bf-abcc4a5fbff2.png)

- feedback
  - 왜 nomask는 텍스트가 안뜨는지 확인해봐야할 것 같다.
  - html/css를 더 정비해야겠다.
  - class를 늘려서 인공지능 과일도감을 만들어봐야지~
  
-----

## 참고자료

- 조코딩님 유튜브
  - [세상에서 가장 쉬운 인공지능 만들기 1탄 | Teachable Machine으로 AI 과일도감 제작하기](http://img.youtube.com/vi/USQGTW34lO8&list=PLU9-uwewPMe1AsOwlodmuaap99KH_483a/0.jpg)
    ![image](https://user-images.githubusercontent.com/69496570/137283016-62f3f002-38e5-4be7-8806-83d691d23dff.png)
- [구글에서 발행한 teachable machine 서비스 사이트s](https://teachablemachine.withgoogle.com/train)
- 이런식으로 딥러닝기반 마스크 출입통제 알고리즘같은 게 만들어지는구나 싶었다.
- 마스크 인식 서비스들을 구글링하니 아래와 같은 플젝을 한 사람을 찾았다. 2학년이라는데, 나도 2학년이니까 열심히 세상에 의미있는 것들을 만들어봐야지.

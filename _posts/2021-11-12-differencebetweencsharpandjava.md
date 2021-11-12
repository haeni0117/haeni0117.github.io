---
title: "C#과 Java차이점 + 개발분야 아카이빙"
categories:
  - C#
  - JAVA
tags:
  - C#
  - JAVA
last_modified_at: 2021-11-11T08:06:00-05:00
---
# C# vs Java
## 1. 처리속도의 차이
- <span style="color:red">C#은 Native언어가 아니다</span>보니 MS의 .Net의 CLR(Common Language Runtime)에 있는 JIT(Just-In_Time) 컴파일러를 거쳐서 Native코드로 변환되어 실행한다.
  - Native 언어에 비해 step이 추가적으로 존재한다 -> 비용 증가
- 위 현상(네이티브 코드로 변환 => 비용증가)이 <span style="color:red">성능하락</span>의 원인중 하나로 꼽히기도 한다.
- 간단한 테스트 결과 Java는 JVM을 통한 컴파일러 과정이 있음에도 불구하고 C#에 비해서 빠른 성능을 보여주었다.
  - 단순 반복문 사용테스트
    - C# : 10억번 반복 시 1.8초, 100억번 반복 시 15.5초
    - JAVA : 10억번을 반복 시 1초, 100억번을 반복하였는데 3초
  - 무겁지 않은 프로그램은 사실 크게 차이가 없지만(-> 10억번 반복 : C#(1.8s) vs JAVA(1s)) 단순하게 for문을 여러번 돌리는 테스트만 진행해봐도 반복횟수가 늘어날수록(프로그램이 무거워질수록) 완료되기까지의 속도가 서로 많이 차이나는것을 볼 수 있다.
  - 즉, 간단한 프로그램에서는 별 차이가 없으나, 프로그램이 무거워질수록 성능차이가 커진다.
- <u>결론 : C#이 네이티브 언어가 아니고, JAVA는 JVM을 통한 컴파일러 과정이 존재함에도 성능이 좋아서 처리속도는 JAVA가 C#보다 낫다. 프로그램 매스가 커질수록 성능 갭은 커진다.</u>

## 2. 프로그램 디자인 편의성
- C# : Winform, WPF와 같은 방식으로 개발하게 되면 아래와 같이 편하게 디자인을 진행할 수 있다. 
  - Winform : 기존의 콘솔 창을 사용하는 CUI(Character User Interface)와 다르게 <span style="color:blue">GUI(Graphical User Interface)를 제공</span>하는 것이 Windows Form -> 줄여 말하자면 윈폼(Winform)
  - WPF((Windows Presentation Foundation) : <span style="color:blue"> 데스크톱 클라이언트 애플리케이션을 만드는 UI 프레임워크</span>이다.
  - WPF 개발 플랫폼은 애플리케이션 모델, 리소스, 컨트롤, 그래픽, 레이아웃, 데이터 바인딩, 문서 및 보안을 포함하여 다양한 애플리케이션 개발 기능 세트를 지원한다.
- JAVA : Java는 디자인을 C#처럼 간단하게 하기 쉽지 않다. 
  - 쉽지 않은 이유 
    - Java는 UI 디자인을 초기에 나온 AWT 혹은 후에 개선되어 나온 Swing을 이용하여 둘 다 <span style="color:red">코드로 디자인</span>을 하기 때문이다.
    - Java는 Swing의 클래스인 JFrame을 상속받은 클래스 안에 코드로 직접 해주어야하는 약간의 불편함이 있다.
- <u>결론 : 프로그램 디자인 편의성은 코드 없이 Winform과 WPF와 같은 방식이 제공되는 C#이 직접 코드를 작성해야하는 JAVA보다 낫다.</u>

## 3. 숫자 형태의 값 처리
- C# : 대응하는 변수 등에 타입만 맞춰주면 특별한 일 없이 오류가 뜨지 않는다.
- JAVA : 별도의 선언을 통해서 해당 숫자값이 해당 타입이라는 것을 인식하게 만들어야 한다.
- 예제코드 ; long타입을 가지는 숫자값
  - <img width="1023" alt="스크린샷 2021-11-12 오후 12 46 07" src="https://user-images.githubusercontent.com/69496570/141405676-070c4e7e-9bbf-41d3-b431-64ec8ff60346.png">
  - <img width="1023" alt="스크린샷 2021-11-12 오후 12 46 24" src="https://user-images.githubusercontent.com/69496570/141405686-5ed03d3e-4360-43c4-b041-733a14811bbf.png">

# Native 언어
- 컴파일, 링크, 빌드를 통해 CPU가 이해하는 기계어로 바꾸어 소프트웨어를 생성하는 언어
- Native 언어 외에도 ‘인터프리터 언어’, ‘Hybrid 언어’가 있다.

# 인터프리터 언어
- 프로그래밍 언어의 소스 코드를 바로 실행하는 프로그램
  - Python : 인터프리터가 실행하는 고급 언어
  - 즉 컴파일, 링크, 빌드 같은 행위가 전혀 필요 없다. 따라서 인터프리터로 해석되는 고급 언어는 <span style="color:red">반드시 느릴 수 밖에 없다.</span>
    - 느린 이유?
      - C++(native lang)로 작성된 소스 코드 : 컴파일 => 목적파일(기계어에 준함)
        - 링커를 통해 실행파일(기계어)이 되었다.
      - Python(interpreter lang)은 인터프리터가 사람의 언어를 즉각적으로 해석 => 기계어로 바꾸어 실행한다. 따라서 C++에 비해 해석하는 비용 증가
        -  Python은 정확하게 파고들면 인터프리터 언어라고 하기엔 애매하다고 한다. 
        -  > 최근에 많이 보게 되는 질문 중 하나가 ‘파이썬은 인터프리터 언어입니까? 컴파일언어입니까?’라는 것이다. 개인적으로 이 질문은 사람을 참 난감하게 하는데, 어떻게 답해야하나에 앞서 아직까지도 이 개념을 이렇게 잘못 가르치는 교재 혹은 과정이 대부분이라는 점 때문이다. 그럼 인터프리터 언어와 컴파일 언어가 무엇인지 알아보고, 과연 파이썬은 인터프리터 언어인지 생각해보자.
참고로, 보통 나는 이 질문에 ‘반만 맞다’고 말하거나 더 이상의 설명이 귀찮은 경우에는 ‘통상 인터프리터 언어라고 합니다.’라고 답한다.

- 프로그래밍 언어의 소스 코드를 바로 실행하는 프로그램Python은 인터프리터가 실행하는 고급 언어입니다. 즉 컴파일, 링크, 빌드 같은 행위가 전혀 필요 없습니다. 따라서 인터프리터로 해석되는 고급 언어는 반드시 느릴 수 밖에 없습니다s




## 출처
- [이 세상엔 하고싶은 것, 해야할 것이 많다 - JAVA와 C#의 차이점](https://skfkdkdlaos.tistory.com/4)
- [Developer Lee - 프로그래밍 언어란?](https://unagi44.wordpress.com/tag/native-%EC%96%B8%EC%96%B4/)
- [WireFrame - 파이썬은 인터프리터언어입니까?](https://soooprmx.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%80-%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0%EC%96%B8%EC%96%B4%EC%9E%85%EB%8B%88%EA%B9%8C/)
- [Microsoft Docs - WPF란?](https://docs.microsoft.com/ko-kr/visualstudio/designers/getting-started-with-wpf?view=vs-2022)

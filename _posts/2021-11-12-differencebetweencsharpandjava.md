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
## 2. 프로그램 디자인 편의성
- C# : Winform, WPF와 같은 방식으로 개발하게 되면 아래와 같이 편하게 디자인을 진행할 수 있다. 
  - Winform : 기존의 콘솔 창을 사용하는 CUI(Character User Interface)와 다르게 GUI(Graphical User Interface)를 제공하는 것이 Windows Form -> 줄여 말하자면 윈폼(Winform)
  - WPF
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

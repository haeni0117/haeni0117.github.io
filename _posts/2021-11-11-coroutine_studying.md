---
title: "[unity] 코루틴(Coroutine)함수"
categories:
  - UNTIY
tags:
  - coroutine function
last_modified_at: 2021-11-11T08:06:00-05:00
---
Update 함수는 게임 오브젝트가 활성화된 상태에서 매 프레임 호출되어 수행된다. 그래서 유니티 엔진으로 게임을 만들 때는 대부분의 게임 동작을 Update 함수에서 작동하도록 구현한다.
- 한계 : Update 함수는 <mark>멈추지 않고 계속해서 동작하는 함수이기 때문에 여기서 일시적으로 돌아가는 서브 동작을 구현하는 것과 어떤 다른 동작이 처리되는 것을 기다리는 기능</mark>을 구현하기는 매우 까다롭다.



## 출처
- [베르의 프로그래밍 노트 - Programming 코루틴(Coroutine) 다루기](https://wergia.tistory.com/219)


---
title: "[인디게임 A.I 제작기] 인벤토리 창 구성"
categories:
  - UNITY
tags:
  - gamedevelopment, AI
last_modified_at: 2021-10-16T08:06:00-05:00
---
# [인디게임 A.I 제작기] 인벤토리 창 구성
- <mark>인벤토리(inventory)</mark>란?
  - 인벤토리란 원래뜻을 알아보면 목록 혹은 보유자산과 같은 의미의 어원인과 inventory와 같다.
- 우리 게임은 총 3가지의 인벤토리 창으로 구성되어 있다. -> 도구창, 합성창, 분해창


## 도구창
![도구창 (도구)_1@4x](https://user-images.githubusercontent.com/69496570/137615857-a5b0e183-a99e-40dd-98ac-9886637b9767.png)
- 도구창은 <mark>아이템 사용</mark>에 관한 기능을 수행하는 창이다. 게임 진행중 특정 순간에 도구를 사용해야만 다음으로 넘어갈 수 있다. (만약 도구 사용이벤트를 수행하지 않는다면 다음으로 넘어갈 수 없다.)
- 인벤토리 창에 관한 액션들을 명확히 정하지 않아서 프로그래밍하는데에 의문점이 많았는데 팀원 중에 게임개발과정 국비교육과정을 듣고 계신 분이 있어서 UI flow chart를 만들어주셨다.
  - UI flow chart(UI 플로우차트) : [UX 디자인의 설계도 : IA와 플로우 차트 그리고 화면 설계(by Megi)](https://brunch.co.kr/@megigames/5) 
  - 위 브런치 글에서 ux디자인에 대한 정보를 많이 얻을 수 있었다. 역시 실무하면서 배우는 게 정말 많다고 느낀다. ui/ux디자인에 관한 부분은 다른 글에서 다시 정리하면서 다뤄봐야겠다
- 도구창 UX flow chart 
  - <img width="1164" alt="스크린샷 2021-10-17 오후 4 40 13" src="https://user-images.githubusercontent.com/69496570/137616997-42359957-a654-4545-8353-4ed5e425c1ad.png">
  - <img width="1152" alt="스크린샷 2021-10-17 오후 4 40 21" src="https://user-images.githubusercontent.com/69496570/137617001-d0e53344-5552-4ba9-9164-7214af4b0bb9.png">
  - <img width="1407" alt="스크린샷 2021-10-17 오후 4 40 35" src="https://user-images.githubusercontent.com/69496570/137617004-3c589429-8d85-4bde-8caf-e534137e640d.png">
  - <img width="1152" alt="스크린샷 2021-10-17 오후 4 40 46" src="https://user-images.githubusercontent.com/69496570/137617008-b968d1cb-8e23-4ac5-b2b6-180a5012151c.png">

## 분해창
![도구창 (분해)_1@4x](https://user-images.githubusercontent.com/69496570/137615860-ec1ffe45-27ac-4e5f-b19a-54511fa47259.png)
- 분해창 UX flow chart 
  - <img width="1144" alt="스크린샷 2021-10-17 오후 4 42 22" src="https://user-images.githubusercontent.com/69496570/137617101-ceded985-0de4-4565-805c-286d7b72a282.png">
  - <img width="1147" alt="스크린샷 2021-10-17 오후 4 42 29" src="https://user-images.githubusercontent.com/69496570/137617102-a5f67abc-a5ee-4607-aac6-6df783cb3397.png">
  - <img width="1146" alt="스크린샷 2021-10-17 오후 4 42 40" src="https://user-images.githubusercontent.com/69496570/137617104-c43a1a94-a835-4518-a911-54c35ba15aeb.png">
  - <img width="1145" alt="스크린샷 2021-10-17 오후 4 42 48" src="https://user-images.githubusercontent.com/69496570/137617105-112d7e48-fa51-4ce3-a831-6ac9e415f1bd.png">
  - <img width="1144" alt="스크린샷 2021-10-17 오후 4 43 04" src="https://user-images.githubusercontent.com/69496570/137617107-773fe113-7b91-4068-82f1-3ddca5947223.png">
  - <img width="1146" alt="스크린샷 2021-10-17 오후 4 43 13" src="https://user-images.githubusercontent.com/69496570/137617108-9cd320d3-5fd0-496c-b083-6924164f7a0d.png">


## 합성창
![도구창 (합성)_1@4x](https://user-images.githubusercontent.com/69496570/137615861-6436d448-3983-443a-83de-f1eefe7bc11e.png)

- 합성창은 <mark>아이템 합성</mark>에 관한 기능을 수행한다. 합성창이니 아이템합성에 관한 기능을 수행하는 것은 당연한 이야기이지만, 어떤 메커니즘으로 아이템이 합성되는지에 대해 설명하도록 하겠다.

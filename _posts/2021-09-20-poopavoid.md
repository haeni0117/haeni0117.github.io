---
title: "유니티로 똥피하기 게임 제작일지 - 1"
excerpt: "Dev GomDol님의 제작영상을 시청 후 똥피하기 게임 제작과정을 정리하였습니다."

categories:
  - UNITY
tags:
  - Blog
last_modified_at: 2019-04-13T08:06:00-05:00
---

휴학도 했겠다, 실력을 늘리는 가장 최고의 방법은 직접 프로젝트를 해보는 것이라고 생각하기 때문에 간단한 미니게임이라도 혼자서 만들어보면서 UNITY실력을 올려야겠다는 생각을 했다. 아직 2D도 완전히 자유자재로 다루는 것도 아닐 뿐더라, 물리엔진까지 다루려면 갈 길이 멀다. github에 들어온지 4주 정도 된 것 같다. git태기라고 해야할까... 이제 다시 열심히 개발해보려고 한다. 아자아자!!

UNITY를 사용하는 사람이라면 누구나 그렇겠지만, 똑같은 아이콘이지만 흰색 배경인 UNITY HUB와 검은 배경인 UNITY 두 개 모두 설치되어 있어야 원활한 진행이 가능하다. 예전에 UNITY Hub가 없었을 시절에는 개발자가 일일이 설정해주는 과정이 필요했었다는데, 유니티 허브가 존재하는 시대에 개발할 수 있어서 얼마나 다행인지 모른다. 
### 🐥 Unity Hub에서 프로젝트 생성하기 

유니티 허브(흰색 배경)에 들어가면 이렇게 진행중인 프로젝트를 볼 수 있고 오른쪽 상단에 있는 <b>[추가]</b>버튼을 통해서 새로운 프로젝트를 생성할 수 있다.
<img width="974" alt="poopavoid1" src="https://user-images.githubusercontent.com/69496570/133953148-2cfbc1d6-6708-4b9b-90ea-f6af1b90ffcd.png">
우리가 만들 똥피하기 게임은 단순한 2D게임이기 때문에 2D로 지정해 준 후 프로젝트를 만들어보자.

### 🐥 타일맵(Tilemap)과 팔레트(Palette)생성하기

프로젝트를 열면 아래와 같은 빈프로젝트가 생성된다. 마우스 오른쪽 버튼을 클릭해서 `2D Object -> Tilemap -> Rectangular`을 선택해서 hierarchy창에 타일맵을 만들어준다. 
타일맵(Tilemap)이라는 것은 Unity 2017.2 버전부터 공식적으로 추가된 시스템으로 한정된 스프라이트(Sprite)리소스를 효과적으로 조합하여 배치하여 스테이지(Stage)의 필드(Field)를 구성할 수 있는 2D 에디터이다. 타일맵을 생성하면 타일맵의 이름을 ground로 설정해주자. 우리가 이 타일맵으로 할 것은 똥이 떨어지는 상황에서 플레이어가 이동할 ground가 될 것이므로 semantic하게 이름을 지어주는 게 좋다.

✨`semantic` : 의미론적인 -> 변수명,태그 등을 프로그램에서 쓰이는 역할이나 성격에 맞게 정의해주는 것을 의미한다. 아무 단어나 변수명으로 설정하기 보다는 시맨틱한 변수명으로 정의하는 게 더 바람직하다.
<img width="615" alt="스크린샷 2021-09-21 오후 7 53 56" src="https://user-images.githubusercontent.com/69496570/134303197-5923af2b-1a9c-4586-9b54-8ff2f7fcddcd.png">

그 후 `create new palette`를 통해 새로운 팔레트를 생성해준다.

<img width="343" alt="스크린샷 2021-09-21 오후 7 51 55" src="https://user-images.githubusercontent.com/69496570/134303160-bb54e3b2-c253-4407-8ae5-9384553f74db.png">
<img width="1440" alt="스크린샷 2021-09-21 오후 7 53 00" src="https://user-images.githubusercontent.com/69496570/134303181-7080149c-b728-4bf1-9f98-54a281ae436a.png">
<img width="339" alt="스크린샷 2021-09-21 오후 7 53 08" src="https://user-images.githubusercontent.com/69496570/134303192-03275c53-3a14-471e-be6c-89809cdc531b.png">

<img width="1101" alt="스크린샷 2021-09-21 오후 7 54 11" src="https://user-images.githubusercontent.com/69496570/134303201-66fe3a09-ac5a-468e-8a00-aa44eac14612.png">
<img width="1165" alt="스크린샷 2021-09-21 오후 7 54 26" src="https://user-images.githubusercontent.com/69496570/134303203-6a9083a1-46c1-4b2f-b152-72f8ea0844b3.png">
<img width="84" alt="스크린샷 2021-09-21 오후 7 54 59" src="https://user-images.githubusercontent.com/69496570/134303210-c9458a38-d07a-4f94-9abc-1d5ff754a901.png">
<img width="338" alt="스크린샷 2021-09-21 오후 7 59 21" src="https://user-images.githubusercontent.com/69496570/134303212-ed386d3f-29aa-419b-9143-3f7aa42b5d23.png">
<img width="831" alt="스크린샷 2021-09-21 오후 8 00 02" src="https://user-images.githubusercontent.com/69496570/134303213-e8ab3d95-c183-47e3-87b2-5f07c40cd84e.png">
<img width="299" alt="스크린샷 2021-09-21 오후 8 03 42" src="https://user-images.githubusercontent.com/69496570/134303214-00f91c4a-bfa2-49d2-ab4a-3cc42dd42049.png">
<img width="1440" alt="스크린샷 2021-09-21 오후 8 04 17" src="https://user-images.githubusercontent.com/69496570/134303215-36087db4-623d-4753-9783-1143ffe0f008.png">
<img width="337" alt="스크린샷 2021-09-21 오후 8 05 10" src="https://user-images.githubusercontent.com/69496570/134303219-e54a1693-8a1a-47c4-a3b4-53cec6f1eab7.png">
<img width="337" alt="스크린샷 2021-09-21 오후 8 05 40" src="https://user-images.githubusercontent.com/69496570/134303221-7989dc49-0fe7-4bad-bb2c-52877d899ff2.png">
<img width="339" alt="스크린샷 2021-09-21 오후 8 06 18" src="https://user-images.githubusercontent.com/69496570/134303223-0ab90600-52c1-4998-ac24-f2e24165ef48.png">
<img width="322" alt="스크린샷 2021-09-21 오후 8 06 35" src="https://user-images.githubusercontent.com/69496570/134303226-4479464a-06fe-4bb9-9f55-22523b4f70e1.png">
<img width="333" alt="스크린샷 2021-09-21 오후 8 07 17" src="https://user-images.githubusercontent.com/69496570/134303228-470b884b-9a13-417b-9ddb-5e7b3a7d946a.png">
<img width="1242" alt="스크린샷 2021-09-21 오후 8 07 24" src="https://user-images.githubusercontent.com/69496570/134303230-9209ecbd-0667-4c6b-ad6d-71d5b2861564.png">
<img width="338" alt="스크린샷 2021-09-21 오후 8 08 32" src="https://user-images.githubusercontent.com/69496570/134303231-9df1175e-7e9e-40ba-bf49-6dc8140ddbad.png">
<img width="334" alt="스크린샷 2021-09-21 오후 8 08 58" src="https://user-images.githubusercontent.com/69496570/134303232-ce4e605f-c8b0-4441-875e-35f7d0563c6a.png">
<img width="410" alt="스크린샷 2021-09-21 오후 8 09 56" src="https://user-images.githubusercontent.com/69496570/134303233-b43e5d85-f1af-4c32-9b0a-f2e6eb5c1248.png">
<img width="394" alt="스크린샷 2021-09-21 오후 8 10 57" src="https://user-images.githubusercontent.com/69496570/134303236-8e73672c-684c-421f-a008-3c77eccc9b78.png">
<img width="405" alt="스크린샷 2021-09-21 오후 8 11 23" src="https://user-images.githubusercontent.com/69496570/134303238-286bb4cb-78c3-40b3-b697-4e117578e1df.png">
<img width="1105" alt="스크린샷 2021-09-21 오후 8 11 53" src="https://user-images.githubusercontent.com/69496570/134303242-e53498df-43e2-4ee6-b398-fedea1e7af31.png">
<img width="1440" alt="스크린샷 2021-09-21 오후 8 32 10" src="https://user-images.githubusercontent.com/69496570/134303246-b35d83df-bfb3-4eda-b652-1563768850f7.png">
<img width="1440" alt="스크린샷 2021-09-21 오후 8 42 28" src="https://user-images.githubusercontent.com/69496570/134303248-847d70a7-4ab8-4e68-a66c-82f1d62607a9.png">

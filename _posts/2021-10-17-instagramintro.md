---
title: "인스타그램 클론코딩 - intro"
categories:
  - webdevelopment, front-end,
tags:
  - gamedevelopment, AI
last_modified_at: 2021-10-17T08:06:00-05:00
---

# intro

## 수업설명

- 수업목표 : 인스태그램 그대로 구현 -> html,css는 뼈대구성만 있으면 간단하게 할 수 있다.
- Editor : webstorm(유료), phpstrom 사용
  - 본인이 사용하고 싶은 에디터써도 OK -> 난 VScode 사용할 것이다.

## 디렉토리 구성

- css 디렉토리 생성
  - resetcode가 필요하다. -> `reset.css`
  - 기본적으로 가지고 있는 코드(여백 등)이 있기때문에 이를 초기화해주는 기능을 한다.
  - [CSS Tools : Reset CSS](https://meyerweb.com/eric/tools/css/reset/) : 'reset css'라는 키워드로 구글링하면 사이트 찾을 수 있다.
    ![image](https://user-images.githubusercontent.com/69496570/137624120-19f0b24a-7866-4691-aa8b-7f152981d27f.png)
  - `reset.css`를 css디렉토리에 넣어준 후 `index.html`파일의 head 영역에 넣어준다.
  - 폰트는 monaco로 지정해준다.
    - mac에서 monaco폰트가 monospace 즉, 간격이 일정한 폰트이기 때문이다.
    - monospace font가 가독성이 좋다고 한다.
- js 디렉토리 생성
- `index.html` 파일 생성
  - html 기본구조 가져오려면 `!+tab` 단축키 사용하면 된다.

## HTML frame 구성

- 인스타그램 클론코딩을 할 때 웹페이지를 본다면 크게 3가지 영역으로 나눌 수 있다.
- 큰 뼈대를 본 다음에 세세한 영역으로 들어가면 코딩하기 쉬워진다.

### header

![image](https://user-images.githubusercontent.com/69496570/137624415-afe2d3c9-a7c2-48a9-b515-4d426596a108.png) - header를 좀 더 자세히 보자. - inner : 모든 요소들을 감싸고 있는 inner가 존재한다. 그리고 inner는 다시 3가지 요소로 구분된다. 1. logo : 인스타그램 로고 2. 검색창 3. 아이콘창

### container

![image](https://user-images.githubusercontent.com/69496570/137624487-6741e4e8-4ea6-4017-9f48-99046653636c.png)

- leftbox
  ![image](https://user-images.githubusercontent.com/69496570/137624541-06ec73c9-bd75-47f9-8a93-7483e0eea348.png)
- rightbox
  ![image](https://user-images.githubusercontent.com/69496570/137624548-56c3a5c1-921c-4ec7-a848-1cd19bf35289.png)

# header

- 코딩을 하기전에 body영역 안에 container영역을 만들어주는 것이 좋다.
- 그리고 body태그는 되도록 건드리지 않는 것이 좋다. 무언가를 바꿔주고 싶다면 body태그 안에 태그들을 만들어서 변경하도록 하자.
- semantic태그인 section태그를 사용해서 container 영역을 만들어주자.
- head영역에 header영역을 만들어주는 게 아니다!!! 크게 3가지 영역으로 나눴던 모든 부분들은 모두 body영역에 구현해줄 것이다.

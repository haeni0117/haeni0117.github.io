---
title: "인스타그램 클론코딩 - intro"
categories:
  - webdevelopment, front-end,
tags:
  - gamedevelopment, AI
last_modified_at: 2021-10-17T08:06:00-05:00
---

# 1강 - intro

## 수업설명

- 수업목표 : 인스타그램 그대로 구현 -> html,css는 뼈대구성만 있으면 간단하게 할 수 있다.
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

![image](https://user-images.githubusercontent.com/69496570/137624415-afe2d3c9-a7c2-48a9-b515-4d426596a108.png) - header를 좀 더 자세히 보자. - inner : 모든 요소들을 감싸고 있는 inner가 존재한다. 그리고 inner는 다시 3가지 요소로 구분된다.

1. logo : 인스타그램 로고
2. 검색창
3. 아이콘창

### container

![image](https://user-images.githubusercontent.com/69496570/137624487-6741e4e8-4ea6-4017-9f48-99046653636c.png)

- leftbox
  ![image](https://user-images.githubusercontent.com/69496570/137624541-06ec73c9-bd75-47f9-8a93-7483e0eea348.png)
- rightbox
  ![image](https://user-images.githubusercontent.com/69496570/137624548-56c3a5c1-921c-4ec7-a848-1cd19bf35289.png)

---

# 2강 - header

- 코딩을 하기전에 body영역 안에 container영역을 만들어주는 것이 좋다.
- 그리고 body태그는 되도록 건드리지 않는 것이 좋다. 무언가를 바꿔주고 싶다면 body태그 안에 태그들을 만들어서 변경하도록 하자.
- semantic태그인 section태그를 사용해서 container 영역을 만들어주자.
- head영역에 header영역을 만들어주는 게 아니다!!! 크게 3가지 영역으로 나눴던 모든 부분들은 모두 body영역에 구현해줄 것이다.
- 결국 `body -> container -> header -> inner` 로 계층이 구성된다.

## header css 구현

- 강의에서 position을 absolute로 설정하면 x,y를 둘 중 하나는 설정해줘야한다고 했는데 x : right or left / y: top or bottom 으로 설정해라는 의미인 것 같다.

```
#header{
  width : 100%;
  position : absolute;
  left : 0;
  top : 0;
  z-index : 999;
  background : white;
  border-bottom : 1px solid rgba(0,0,0,0.1);
}
```

- `width : 100%` : 가로폭을 풀로 채운다.
- `position : absolute` : 포지션(position)의 성질을 absolute로 설정한다.
  - 내 블로그에 CSS position에 대해 정리한 문서 있다.
- `left`,`top` : absolute 포지션 세부사항 설정
  - `absolute`자체는 '어떤 걸 조상(기준)으로 둘 지'이므로 얼마나/어떻게 이동하냐에 관한내용은 top/bottom/right/left를 통해서 설정한다.
  - 어떻게 : `top,bottom,right,left`
  - 얼마나 : ( )px
- `border-bottom` : 밑에 경계선을 하나 만든다. 그리고 경계선의 성질은 1px의 굵기인 단선(solid)이다.
- `rgba` : `rgb`는 색상코드에서 쓰는 그 RGB가 맞고 a는 투명도에 관한 값이다.
- 위의 코드만으로는 웹페이지에 아무것도 나타나지 않는다.
  - 왜냐하면 높이 값이 설정되어 있지 않기 떄문이다. 지금 상태의 높이값은 0이나 마찬가지이다.
  - 우리 눈에 보이는 사람들의 키는 적어도 0초과이다. 키가 0cm인 사람은 눈에 보이지 않는 것과 같은 원리이다.

## inner(header의 자식) css 구현

```
#header. inner{
  width : 975px;
  height : 77px;
  margin : 0 auto;
}
```

- `margin : 0 auto` : 중앙정렬
  - 그런데 margin이 0이고 auto인게 왜 중앙정렬이랑 같은 말일까?
    - 0 : 위 아래 여백을 주지 않는다는 의미이다.
    - 원래 숫자가 0이 아니라면 px인지 %인지 정확하게 적어줘야 적용가능하다. 하지만 0은 `0% = 0px = 존재하지 않음`이기 때문에 적용가능하다.
  - `auto` : 가로 중앙에 배치한다는 뜻이다. 따라서 `좌여백 = 우여백`
  - 그리고 위의 코드가 적용되지 않는 예외상황들이 존재한다.
    - [그 예외상황들에 대해 알고싶다면?](https://hansolcha.tistory.com/4)

## inner요소들(로고,검색창,아이템창) css 구현

### 1. 로고(instagram 로고)

- 유저가 어느페이지에서 무얼하고 있든 로고를 클릭하면 원래 페이지로 돌아온다.
  - 예시 : 친구랑 DM중 -> 인스타그램 로고 클릭 -> www.instagram.com 접속
  - 우리는 유저가 인스타그램 로고를 클릭하면 index.html을 다시 불러와야 한다. -> 로고에 `index.html`를 링크해야한다. -> `a`태그 사용
- HTML

```
<h1 class = "logo">
  <a href = "index.html">
  </a></h1>
```

- 아이콘 넣기
  - 이미지를 통해서 넣기
  - background를 통해 이미지 배치시키기
    - spritecow에서 가져와서 쓴다.
    - spritecow 웹사이트 : [http://www.spritecow.com/](http://www.spritecow.com/)

```
.sprite_user_icon_outline{
  display:inline-block;
  background:url('../imgs/dfghjk.png') no-repeat -277px -182px;
  width:22px;
  height:24px;
}
```

- `display : inline-block` : `display`는 `inline`속성이 있고, `block`속성이 있다. `inline-block`은 `inline`과 `block`의 성질을 모두 가지고 있는 속성이다.
  - 해당 사이트에서 CSS의 display속성에 대해 잘 설명해놓았다. -> [https://ofcourse.kr/css-course/display-%EC%86%8D%EC%84%B1](https://ofcourse.kr/css-course/display-%EC%86%8D%EC%84%B1)
- block
  - div 태그, p 태그, h 태그#, li 태그 등이 block에 해당된다.
  - 기본적으로 가로 영역을 모두 채우며, block 요소 다음에 등장하는 태그는 줄바꿈이 된 것처럼 보인다.
  - width, height 속성을 지정 할 수 있으며, block 요소 뒤에 등장하는 태그가 그 이전 block 요소에 오른쪽에 배치될 수 있어도 항상 다음 줄에 렌더링된다.

```
<style>
.block1{ width: 300px; border: 3px solid #333 }
.block2{ width: 200px; border: 3px solid #999 }
</style>

<div class="block1">1</div>
<div class="block2">2</div>
hello
```

- inline
  - 줄바꿈, width와 height 지정 불가능
  - 문서편집에서 볼드, 이탤릭, 색상, 밑줄 등 텍스트에 효과를 주기 위해 존재하는 단위라고 할 수 있다. -> 이런 효과를 더해준다고해서 줄바꿈이 일어나는 것이 아니기 때문이다.

```
<style>
.inline1{
	background: #09c;
}
.inline2{
	width: 200px; /* 이 값은 무시됩니다 */
	border: 3px solid #999;
}
</style>

<p>
	Lorem ipsum dolor sit amet, <span class="inline1">consectetur adipiscing elit</span>,
	sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
	Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
	Duis aute irure dolor in <span class="inline2">reprehenderit</span>
	in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
	Excepteur sint occaecat cupidatat non proident,
	sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
```

- inline-block
  - inline과 block의 중간속성이다.
  - 줄 바꿈이 되지 않지만 크기를 지정 할 수 있다.
    - 줄 바꿈 불가능 -> inline의 속성
    - 크기지정(width,height)가능 -> block의 속성

```
<style>
.inline-block1{
	display: inline-block;
	background: #09c;
	height: 45px;
	/* 원래 inline 요소의 높이는 글자(폰트)의 높이를 바탕으로 설정되지만,
	inline-block을 이용하면 임의로 높이 또한 설정을 할 수 있습니다. */
}
.inline-block2{
	display: inline-block;
	width: 200px; /* 이 값은 이제 정상 작동합니다 */
	border: 3px solid #999;
}
</style>

<p>
	Lorem ipsum dolor sit amet, <span class="inline-block1">consectetur adipiscing elit</span>,
	sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
	Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
	Duis aute irure dolor in <span class="inline-block2">reprehenderit</span>
	in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
	Excepteur sint occaecat cupidatat non proident,
	sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
```

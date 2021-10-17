---
title: "CSS 포지션(position) - static,relative,absolute,fixed"
categories:
  - webdevelopment, front-end,
tags:
  - gamedevelopment, AI
last_modified_at: 2021-10-17T08:06:00-05:00
---

# position

태그들의 위치를 결정하는 css이다.

## static

- 모든 태그들의 default 상태이다. 그렇기 때문에 static일 시 따로 명시하지 않아도 된다.
- 왼쪽에서 오른쪽, 위에서 아래로 쌓인다.
  - 넘버링을 한다고 했을 때의 직관적인 방향성과 같음을 기억하면 더 쉽게 이해할 수 있다.

## relative

- 태그의 위치를 살짝 변경하고 싶을 때 사용한다.
- HOW? top,right,bottom,left 속성을 사용해 위치 조절이 가능하다.
  - top태그에 5px을 설정해주면 static일 때보다 아래로 이동한다.
  - WHY? relative는 각각의 방향을 기준으로 태그 안쪽방향으로 이동한다. 바깥쪽으로 이동하게 하고 싶으면 음수값으로 설정해야한다.
- `z-index` : 스크린과의 거리에 관한 키워드이다. 값이 크면 스크린과 더 가까워진다 = 즉 레이어들 중 위로 올라가게 된다.
  - ppt에서 가장 위로 오게 한다 = `z-index`값을 가장 크게 설정한다.
  - 기본값은 0이다.

## absolute

- position : static 속성을 가지고 있지 않은 조상을 기준으로 움직인다.
  - 따라서 바로 상위 태그가 static을 속성으로 가지고 있다면 조상이 될 수 없다.
  - 그렇다면 조상 중에 포지션이 `relative`, `absolute`, `fixed`인 태그가 없다면 가장 위의 태그(body태그)가 조상이 된다. -> body태그를 기준으로 위치를 설정하게 된다.
- cf) relative는 static상태를 기준으로 주어진 픽셀만큼 움직인다.
- 조상들 중 static 속성을 가지고 있는 조상이 없을 경우
  - <img width="768" alt="스크린샷 2021-10-18 오전 12 45 40" src="https://user-images.githubusercontent.com/69496570/137634773-eac136ff-e42b-4b50-8ae2-67b8007c44d2.png">
  - <img width="764" alt="스크린샷 2021-10-18 오전 12 45 51" src="https://user-images.githubusercontent.com/69496570/137634779-11dc8c60-f478-4e59-a600-f3ccf9ee52ae.png">
- absolute가 되면 div여도 더는 width:100%가 아니라고 하는데, 이건 무슨 말인지 잘 모르겠다...........

## fixed

- 스크롤을 내려도 그 자리에 계속있는 요소들을 구현하기 위해 필요한 성질이다.
- 위 사이트에 접속해서 스크롤을 해보면 어떤 기능인지 확실히 알 수 있을 것이다 -> [fixed 구현 사이트링크](https://www.zerocho.com/category/CSS/post/5864f3b59f1dc000182d3ea1)
- 아래로 스크롤을 했을 때 게시물만 내려가고 왼쪽에 있는 사이트 주인장 프로필이랑 tag, 카테고리들은 계속 가만히 있다.
- why? fixed 되었기 때문이다
  - <img width="667" alt="스크린샷 2021-10-18 오전 12 50 21" src="https://user-images.githubusercontent.com/69496570/137635013-497767d4-a1b0-47f9-93af-7063ddb50744.png">
  - <img width="654" alt="스크린샷 2021-10-18 오전 12 50 31" src="https://user-images.githubusercontent.com/69496570/137635019-ad8cc242-f0a8-4ccb-942d-772a0f6d4f3a.png">
  - fixed도 absolute처럼 더는 div가 width: 100%가 아니다(?)

## 참고자료

- [CSS 포지션(position) by ZeroChoTV](https://www.zerocho.com/category/CSS/post/5864f3b59f1dc000182d3ea1)

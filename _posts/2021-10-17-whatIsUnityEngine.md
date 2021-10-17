---
title: "유니티 엔진과 게임 엔진"
categories:
  - UNITY
tags:
  - gamedevelopment, AI
last_modified_at: 2021-10-17T08:06:00-05:00
---

위 글은 '베르의 게임 개발 유튜브' 채널의 '유니티 엔진과 게임 엔진' 영상을 보고 개인공부목적으로 아카이빙한 글입니다.

- 해당 영상 링크 : [[리메이크] 유니티 엔진과 게임 엔진 | 유니티](https://www.youtube.com/watch?v=kEPKqJH4ahU)

# 유니티 엔진과 게임 엔진

- 유니티(UNITY)는 수많은 게임 엔진 중 하나이다.
  - e.g. 언리얼엔진

## 게임엔진(Game Engine)이란?

- 게임을 만드는 데에 도움을 주는 도구상자
- 게임엔진은 게임에 필요한 요소들을 <mark>미리 만들어두었다</mark>는 점이다.
  ![image](https://user-images.githubusercontent.com/69496570/137621551-7a701035-a9e2-41ca-b05c-2b381136365a.png) - 그래픽시스템(Graphic System) - 물리엔진(Physics) - 오디오시스템(Audio) - UI시스템(UI : user experience) - 기타(etc : network, effect, animation, input, navigation ...)

## 만약 게임엔진이 없었다면?

- 가상 공간 속에서 점->선->면 제작 프로세스를 거쳐 직접 제작해야한다.
- 물리적인 효과를 위해 충돌시스템을 새로 만들어야한다. -> 이는 ui system,audio system도 마찬가지이다.
- 실제로 초창기의 게임개발자들은 이 과정들을 직접 수행했다.
- Problem & Solution
  - Problem
    - 그러나 게임의 퀄리티가 올라갈수록 게임개발에 사용되는 시간, 비용은 증가한다는 문제가 있었다.
  - Solution
    - 그래서 이미 있는 게임을 재활용하면 게임을 더 효율적으로(시간,비용의 최소화)만들 수 있지 않을까?하는 생각
- 위의 문제해결과정(어떻게 하면 더 게임을 효율적으로 만들지에 관한 고찰)에서 도출된 결론이 바로 게임엔진(Game Engine)!
  - e.g. unity, unreal
- 따라서 게임개발자들은 게임을 만들 수 있는 시스템구현보다 게임기능구현 그 자체에 더 집중할 수 있게 되었다(훨씬 효율적)

## 유니티의 장점

- 게임제작에 필요한 많은 기능들을 제공하고 있고, 게임개발자들이 게임제작 그 자체에 집중할 수 있게 도와준다(게임엔진의 보편적 특징)
- GameObejct, Flexible Component Function, Intuitive GUI => 초급자가 쉽게 접근할 수 있다.
  ![image](https://user-images.githubusercontent.com/69496570/137622016-166c9cc5-1fce-4581-92d3-68efec2af9e3.png)
- AssetStore(에셋스토어)에서 다른 사람들이 제공하는 그래픽리소스나 기능들을 구매하여 게임개발기간을 줄일 수 있다는 장점 => 소규모개발팀, 인디게임개발팀에서 자주 사용된다. (자본이 별로 없는 개발팀)

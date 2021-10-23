---
title: "Make the 어몽어스(1) - 메인메뉴 만들기"
categories:
  - UNITY
tags:
  - gamedevelopment
last_modified_at: 2021-10-22T08:06:00-05:00
---

## 어몽어스(AmongUs)란?

《어몽 어스》는 미국의 게임 스튜디오 이너슬로스에서 2018년 6월 15일에 출시 및 발표한 온라인 다인용 소셜 디덕션 게임이다. 모바일 버전은 무료이고, PC 버전은 유료이다.이 게임은 우주와 하늘을 소재로 한 장소, 여기서 플레이어는 두 역할 중 하나를 맡게 된다

## 베르의 게임 개발 유튜브 -> Make the 시리즈

일반적으로 한 강의 당 하나의 기능을 구현하는 것을 보여줬는데, 이 시리즈는 하나의 게임을 완전하게 만드는 것을 목표로 한다.

## 구현기능 -> 메인메뉴

- 프로젝트 열기
  - 어몽어스는 2D패키지로 프로젝트를 열어준다.
    ![image](https://user-images.githubusercontent.com/69496570/138539694-863e4d0e-3435-41ad-8c4f-b79f600cb82f.png)
  - 게임을 만드는 데에 필요한 패키지를 다운로드한다.
    - window -> package manager -> Universal RP package 설치
      ![image](https://user-images.githubusercontent.com/69496570/138539876-88a1f1d4-1561-40f5-b757-7743e06cda25.png)
    - create -> rendering -> universal renderpipeline -> pipeline asset 선택
    - ![image](https://user-images.githubusercontent.com/69496570/138540019-ba43b6ea-ed4a-4495-9406-28ad56f78cee.png)
  - 다운받은 패키지를 활용하여 에셋 생성하기
    Universal Pipeline asset을 열어서 inspector 창의 General 섹션안에 넣어준다.
    - 상단 메뉴바에서 edit -> project settings를 선택해서 project setting view를 열어 graphic 섹션의 Scriptable Render Pipeline Settings에 앞에서 생성한 render pipeline asset을 넣어준다.
      ![image](https://user-images.githubusercontent.com/69496570/138540138-bf5658dc-5568-408b-800c-822ac09727bf.png)
      ![image](https://user-images.githubusercontent.com/69496570/138540164-3b111b87-b30f-4bd6-b2ef-50861b693052.png)
- 프로젝트 리소스 다운받기
  - 프로젝트 리소스를 다운받은 후 import해주기
  - ![image](https://user-images.githubusercontent.com/69496570/138540200-8918d042-bf05-4fd2-9be3-5d33d0a21f21.png)
    ![image](https://user-images.githubusercontent.com/69496570/138540235-df932253-5efb-4552-8b38-453cc7929847.png)
  - 원활한 프로젝트 관리를 위해서 새로운 폴더를 만들어서 asset들을 정리해준다.
    ![image](https://user-images.githubusercontent.com/69496570/138540302-2312d17f-c0ed-4232-809d-0847b06461c1.png)
  - 프로젝트 세팅과정이 끝나면 파란색의 GameView화면을 볼 수 있다.
    ![image](https://user-images.githubusercontent.com/69496570/138540366-8059d6f0-1451-4956-949d-319ccf5410d2.png)

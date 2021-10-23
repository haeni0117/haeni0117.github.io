---
title: "Make the 어몽어스(1) - 메인메뉴 만들기"
categories:
  - UNITY
tags:
  - gamedevelopment
last_modified_at: 2021-10-22T08:06:00-05:00
---

# 어몽어스(AmongUs)란?

![image](https://user-images.githubusercontent.com/69496570/138540527-0553ab71-a8d4-4813-a8c9-df9a7a054b40.png)
《어몽 어스》는 미국의 게임 스튜디오 이너슬로스에서 2018년 6월 15일에 출시 및 발표한 온라인 다인용 소셜 디덕션 게임이다. 모바일 버전은 무료이고, PC 버전은 유료이다.이 게임은 우주와 하늘을 소재로 한 장소, 여기서 플레이어는 두 역할 중 하나를 맡게 된다

### 베르의 게임 개발 유튜브 -> Make the 시리즈

일반적으로 한 강의 당 하나의 기능을 구현하는 것을 보여줬는데, 이 시리즈는 하나의 게임을 완전하게 만드는 것을 목표로 한다.

# 구현기능 -> 메인메뉴

## 프로젝트 열기

- 어몽어스는 2D패키지로 프로젝트를 열어준다.
  ![image](https://user-images.githubusercontent.com/69496570/138539694-863e4d0e-3435-41ad-8c4f-b79f600cb82f.png)
- 게임을 만드는 데에 필요한 패키지를 다운로드한다.
  - window -> package manager -> Universal RP package 설치
    ![image](https://user-images.githubusercontent.com/69496570/138539876-88a1f1d4-1561-40f5-b757-7743e06cda25.png)
  - create -> rendering -> universal renderpipeline -> pipeline asset 선택
  - ![image](https://user-images.githubusercontent.com/69496570/138540019-ba43b6ea-ed4a-4495-9406-28ad56f78cee.png)

## 다운받은 패키지를 활용하여 에셋 생성하기

- Universal Pipeline asset을 열어서 inspector 창의 General 섹션안에 넣어준다.
- 상단 메뉴바에서 edit -> project settings를 선택해서 project setting view를 열어 graphic 섹션의 Scriptable Render Pipeline Settings에 앞에서 생성한 render pipeline asset을 넣어준다.
  ![image](https://user-images.githubusercontent.com/69496570/138540138-bf5658dc-5568-408b-800c-822ac09727bf.png)
  ![image](https://user-images.githubusercontent.com/69496570/138540164-3b111b87-b30f-4bd6-b2ef-50861b693052.png)

## 프로젝트 리소스 다운받기

- 프로젝트 리소스를 다운받은 후 import해주기
- ![image](https://user-images.githubusercontent.com/69496570/138540200-8918d042-bf05-4fd2-9be3-5d33d0a21f21.png)
  ![image](https://user-images.githubusercontent.com/69496570/138540235-df932253-5efb-4552-8b38-453cc7929847.png)
- 원활한 프로젝트 관리를 위해서 새로운 폴더를 만들어서 asset들을 정리해준다.
  ![image](https://user-images.githubusercontent.com/69496570/138540302-2312d17f-c0ed-4232-809d-0847b06461c1.png)
- 프로젝트 세팅과정이 끝나면 파란색의 GameView화면을 볼 수 있다.
  ![image](https://user-images.githubusercontent.com/69496570/138540366-8059d6f0-1451-4956-949d-319ccf5410d2.png)

## 배경만들기

- 지금 game view가 파란색인데, 이걸 검정배경(우주)로 바꿔야한다.
- hierarchy view에서 main camera선택 -> inpector창 -> camera 프로퍼티 중 environment의 background색 = black으로 지정해준다.
  ![image](https://user-images.githubusercontent.com/69496570/138540505-74d0145e-6622-4e66-a284-796f838e136c.png)

## 메인메뉴의 기본 UI 배치하기

- hierarchy 뷰에서 UI -> Canvas를 생성한다.
- 빈 게임오브젝트(mainMenu)를 canvas의 자식으로 생성한다. 그 후 anchor를 stretch로 변경한 다음 left,top,right,bottom=0으로 설정
- 메인메뉴 아래에 image를 하나 생성한다. 그리고 그 이미지의 소스 이미지 프로퍼티에 sprite title image를 넣어준다. 그리고 이미지 컴포넌트의 SetNativeSize를 눌러서 적당한 크기로 맞춰준 다음 위치를 조정한다.
- 버튼UI를 만들어준다. 버튼 아래에 있는 text오브젝트는 삭제한 다음, 버튼이미지에 로컬버튼이미지를 찾아서 넣어준다. 그리고 크기와 위치를 적당히 맞춰준다.
- 나머지 온라인, 튜토리얼, 연습모드도 같은 방식으로 만들어준다.
- 아래쪽에 원형버튼을 추가하기 : 버튼UI생성 후 텍스트 오브젝트를 삭제한다. 그리고 원형버튼 이미지를 넣고, 5개를 복사해서 배치한다. 그리고 아래와 같이 버튼들을 세팅해준다.
  ![image](https://user-images.githubusercontent.com/69496570/138540807-4a357221-b14c-4cd9-b96c-1ae03dcb7b90.png)
- 모든 버튼 생성이 끝난 후 모든 버튼을 선택해서 highlighted color를 연두색으로 바꾼다. 그러면 진짜 어몽어스 게임처럼 버튼을 누르려고 할 떄 색이 연두색으로 변한다!
  ![image](https://user-images.githubusercontent.com/69496570/138540866-b23e0af5-dd9c-445e-8b3c-7f60df4756a9.png)

## UI 해상도 작업

현재 상태는 gameview에서 화면 해상도를 변경하면 ui가 밖으로 삐져나가는 문제가 있다. 해상도가 변경될 때마다 UI가 제대로 출력되지 않는 문제를 해결해야 한다.

- hierarchy view -> Canvas오브젝트 선택 -> canvas scaler 컴포넌트 -> UI scale mode를 Scale With Screen Size로 변경한다.
- 그 후 reference resolution을 현재 해상도로 맞춰준다. match = 1로 설정한다.
  - Match값 ?
    - 화면의 크기에 따라 UI를 조정할 때 화면의 너비와 높이 중에서 어디를 기준으로 잡을 것인가를 설정해야하는데, amongUs는 가로형 게임이기 때문에 해상도가 높이를 기준으로 너비가 flexible -> 따라서 match = 1

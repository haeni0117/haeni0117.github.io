---
title: "플레이어 캐릭터 구현하기"
categories:
  - Unity
tags:
  - userData
last_modified_at: 2021-10-29T08:06:00-05:00
---
캐릭터를 구현하는 여러가지 방법에 대해서 알아본 후 액션 RPG에 맞는 방법 선택
1. rigidbody를 사용하는 이유
2. rigidbodycharacter 설정하기
3. rigidbodycharacter.cs 구현하기

RigidBody : 게임오브젝트를 물리엔진에서 제어하도록 하는 컴포넌트
![image](https://user-images.githubusercontent.com/69496570/139321324-fa910998-31e9-4bac-9f84-203fddcc5395.png)
- 이동에 관련된 구현 : addforce, addtorque -> 오브젝트에 가해진 힘에 의해 자동으로 계산된다.
- collide component 추가 -> 
- 일반적으로 게임에서는 과장된 움직임을 구현하기 때문에 물리엔진을 사용하는 경우는 잘 없다고 함. 그럼에도 물리엔진을 통해 구현을 경험하고 템플릿을 만들어보는 것은 할 만한 가치가 있는 개발공부
  - 현실세계의 액션을 응용..? 수정..? 어쨌든 조작을 가한 현실액션이라는 점은 애니메이션과 유사한 것 같다.
  - ex ) 앵그리버드 : 실제로 저 사이즈의 물체를 저만큼의 거리만큼 당겼을 때 아무리 탄성도 높은 새총이라고 할 지라도 불가능한 물리액션 + 새가 나무 부수는 게 애초에 말이 안되니까
  - ![image](https://user-images.githubusercontent.com/69496570/139322115-1940cc9a-224a-4702-ab9e-93fa36978c28.png)

## rigidbody를 이용한 charater gameobject구성
1. capsule mesh ; 캐릭터 추가 목적
  - ![image](https://user-images.githubusercontent.com/69496570/139322976-8df2d97f-514e-44be-9231-6d21d0c7a0b0.png)
  - primitive objects 중 하나이다. 
  - Unity에서는 모델링 소프트웨어에 의해 만들어질 수 있는 모든 형태의 3D 모델을 다룰 수 있습니다. 그러나 Unity에서 직접 만들 수 있는 프리미티브 오브젝트 유형이 있으며, 그것들은 Cube, Sphere, Capsule, Cylinder, Plane 그리고 Quad입니다. 이러한 오브젝트는 그대로도 유용하지만(예를 들면 Plane은 평평한 지면으로 자주 사용됩니다), 추가 테스트 목적으로 오브젝트 틀이나 프로토 타입으로도 활용할 수 있습니다. 모든 프리미티브 GameObject > 3D Object 메뉴를 사용하여 각 항목을 선택하여 씬에 추가할 수 있습니다.(출처 : [유니티 공식문서 : 프리미티브 오브젝트](https://docs.unity3d.com/kr/530/Manual/PrimitiveObjects.html))
  - 종류 : cube, sphere, capsule, cylinder, plane, quad
    - quad라는 건 처음 들어봐서 모르겠고, 생긴 형태는 plane이나 quad나 종이처럼 생긴 건 비슷한데 뭐가 다르다는 건지 모르겠다.
    - quad란? a square or rectangular outside area with buildings on all four sides, often part of the land of a college or university
    - ![image](https://user-images.githubusercontent.com/69496570/139323549-85b7d4c3-8f4b-4f36-8670-d67b8bdf7b75.png)
      - ~~사각형이라는 건지 직사각형이라는 건지 ㅋㅋ.... 뭐 대충 사각형인 것 같은데 개발 계속하다보면 알게되겠지 아니면 다른 분들께 물어봐야지~~
    - quad와 plane 차이점 : Plane 과 Quad 는 같은 형태를 띄고 있지만
<mark>Plane 은 여러개의 삼각형</mark>으로 이루어져 있는 반면에 <mark>Quad 는 단 두개의 삼각형</mark>으로 이루어져 있기 때문에 단순한 면을 표현하는 것에 있어서 경제적이다
드로우 모드를 Wireframe 으로 전환하면 그 차이를 확실히 볼 수 있다
  (출처 : [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wowsoft72&logNo=221049597965](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wowsoft72&logNo=221049597965))
  ![image](https://user-images.githubusercontent.com/69496570/139325053-e053596f-0791-4f9c-8529-5bd1840d4741.png)
3. rigidbody component ; 물리 엔진에 의해 제어
4. capsule collider ; 충돌 연산을 위하여 반드시 추가 필요
5. rigidbodycharacter.cs ; c#스크립트 -> 사용자 입력 및 이동처리

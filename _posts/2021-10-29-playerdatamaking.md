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

# UNITY editor에서 직접 구현하기
세팅 : terrain, 계단 -> layer:ground로 설정, static 지정 
- 비어있는 오브젝트에 capsule collider 컴포넌트 추가 
- 빈 게임오브젝트에 capsule 오브젝트를 자식으로 추가해준다. 부모의 이름 : rigidbodycharacter
- 자식오브젝트의 collider는 사용하지 않기 때문에 삭제하면 된다. -> remove component!
- RigidbodyCharacter의 센터값을 (x,y,z)=(0,1,0)으로 설정한다. 그러면 항상 하단이 원점이 된다.
  - 그 이유는? 캐릭터의 발끝이 항상 원점이 되도록 설정하기 위해서
  - capsule도 y포지션 1로 설정하여 위로 올려둔다.
- ![image](https://user-images.githubusercontent.com/69496570/139568445-c78dbecd-36cd-406f-b105-6aa352b73778.png)
- rigidbodycharacter에 rigidbody 컴포넌트를 추가한다.
  - `mass` : 질량계산 -> 중력에는 영향을 받지 않지만, rigidbody끼리 충돌했을 떄 반응을 어떻게 할 것인가를 결정한다.
    - 무게(weight) = 질량(mass) * 중력가속도(g)
  - `drag` : 공기저항값 -> Drag값이 적어지면 무거워보이고 커지면 가벼워보인다. 
    - 쇠구슬과 종이 생각해보면 될 듯. 공기저항값이 비교적 높은 종이는 살랑살랑 떨어진다(영향을 많이 받음) 반면에 무거운 쇠구슬은 공기저항값이 비교적 낮고 공기에 영향을 거의 받지 않은 채 낙하한다.
    - drag값은 8정도로 설정한다.
    - ![image](https://user-images.githubusercontent.com/69496570/139570419-60686595-9ac9-40e7-ab84-9d8d126ffdbb.png)
  - `angular drag` : 회전할 때 공기저항값
  - `use gravity` : 중력을 받을 것인지 아닌지
  - `is kinematic` : 물리엔진이 아닌 게임오브젝트의 로직에 따라 게임오브젝트를 이동시킨다. 
    - -> 게임에서는 물리엔진 말고 자체 로직을 사용하는 경우도 많기 때문에 is kinematic이 자주 사용될 거라고 예측가능
  - `interpolation` : 물리엔진의 애니메이션을 자연스럽게 보간한다.
    - 기본설정으로 Interpolation는 비활성화 되어 있습니다. 주로 리지드바디 Interpolation은 플레이어의 캐릭터에 사용됩니다. 물리 효과에 대한 계산과, 렌더링 계산은 서로 다른 주기로 동작합니다. 이러한 이유로 물리효과와 그래픽효과가 완전히 동기가 맞지는 않기 때문에, 해당 오브젝트가 어색해 보일 수 있습니다. 어색해 보이는 효과가 미미할 수 있지만 특히 카메라가 메인 캐릭터를 따라가는 경우와 같이, 플레이어 캐릭터에 뚜렷하게 나타나는 경우가 있습니다. (출처 : [UNITY - 스크립팅API Rigidbody.interpolation](https://docs.unity3d.com/kr/530/ScriptReference/Rigidbody-interpolation.html))
  - `collision detection` : 충돌처리를 연속적으로 할 것이냐 or 특정한 경우에만 할 것이냐 설정한다.
  - `freeze position` : 물리엔진에서 값을 조정하는 것이 아니라 픽스할건지  or 물리엔진이 처리하도록 둘 것인지 설정한다.
     - 이 프로젝트에서는 모두 물리엔진에 맡길 것이므로 unchecked 상태로 두면 된다.
  - `freeze rotation` : y값만 사용할 것이기 때문에 x,z값을 checked 상태로 설정한다 -> 물리엔진에서 x,z 로테이션값 임의로 변경 불가능해진다.

## rigidbody character에 스크립트 추가해주기
  ![image](https://user-images.githubusercontent.com/69496570/139570842-efca0ffa-6672-4627-9376-d2fceb653372.png)
- `FixedUpdate()` : 프레임을 기반으로 호출되는 Update 와 달리 Fixed Timestep에 설정된 값에 따라 일정한 간격으로 호출됩니다. 물리 효과가 적용된(Rigidbody) 오브젝트를 조정할 때 사용됩니다(Update는 불규칙한 호출임으로 물리엔진 충돌검사 등이 제대로 안될 수 있음). -> <mark>프레임과 상관없이 고정적으로 호출된다.</mark>
  - cf ) `LateUpdate()`, `Update()`
  - 출처 : [Update() , FixedUpdate() , LateUpdate() 의 차이점 by Developug](http://developug.blogspot.com/2014/09/update-fixedupdate-lateupdate.html)
![image](https://user-images.githubusercontent.com/69496570/139571271-e10c9f3d-566a-4bf3-a175-adfdbd5b61c3.png)
### `#region`과 `#endregion`
  - 목적성 
     - 1) 서로 관련된 method, properties, fields 등등 그룹을 지을 수 있습니다. 
     - 2) 긴 코드 블록들을 작은 블록으로 만들 수 있습니다. 개발자는 코드를 보고 싶을때 코드 왼쪽 편의 '+'를 선택하여 확대할 수 있고, 그곳에서의 작업이 끝났을 경우 '-'를 선택하여 닫아 두어 최대한 현재의 작업에만 집중할 수 있습니다. 
    - ![image](https://user-images.githubusercontent.com/69496570/139571428-6e8d5a40-75fb-4863-aeab-1e1184424788.png)
  - 출처: https://nsstbg.tistory.com/5 [All about it...]

### moveposition()
![image](https://user-images.githubusercontent.com/69496570/139571541-2696ec03-89e1-4623-8449-8c489cfaf0a0.png)
- Moves the kinematic Rigidbody towards position.
- Rigidbody.MovePosition moves a Rigidbody and complies with the interpolation settings. When Rigidbody interpolation is enabled, Rigidbody.MovePosition creates a smooth transition between frames. Unity moves a Rigidbody in each FixedUpdate call. The position occurs in world space. Teleporting a Rigidbody from one position to another uses Rigidbody.position instead of MovePosition.
  - teleport란? 순간이동

- 캐릭터가 capsule이라서 direction을 파악하기가 어려움 -> cube mesh 추가
### Vector3.Scale()
- public static Vector3 Scale(Vector3 a, Vector3 b) => 벡터의 곱
- Rigidbody.MovePosition moves a Rigidbody and complies with the interpolation settings. When Rigidbody interpolation is enabled, Rigidbody.MovePosition creates a smooth transition between frames. Unity moves a Rigidbody in each FixedUpdate call. The position occurs in world space. Teleporting a Rigidbody from one position to another uses Rigidbody.position instead of MovePosition.

```
using UnityEngine;

public class Example : MonoBehaviour
{
    Rigidbody m_Rigidbody;
    public float m_Speed = 5f;

    void Start()
    {
        //Fetch the Rigidbody from the GameObject with this script attached
        m_Rigidbody = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        //Store user input as a movement vector
        Vector3 m_Input = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));

        //Apply the movement vector to the current position, which is
        //multiplied by deltaTime and speed for a smooth MovePosition
        m_Rigidbody.MovePosition(transform.position + m_Input * Time.deltaTime * m_Speed);
    }
}
```


## jump 구현하기

- Rigidbody.MovePosition moves a Rigidbody and complies with the interpolation settings. When Rigidbody interpolation is enabled, Rigidbody.MovePosition creates a smooth transition between frames. Unity moves a Rigidbody in each FixedUpdate call. The position occurs in world space. Teleporting a Rigidbody from one position to another uses Rigidbody.position instead of MovePosition현
- Rigidbody.MovePosition moves a Rigidbody and complies with the interpolation settings. When Rigidbody interpolation is enabled, Rigidbody.MovePosition creates a smooth transition between frames. Unity moves a Rigidbody in each FixedUpdate call. The position occurs in world space. Teleporting a Rigidbody from one position to another uses Rigidbody.position instead of MovePosition.

## Dash 구현하기
- dash : 질주
![image](https://user-images.githubusercontent.com/69496570/139572504-205e6aa7-6ddb-4b21-8029-c18ab9bcba42.png)
- ~~선형대수학을 마스터못해서 도대체 뭔 식인지 모르겠다.. 선대공부를 다시해야하나 벡터 ....
- <mark>rigidbody의 저항값을 로그함수화시켜서 점차적으로 느려지는 값으로 표현될 수 있게 dashVelocity값을 계산한 것</mark>
- 예전에 타이포그래피할 때 미분가능한 구조로 그래프를 그렸던 것처럼 로그함수사용의 궁극적 목적은 정말 실제처럼 dash하게 보이기 위해서 사용하는 것
- ![image](https://user-images.githubusercontent.com/69496570/139572610-247985d1-fb95-4561-8579-ff9723250e35.png) 
- 딱 그냥 봐도 일반 직선그래프랑은 모션이 다를 것 같지 않나?

![image](https://user-images.githubusercontent.com/69496570/139572826-4bb525d0-ab81-4de1-a0dd-db75b1335342.png)
### `AddForce()`
- 출처 : [AddForce에 대한 모든 것(+relaive force) by 노는 게 제일 좋아](https://luv-n-interest.tistory.com/687)
- 형태
  - 1. `public void AddForce(Vector3 force, ForceMode mode = ForceMode.Force)`
  - 2. `public void AddForce(float x, float y, float z, ForceMode mode = ForceMode.Force) `
  - 사실 두 형태가 본질은 같다. 왜냐하면 1번은 force라는 변수가 하나의 벡터값인 것이고, 2번째 형태는 벡터값이 아닌 대신에 벡터의 구성요소들을 매개변수로 받고 있기 떄문이다.
  - 간단하게  `Vector3 force = float x,y,z` 라고 생각하면 되겠다. -> AddForce( 방향 x 힘 값, 힘의 종류 )
- 기능 : addforce -> force를 더해준다. 
  - rigidbody가 active상태일 때 힘을 전달해준다(addforce)
  - 이런 force calculation은 FixedUpdate()에서 일어난다.


### ForceMode
- 어떤 식으로 힘을 전달하는지
- ForceMode의 네 가지 타입 
- ![image](https://user-images.githubusercontent.com/69496570/139573104-41b6a1ab-2d8e-431b-a9d2-44d1ab8a582a.png)
- 질량(mass)을 무시하느냐? 연속적인 힘이냐? 에 따른 분류이다. 아래는 출처 블로그 작성자분이 설명하신 건데 너무 이해가 잘 되어서 들고왔다. ~~연속적인 힘이 뭔소리지~~
  - <span style="color:red">Force</span>는 연속 + 질량 무시 X : 현실적인 물리현상을 나타낼 때 많이 씀
  - <span style="color:green">Accel</span>은 연속 + 질량 무시 O : 질량에 관계 없이 가속된다. 즉, 오브젝트의 질량에 관계없이 가속을 주고싶다면 이용한다.
  - <span style="color:blue">Impulse</span>는 불연속 + 질량 무시 X : 짧은 순간의 힘, 충돌이나 폭발과 같은 것에 많이 쓰인다.
  -  <span style="color:gray">Velocity Change</span> 불연속 + 질량 무시 O : 마찬가지로 질량에 관계 없이 속도를 바꾼다. 질량이 다른 함대 같은 경우 같은 힘을 줘서는 같은 속도로 움직일 수 없는데 이 모드를 사용하면 가능하다.
  - ~~불연속에 질량까지 무시하면 비현실적 모션인건가?~~
  

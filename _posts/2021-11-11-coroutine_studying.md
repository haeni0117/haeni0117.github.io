---
title: "[unity] 코루틴(Coroutine)함수"
categories:
  - UNTIY
tags:
  - coroutine function
last_modified_at: 2021-11-11T08:06:00-05:00
---
## Update 함수
- `Update ` : 게임 오브젝트가 활성화된 상태에서 매 프레임 호출되어 수행된다. 그래서 유니티 엔진으로 게임을 만들 때는 대부분의 게임 동작을 Update 함수에서 작동하도록 구현한다.
- 한계 : Update 함수는 <mark>멈추지 않고 계속해서 동작하는 함수</mark>이기 때문에 여기서 <mark>일시적으로 돌아가는 서브 동작</mark>을 구현하는 것과 <mark>어떤 다른 동작이 처리되는 것을 기다리는 기능</mark>을 구현하기는 매우 까다롭다.
  - 내가 구현하려는 합성기능은 사용자가 합성기능을 사용하고자 할 때만 필요하기 때문에 update()보다 coroutine이 훨씬 적합하다. 
  - bool자료형을 사용하여 상시대기형식으로 합성창을 구현한다는 것 자체가 비효율적인 프로그래밍
  - 레퍼런스로 본 블로그에서도 이런 상황에서 update()를 사용하는 것에 대해 비효율적이라고 지적하고 있다. 
  - ![image](https://user-images.githubusercontent.com/69496570/141271341-0823d71a-2159-40bd-ac31-00e424831efa.png)
- 그렇다면, 코루틴함수는 조건부 update()라고 볼 수 있지 않을까? 
- 음 조건부 Update()라고 볼 수 있기는 한데, 포인트는 대기인 것 같다. update()를 사용할 때에는 일일이 시간을 카운팅하면서 호출->종료->호출->종료 이런식으로 분기를 나눠야했다면 코루틴을 사용하면 그냥 그 코루틴 하나가 얼마동안 작동하고 정해놓은 시간이 지나면(일정 시간동안 진행되다가) 다시 유니티에게 제어를 넘겨준다(코루틴은 종료).
- 총 게임같은 데에서는 유용하게 사용할 수 있을 것 같은데, 지금 우리 게임에서 유용하게 쓰일지는 잘 모르겠다.

## FixedUpdate 함수
- MonoBehaviour가 활성화 되어있는 경우에, 매 고정된 프레임율의 프레임(fixed framerate frame)마다 호출된다.
- Rigidbody를 다루는 경우에, Update대신 FixedUpdate를 사용해야 합니다. 
  - 예를 들어 리지드바디에 힘을 가하는 경우에, FixedUpdate안에서 매 고정된 프레임마다 힘을 적용해야 합니다. 이 경우 Upate에서 매 프레임마다 힘을 적용하지 않도록 합니다.
- 코루틴, Update(), FixedUpdate()비교
   - Update(매 프레임 호출),
   - FixedUpdate(1초 당 정해진 횟수 호출 (50회 40회 등) 

## 코루틴(Coroutine) 함수
- 코루틴이라는 것은 어떠한 작업을 처리할 때 필요에 따라 <mark>시간 간격을 두고 작업을 처리</mark>할 수 있도록 도와주는 함수 형식이다.
- Update 함수와 따로 일시적으로 돌아가는 서브 동작을 구현하거나, 어떤 다른 작업이 처리되는 것을 기다리는 기능을 구현하는데 쓰이는 것이 바로 코루틴(coroutine)
- 예제코드로 코루틴의 동작에 대해 구체적으로 살펴보자.
  - CF ) 아래의 코드는 update()함수를 통해 attacker 클래스를 구현한 것이다. 매 프레임마다 호출되는 함수답게 조건분기의 연속이다. 
  - 코루틴으로 구현한 공격함수와 비교한다면, update()로 구현한다는 것이 얼마나 비효율적인지를 느낄 수 있다.
  
  ```
  public class Attacker : MonoBehaviour
  {
    public bool isDelay;
    public float delayTime = 2f;
    float timer = 0f;
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (!isDelay)
            {
                isDelay = true;
                Debug.Log("Attack");
            }
            else
            {
                Debug.Log("Delay");
            }
        }
        // 업데이트로 구현한 공격 딜레이
        if (isDelay)
        {
            timer += Time.deltaTime;
            if (timer >= delayTime)
            {
                timer = 0f;
                isDelay = false;
            }
        }
    }
  }

  ```
  
  - 코루틴(Coroutine)으로 구현한 공격함수 코드


  ```
  // 코루틴으로 구현한 공격 딜레이
  IEnumerator CountAttackDelay()
  {
    yield return new WaitForSeconds(delayTime);
    isDelay = false;
  }
  ```
  
    - 코루틴은 다른 함수와 다르게 특수한 문법이 존재한다. 지금 당장 위 코드만 봐도 `IEnumerator`,`yield return` 등등 좀 생소한 키워드가 있는 것을 확인할 수 있다.

## 코루틴(Coroutine)함수 만드는 방법
1. 반환형을 IEnumerator로 설정한다.
2. yield return이란 코드를 작성한다.
  - `yield return` : 코루틴에서 동작하는 제어권을 유니티에 다시 돌려준다는 뜻
  - yield return 시점에 도착하면 코루틴은 반환 타입으로 정의한 만큼 코드 동작을 중지하고 제어권을 유니티에 돌려준다.
  - 반환 타입의 조건이 충족되면 이 다음 줄부터 다시 코루틴이 동작한다.
  - 코루틴이 제어권을 얼마나 양보할 지 정하는 반환 타입에는 여러 가지가 있다.


3. 코루틴 함수는 실행할 때 일반 함수처럼 호출하는 것이 아니라, StartCoroutine 함수를 이용해서 호출해야 한다.
4. 반환 타입 종류

```
// 한 프레임 기다림
yield return null;

// 게임 시간으로 1초 기다림(time scale에 영향받음)
yield return new WaitForSeconds(1f);

// 실제 시간으로 1초 기다림(time scale에 영향받지 않음)
yield return new WaitForSecondsRealtime(1f);

// 다음 FixedUpdate 끝날 때까지 기다림
yield return new WaitForFixedUpdate();

// 다음 프레임의 Update와 모든 렌더링이 끝날 때까지 기다림
yield return new WaitForEndOfFrame();
```


## 출처
- [베르의 프로그래밍 노트 - Programming 코루틴(Coroutine) 다루기](https://wergia.tistory.com/219)
- [Prosto - 코루틴이란? 사용법은?](https://prosto.tistory.com/68)



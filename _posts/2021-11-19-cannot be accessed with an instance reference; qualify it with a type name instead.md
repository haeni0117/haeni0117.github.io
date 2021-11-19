---
title: "[unity] CS0176 - cannot be accessed with an instance reference; qualify it with a type name instead"
categories:
  - unity
tags:
  - error
  - static
last_modified_at: 2021-11-19T09:06:00-05:00
---
# CS0176
cannot be accessed with an instance reference; qualify it with a type name instead
- static 변수에 관련된 에러인 것 같다.
- 내가 원하는 것은 다른 스크립트에서 쓰고 있는 cnt라는 정적변수를 initiate 하지 않고, 그대로 들고오는 방법에 대해서

# 개념정리
## static
- static 키워드는 변수 혹은 함수 혹은 클래스가 객체(인스턴스) 단위가 아니라 클래스 단위로 생성, 사용되게 하는 키워드이다
- msdn의 설명에 따르면 <u>static 한정자는 특정 개체가 아니라 해당 형식 자체에 속하는 정적 멤버를 선언하는 데 사용됩니다</u>라고 한다.

## static 함수
- static변수와 동일한 개념이다.
- 차이점 : 객체단위가 아니라 함수
- 단순 숫자 계산해주는 함수들 모두 static이다.
  - ex) 클래스를 배우기 전에 지금까지 만들었던 함수들, main 함수 

## main함수
- 프로그램의 시작점
- <u>Main 함수도 클래스 안에 속해야 한다</u>
- <span style="color:red">반드시 static</span>이어야 하며, 외부에서 호출되므로 public 액세스 지정을 가져야 한다
- 리턴값과 인수는 다음 4가지 중 하나를 선택할 수 있다.
```
public static void Main();
public static int Main();
public static void Main(string[] args);
public static int Main (string[] args);
//java에서는 3,4번 쓰지 않나? 
//이런 것도 자바랑 상당히 유사한 듯
```
- 리턴(return)값 : 프로그램 자체의 실행 결과를 리턴
- 아예 없거나(void) 있다면 int 형이어야 한다
  - 주로 void를 사용하며, int를 사용하면 끝에 return(); 가 있어야 함

## args
- args : 프로그램으로 전달되는 인수
- args는 <u>열어야할 파일의 경로나 옵션 스위치</u> 등이 전달된다

## static 변수 사용 예시
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
  class Character
  {
      public int num = 0;
      public Character()
      {
        num++;
       }
    }
  class Program
  {
    static void Main(string[] args)
    {
      Character mario = new Character();
      Character luigi = new Character();
      Console.WriteLine(mario.num);
    }
  }
}
```
- 네임스페이스(namespace)
  - namespace간의 이름이 달라야하는데 그 내용물의 이름은 다르지 않아도 OK
  - ![image](https://user-images.githubusercontent.com/69496570/142608856-16d0734d-8e48-4533-b56a-e385e0c7ec87.png)
  - 클래스를 불러올때 어떤 namespace 에서 불러올 건지 정하고 클래스를 부른다.
  - namespace를 일일히 이름을 적어주기가 힘드니 using 이라는 키워드가 존재한다.
- Q. 만약 static 변수가 아니라면?
  - 맴버 변수로 객체마다 num이 할당되고 `num++`도 객체마다 이루어지기때문에 `mario.num`은 당연히 1이 나온다 ( 마리오 생성자는 1번만 불렸으므로 )
  - 따라서 기존방식으로는 캐릭터가 총 몇개 생성되었는지 알수없다.
  - 이러한 문제를 해결하기위한 키워드가 <mark>static</mark>이다

## 코드수정
```
[System.Serializable]
public class bathroom_inspect : MonoBehaviour
{
    public static int cnt;
    public List<inspection> Tools;
    public GameObject toiletItems;
    private bool showerbooth, showerboothshelves,shampoo,rinse,
                 bodywash,sparekey,iotbidet,
                 footmat,mirrorandshelves,medicine,toothpaste,
                 tissue,shaver,dryer,towel,coat,washstand,towelhanger= false;


    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
      cnt = ch1.cnt;
      Debug.Log("hihi");
      Debug.Log("! : "+cnt);
      if(cnt==172){
        toiletItems.SetActive(true);
      }
    }
}
```
- 수정과정 
  - update()를 통해 cnt를 지속적으로 업데이트한다. → `cnt = ch1.cnt`

## 출처
- [SeeRoE 프로그래밍 기록 - [C# 때려잡기] C# 강의 23. static 변수 및 함수](https://see-ro-e.tistory.com/120)
- [BlackP 프로그래밍 - C# namespace, using](https://m.blog.naver.com/bug_ping/221425846342)
- [야구를 좋아하는 프로그래머 - C# main 함수](https://hidingzz.tistory.com/419)

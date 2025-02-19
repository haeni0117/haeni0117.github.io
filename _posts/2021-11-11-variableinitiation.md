---
title: "[unity/도전학기] 합성창에서 변수(com2) 초기화 이슈"
categories:
  - 도전학기
tags:
  - client
last_modified_at: 2021-11-11T08:06:00-05:00
---
합성하는 과정에서 이슈가 발생했다.
- [도구]/[분해]/[합성] 인벤토리 중 합성을 클릭해서 합성창을 활성화시킨다.
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 15" src="https://user-images.githubusercontent.com/69496570/141266571-e88714df-bb3e-4d59-ab1b-47ed3311fb03.png">
- 합성창에 존재하는 아이템 중 하나를 선택하면 `GameObject`인 `secondselection`을 활성화시킨다 : 합성 과정 중 두 번째 아이템
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 21" src="https://user-images.githubusercontent.com/69496570/141266592-9b524917-3248-47b2-a5ad-fb4ae3aa1f13.png">
- 두 번째 합성창에서 아이템을 또 선택한다(두 번째 선택) => 합성할 두 개의 아이템 선택 완료
<img width="1433" alt="스크린샷 2021-11-11 오후 5 43 28" src="https://user-images.githubusercontent.com/69496570/141266597-2f06eff9-4651-4258-856b-7b77e5340c01.png">
- [아니요] 클릭 -> 합성 종료
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 39" src="https://user-images.githubusercontent.com/69496570/141266602-b1e44138-d3ec-47a7-8c84-27755208d2e9.png">
- 그 후 다시 합성하고자 합성을 하면, 아직 두 번째 아이템을 선택을 안했음에도 직전의 합성과정에서 선택한 두 번째 아이템이 그대로 존재하는 문제가 생긴다. 아래와 같은 상황에서는 첫 번째 [모형자동차]는 새로운 합성과정에서 선택한 것이지만, 두 번째 [모형자동차]는 이 전에 있던 아이템 정보가 남아있어서 선택도 안했는데 남아있는 것이다. 
- 첫 번째 아이템, 두 번째 아이템에 대한 변수를 각각 `com1`와`com2`라고 정의하고 public으로 정의해뒀다. 그래서 나는 이걸 함수 안에서 정의해야하는데 public으로 정리해버려서 생기는 문제인 줄 알았다.
- `com2`라는 변수가 처음처럼 텅 비었으면 좋겠는데 어떻게 해결해야할까?
- 변수가 문제가 아니라 `_SlotClick`함수가 종료가 안되고 계속 실행중이라는 게 문제 아닌가? 
<img width="1439" alt="스크린샷 2021-11-11 오후 5 43 48" src="https://user-images.githubusercontent.com/69496570/141266608-1128a8ed-09d8-49ff-ac61-dd3a05edf3e6.png">
<img width="1217" alt="스크린샷 2021-11-11 오후 5 44 19" src="https://user-images.githubusercontent.com/69496570/141266610-1499e9e2-d98d-40c5-88f3-e55e8bf06a91.png">

## 관련코드
```
public void secondselectionMethod(){
        secondselection.SetActive(true);
        CompositionSecondselectionList= MyItemList.FindAll(x=>x.Type=="Composition");//해당 인벤토리(분해/합성/도구)에 해당하는 아이템 로드 
        for(int i=0;i<Slot_second.Length; i++){//slot(아이템이 직접 보여질 영역)개수(slot.length)만큼 for문을 돌린다. 
            bool isExist = i<CompositionSecondselectionList.Count;//slot 존재여부 판단
            Slot_second[i].SetActive(isExist);
            if(isExist){
                ItemImage2[i].sprite = ItemSprite[AllItemList.FindIndex(x=>x.Name==CompositionSecondselectionList[i].Name)];
            }
        }

    }
    public void _SlotClick(int slotNum){
        string slot_name=CompositionSecondselectionList[slotNum].Name;
        string inventorypanel=CompositionSecondselectionList[slotNum].Type;
        CompositionImage2.sprite=ItemSprite[AllItemList.FindIndex(x=>x.Name==CompositionSecondselectionList[slotNum].Name)];
        string com2 = slot_name;
        PopupText[2].text=com1+"과 "+com2+"을(를) 합성하시겠습니까?";
    }
````

## 문제해결(null값 사용)
- 처음에는 코루틴함수를 써야하나 고민했었다. 근데 그건 내가 코루틴함수에 대해 제대로 이해하지 못해서 그랬다. 코루틴의 키워드는 [지연] 그리고 [대기]이다. -> 코루틴함수 공부한 거 정리했음
- null값이라는 걸 사용할 생각을 왜 못했지?? 값을 초기화하려면 값이 없는 상태여야하는데 그게 바로 null
- 합성에 사용되는 두 아이템에 대한 변수가 `com1`,`com2`였는데 이 변수들을 메소드 영역이 아니라 클래스에서 선언하고 첫번째 아이템을 선택하는 함수를 실행할 때 `com2`는 무조건 null값을 가지도록 수정했더니 제대로 구현되었다.
- <img width="744" alt="스크린샷 2021-11-11 오후 8 29 41" src="https://user-images.githubusercontent.com/69496570/141291192-688e59c0-a700-4564-a0ed-7457c27e9f07.png">
- <img width="741" alt="스크린샷 2021-11-11 오후 8 29 49" src="https://user-images.githubusercontent.com/69496570/141291201-93b08942-308d-424c-8fb9-af60d47c6cd3.png">
- 코드
  ```
  public void buttonclick(int button_num){
        switch(AllButtonList[button_num].Type){
            case "yes":
            switch(AllButtonList[button_num].PopupType){
                case "tool":
                Debug.Log("YES / Tool");
                break;
                case "decomposition":
                Debug.Log("YES / Decomposition");
                break;
                case "composition":
                Debug.Log("YES / Composition");
                break;
            }
            break;
            case "no":
            switch(AllButtonList[button_num].PopupType){
                case "tool":
                Debug.Log("NO / Tool");
                popUpPanel[0].SetActive(false);
                break;
                case "decomposition":
                Debug.Log("NO / Decomposition");
                popUpPanel[1].SetActive(false);
                break;
                case "composition":
                isAvailable=true;
                Debug.Log("NO / Composition");
                popUpPanel[2].SetActive(false);
                secondselection.SetActive(false);
                break;
            }
            break;

        }

    }
  
  ```
  
  ```
   public void initiate_method(){
        CompositionImage2.sprite=null;
        com2=null;
    }
  ```
  
<img width="907" alt="스크린샷 2021-11-11 오후 8 34 54" src="https://user-images.githubusercontent.com/69496570/141291433-ab643112-a6a3-420c-a853-8dabdfda1106.png">
<img width="557" alt="스크린샷 2021-11-11 오후 8 35 03" src="https://user-images.githubusercontent.com/69496570/141291440-f2c4ceb3-8d9d-4e3a-ac36-842a29cd4280.png">

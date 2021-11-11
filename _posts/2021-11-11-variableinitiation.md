---
title: "[unity] 변수 초기화"
categories:
  - 도전학기
tags:
  - client
last_modified_at: 2021-11-11T08:06:00-05:00
---
합성하는 과정에서 이슈가 발생했다.
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 15" src="https://user-images.githubusercontent.com/69496570/141266571-e88714df-bb3e-4d59-ab1b-47ed3311fb03.png">
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 21" src="https://user-images.githubusercontent.com/69496570/141266592-9b524917-3248-47b2-a5ad-fb4ae3aa1f13.png">
<img width="1433" alt="스크린샷 2021-11-11 오후 5 43 28" src="https://user-images.githubusercontent.com/69496570/141266597-2f06eff9-4651-4258-856b-7b77e5340c01.png">
<img width="1440" alt="스크린샷 2021-11-11 오후 5 43 39" src="https://user-images.githubusercontent.com/69496570/141266602-b1e44138-d3ec-47a7-8c84-27755208d2e9.png">
<img width="1439" alt="스크린샷 2021-11-11 오후 5 43 48" src="https://user-images.githubusercontent.com/69496570/141266608-1128a8ed-09d8-49ff-ac61-dd3a05edf3e6.png">
<img width="1217" alt="스크린샷 2021-11-11 오후 5 44 19" src="https://user-images.githubusercontent.com/69496570/141266610-1499e9e2-d98d-40c5-88f3-e55e8bf06a91.png">
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

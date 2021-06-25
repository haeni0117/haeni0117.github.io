### 힙(Heap)

### 1. 힙 (Heap) 이란?
- 힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
  - 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

<img src="https://www.fun-coding.org/00_Images/completebinarytree.png" width=300>

- 힙을 사용하는 이유
  -  <span style="color:yellow">ex)최대값 또는 최소값을 구해야 하는 경우가 많다 -> 최대값/최소값 탐색 알고리즘 및 자료구조의 필요성 / 하지만 그 떄마다 정렬을 사용해서 값을 구한다면 시간이 많이 걸린다 -> 이를 줄일 수 있는 자료구조 중 하나가 힙(Heap)이다.</span>
  - 트리(tree)를 기반으로 한 변형된 형태의 정책을 사용하고 있다.
  - 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림 -> 효율적인 방법 고안
  - 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, $ O(log n) $ 이 걸림
  - 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

### 2. 힙 (Heap) 구조
- 힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap) 와, 최소값을 구하기 위한 구조 (최소 힙, Min Heap) 로 분류할 수 있음
- 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조임
  1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
     - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
  2. 완전 이진 트리 형태를 가짐
   - 완전 이진 트리란? 왼쪽부터 데이터를 채운다. + 자식이 최대 2개(노드가 3개 이상은 불가능하다.)

### 힙과 이진 탐색 트리의 공통점과 차이점
- 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
- 차이점:
  - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
  - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
  - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
    - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
- 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨  
<img src="https://www.fun-coding.org/00_Images/completebinarytree_bst.png" width="800" />

### 3. 힙 (Heap) 동작
- 데이터를 힙 구조에 삽입, 삭제하는 과정을 그림을 통해 선명하게 이해하기
- 포인트는 SWAP !!!!

### 힙에 데이터 삽입하기 - 기본 동작
- 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입
<img src="https://www.fun-coding.org/00_Images/heap_ordinary.png">

### 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap 의 예)
- 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
- 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)
<img src="https://www.fun-coding.org/00_Images/heap_insert.png">

### 힙의 데이터 삭제하기 (Max Heap 의 예)
- 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
  - 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
- 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드) 를 root 노드로 이동
- root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

<img src="https://www.fun-coding.org/00_Images/heap_remove.png">


### 4. 힙 구현
### 힙과 배열
- 일반적으로 힙 구현시 배열 <span style="color:yellow">배열 </span>자료구조를 활용함
  - 배열 구조를 활용할 수 있는 이유는 <span style="color:yellow">완전 이진 트리</span>의 구조를 가지고 있기 때문이다.
- 인덱스(index)번호를 알면 부모노드 자식노드를 계산할 수 있다.
  - HOW? 자식노드의 몫을 구하면 부모노드 인덱스 넘버를 구할 수 있다.
  - HOW? 부모노드를 2배하면 왼쪽 자식노드, 그 인덱스넘버에 +1을 하면 오른쪽 자식노드
- 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀더 수월함
  - 부모 노드 인덱스 번호 (parent node's index) = 자식 노드 인덱스 번호 (child node's index) // 2
  - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
  - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1
<img src="https://www.fun-coding.org/00_Images/heap_array.png" width=400>

### 힙에 데이터 삽입 구현 (Max Heap 예
1. 힙 클래스 구현하기
```
  class Heap:
    def _init_(self,data): #최초 실행시의 셀프와 데이터 -> self가 의미하는 바?
      self.heap_array() = list() #내부의 자료구조 -> 배열(list)  
      # 복잡도를 줄이기 위해 인덱스넘버를 1부터 사용
      self.heap_array.append(None)
      self.heap_array.append(data)
```
##### sample
```
heap = Heap(1)
heap.heap_array
[None, 1]
```

```
  class Heap:
    def _init_(self,data): #최초 실행시의 셀프와 데이터 -> self가 의미하는 바?
      self.heap_array() = list() #내부의 자료구조 -> 배열(list)  
      # 복잡도를 줄이기 위해 인덱스넘버를 1부터 사용
      self.heap_array.append(None) #append 그냥 추가되는 게 아니라 제일 뒤에 추가 -> 이진 완전 트리의 메커니즘
      self.heap_array.append(data)

    def move_up(self,inserted_idx):
      if inserted_idx==1: #루트노드일 때
        return False #더 이상 할 게 없다.
      parent_idx = inserted_idx//2 #트리 공식으로 inserted_idx의 부모노드 구하기
      if self.heap_array[inserted_idx]>self.heap_array[parent_idx]
      # 부모노드와 자식노드를 비교함으로써 SWAP이 발생하는지 여부를 조:
        # 정말 부모노드보다 자식노드의 값이 더 클 때-> if문 만족
        return True
      else:
        return false
        # 그렇지 않으면(else -> 부모노드가 자식노드보다 클 때)False값 리턴한다.
        # Q. 이 작업은 언제까지 해야하나? -> while로 반복작업하게 설정해놓았다.
        # A. 모든 부모노드가 자식노드보다 값이 커질 때 or inserted_idx가 루트노드일때(index_num == 1)
        # move_up메소드가 반복작업까지 하는 건 아님 -> only 판별만 하고 반복은 while이 담당한다.

    # 반복문 => until 모든 부모노드가 자식노드보다 값이 커질 때 or inserted_idx가 루트노드일때(index_num == 1)
    while(self.move_up(inserted_idx)):
      parent_idx = inserted_idx//2
      self.heap_array[inserted_idx],self.heap_array[parent_idx]= self.heap_array[parent_idx],self.heap_array[inserted_idx]
      #SWAP
      inserted_idx=parent_idx #재귀(recursion)을 위해서
    return True
```

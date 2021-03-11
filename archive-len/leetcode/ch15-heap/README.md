# 힙



힙의 특성(최소 힙 Min Heap)에서는 부모가 항상 자식보다 작거나 같다) 를 만족하는 거의 완전한 트리 Almost Complete Tree 인 특수한 트리 기반 자료구조



Heap 은 그래프나 트리와는 전혀 관계 없어 보이는 독특한 이름과 달리, 트리 기반의 자료구조.

앞서 우선순위 큐를 사용할 때 매번 활용했던 heapq 모듈이 바로 힙으로 구현되어 있으며, 그중에서도 파이썬에는 최소 힙만 구현되어 있다.

 최소 힙은 부모가 항상 자식보다 작기 때문에 루트가 결국 가장 작은 값을 갖게 되며, 우선순위 큐에서 가장 작은 값을 추출하는 것은 매번 힙의 루트를 가져오는 형태로 구현된다. 기반 구현을 살펴보면, 우선순위 큐 ADT는 주로 힙으로 구현하고, 힙은 주로 배열로 구현한다. 따라서 우선순위 큐는 결국은 배열로 구현하는 셈.



오해하기 쉬운 특징 중 하나는 힙은 정렬된 구조가 아니라는 점.

최소 힙의 경우 부모 노드가 항상 작다는 조건만 만족할 뿐, 서로 정렬되어 있지 않다. 예를 들어 오른쪽의 자식 노드가 레벨 차이에도 불구하고, 왼쪽 노드보다 더 작은 경우도 얼마든지 있을 수 있다.



힙은 완전 이진 트리이기 때문에 배열에 순서대로 표현하기에 적합하다. 이처럼 루트부터 차례대로 나열하면 1, 2, 4, -- 순서대로 각 레벨의 노드가 2배씩 증가하는 형태로 배열에 나열할 수 있다.

트리의 배열 표현의 경우 곅산을 편하기 하기 위해 인덱스는 1부터 사용한다. 항상 균형을 유지하는 특징 때문에 다양한 분야에 활용. 대표적으로 우선 순위 큐 뿐만 아니라 이를 이용한 다익스트라 알고리즘에도 활용. 



## 힙 연산

- Heaps 모듈에서 지원하는 최소힙 연산을 여기서는 파이썬의 리스트만으로 동일하게 구현해보자.

  ```python
  class BinaryHeap(object):
    def __init__(self):
      self.items=[None]
      
    def __len__(self):
      return len(self.items) - 1
  ```

-  삽입

  힙에 요소를 삽입하기 위해서는 Up-Heap 연산을 수행해야 한다. 일반적으로 업힙 연산은 percolate-up()이라는 함수로 정의.  힙에 요소를 삽입하는 과정은 다음과 같다.

  1. 요소의 가장 하위 레벨의 최대한 왼쪽으로 삽입(배열로 표현할 경우 가장 마지막에 삽입)
  2. 부모 값과 비교해 값이 더 작은 경우 위치를 변경한다.
  3. 계속해서 부모 값과 비교해 위치를 변경한다.(가장 작은 값일 경우 루트까지 올라감)

  ![image-20210311093347779](https://tva1.sinaimg.cn/large/008eGmZEgy1gofnzg6rlqj314q0r8u0x.jpg)

  ```python
  def _percolate_up(self):
    i = len(self)
    parent = i // 2
    while parent >= 0:
      if self.item[i] < self.items[parent]:
        self.items[parent], self.items[i] = self.items[i], self.items[parent]
        i = parent
        parent = i // 2
  
  def insert(self, k):
    self.items.append(k)
    self._percolate_up()
  ```

  삽입 자체는 insert()함수를 호출해 실행. 코드에서 insert()함수의 self.items.append()는 1번 과정, self._percolate_up()이 2,3번 과정 



- 추출

  루트를 추출하면 된다. 추출 이후에 다시 힙의 특성을 유지하는 작업이 필요하기 때문에 시간 복잡도는 O(log n).  
  ![image-20210311094608850](https://tva1.sinaimg.cn/large/008eGmZEgy1gofoc9ui23j316e0qcqv5.jpg)

  ```python
  Max-Heapify(A, i):
    left <- 2xi
    right <- 2xi + 1
    largest <- i
    
    if left <= heap_length[A] and A[left] > A[largest] then:
      largest <- left
    
    if right <= heap_length[A] and A[right] > A[largest] then:
      largest <- right
      
    if largest != i then:
      swap A[i] and A[largest]
      Max-Heapify(A, largest)
    
  ```

  왜 인덱스 0을 항상 비워놓고, 1번 인덱스부터 사용하는 이유는 인덱스 계산을 편하게 하기 위함. 

  ```python
  Parent(i)
  	return ceil((i - 1) / 2)
  
  Left(i)
  	return 2i
  
  Right(i)
  	return 2i + 1
  ```

  ```python
  def _percolate_down(self, idx):
    left = idx * 2
    right = idx * 2 + 1
    smallest = idx
    
    if left <= len(self) and self.items[left] < self.items[smallest]:
      smallest = left
    if right <= len(self) and self.items[right] < self.items[smallest]:
      smallest = right
    
    if smallest != idx:
      self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
      self._percolate_down(smallest)
  
  def extract(self):
    extracted = self.item[1]
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._percolate_down(1)
    return extracted
  ```

  

---


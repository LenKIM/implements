# 끼리끼리 알고리즘👨🏻‍💻



# 1. 현황

범주 - 오케이 👌 | 못품 🙅‍♂️

| Leetcode                                               | Hackerrank | 현황 |
| ------------------------------------------------------------ | ---- | ---- |
| [문제43](https://leetcode.com/problems/diameter-of-binary-tree/)<br>[문제44](https://leetcode.com/problems/longest-univalue-path/) | - [Sales By Match](https://www.hackerrank.com/challenges/sock-merchant/problem)<br>- [Counting Vally](https://www.hackerrank.com/challenges/counting-valleys/problem)<br>- [Jumping on the Clouds](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem)<br>- [Repeated String](https://www.hackerrank.com/challenges/repeated-string/problem) | len 👌<br>dhkim 👌    |
| [문제45](https://leetcode.com/problems/invert-binary-tree/)<br>[문제46](https://leetcode.com/problems/merge-two-binary-trees/) | - [Insert a node at a specific position in a linked list](https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem)<br>- [Inserting a Node Into a Sorted Doubly Linked List](https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem)<br>- [Largest Rectangle](https://www.hackerrank.com/challenges/largest-rectangle/problem) | len 👌<br>dhkim 👌 |
| [문제47](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)<br>[문제48](https://leetcode.com/problems/balanced-binary-tree/)<br>[문제49](https://leetcode.com/problems/minimum-height-trees/) | - [Largest Rectangle](https://www.hackerrank.com/challenges/largest-rectangle/problem)<br>- [Castle on the Grid](https://www.hackerrank.com/challenges/castle-on-the-grid/problem) | len 👌<br>dhkim 👌 |
| [문제50](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)<br>[문제51](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) | - [Reverse a doubly linked list](https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem)<br>- [Find Merge Point of Two Lists](https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem) | len 👌<br>dhkim 👌 |
| [문제52](https://leetcode.com/problems/range-sum-of-bst/)<br>[문제53](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | - [Tree: Height of a Binary Tree](https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem)<br>- [Binary Search Tree : Lowest Common Ancestor](https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem) | len 👌<br>dhkim 👌 |
| [문제54](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)<br>[문제55](https://leetcode.com/problems/kth-largest-element-in-an-array) | - [Sorting: Bubble Sort](https://www.hackerrank.com/challenges/ctci-bubble-sort/problem)<br>- [Mark and Toys](https://www.hackerrank.com/challenges/mark-and-toys/problem)<br>- [Sorting: Comparator](https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem) |  |
|                                                              |      |      |
|                                                              |      |      |



# 2. 협업 도구 및 코드 공유 형식⭐️

### 과제 공유 방식

Slack + Github 노티 푸시 형식으로 진행후 코드리뷰 후 PR merge 진행 (단, 각자 푼 시간을 체크하여 기재)

### 풀이 시간 기재

예: 1시간 이상 - 초과, 00분~60분 사이

### 스터디 2시간 진행 방식

1시간 30분 코드 리뷰 및 손코딩 대비, 30분 즉석 문제 풀이(추후 변경 가능)



# 3. 푸는 문제

- 파이썬 알고리즘 인터뷰 문제 리스트

- [해커링크 문제 리스트](https://github.com/LenKIM/implements/blob/master/hackerrank_list.md)



# 4. Github PR 방식💻

### 요약

1. main, develop 브랜치로 나누어서 브랜치 진행
2. 알고리즘 풀이 후, develop 브랜치로 commit 및 push 진행
3. push 이후 PR 요청 후 오른쪽 Reviewers 팀원 지정후 Request 요청
4. 스터디원 모두 코드 리뷰 완료되면 main 브랜치로 Merge



### PR Flow

```
git add (파일명 또는 전체(.))
git commit -m "커밋 메시지"
git push origin develop
정상적으로 push 진행 후 github에서 코드 리뷰어 지정 및 Pull Request 요청
요청된 문제 코드 리뷰 진행
모든 팀원 코드 리뷰 완료시 main 브랜치로 Merge
```



# 5. Commit 메시지 규칙📌

- `FIX` - 보통 올바르지 않은 동작을 고친 경우에 사용합니다.
- `ADD` - 코드나 테스트, 예제, 문서 등의 추가가 있을 때 사용합니다
- `REMOVE` - 코드의 삭제가 있을 때 사용
- `REFACTOR` - 전면 수정이 있을 때 사용합니다.
- `UPDATE` - 원래도 정상적으로 동작하고 있었지만, 수정, 추가, 보완을 한다는 개념입니다. 코드보다는 주로 문서나 리소스, 라이브러리등에 사용합니다
- `IMPROVE` - 향상이 있을 때 사용합니다. 호환성, 테스트 커버리지, 성능, 검증 기능, 접근성 등 다양한 것들이 목적
- `MAKE` - 주로 기존 동작의 변경을 명시합니다.
- `REVISE` - 문서의 개정이 있을 때 주로 사용합니다.
- `CORRECT` - 주로 문법의 오류나 타입의 변경, 이름 변경 등에 사용합니다.
- `MOVE` - 코드의 이동이 있을 때 사용합니다.
- `RENAME` - 이름 변경이 있을 때 사용합니다.
- `VERIFY` - 검증 코드를 넣을 때 주로 사용합니다.


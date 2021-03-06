# 유니코드와 UTF-8



초기에 문자를 표현하던 대표적인 방식은 ASCII 인코딩 방식

*1바이트에 모든 문자를 표현 1바이트는 8비트*

1비트는 체크섬(Checksum)으로 제외하여 7비트, 즉 128글자로 문자를 표현

그러므로, 한글이나 특수문자는 해결을 할 수 없어, 이를 해결하기 위해 2~4 바이트의 공간에 여유 있게 문자를 할당하고자 **등장한 방식이 바로 유니코드(Unicode)**다. 그러나 유니코드 자체는 1바이트로 표현이 가능한 영문자도 2바이트 이상의 공간을 사용하기 때문에 이를 그래도 사용하면 메모리 낭비가 심하고 따라서 **이를 가변 길이 문자 인코딩 방식으로 효율적으로 인코딩하는 대표적인 방식이 바로 우리가 잘 아는 UTF-8**이다. 



 파이썬이 어떻게 문자열 처리 방식할까?

파이썬3부터는 영어뿐만 아니라 한글, 한자 등의 다국어를 출력시 모두 유니코드 기반으로 전환됐고, 쓰는 입장에서는 파이썬에서 가장 좋아진 부분이기도 하다.



**유니코드의 가변 길이 문자 인코딩 방식인 UTF-8의 내부 구조**를 좀 더 상세히 살펴보자.



python 이라는 영문 문자열은 총 24바이트의 메모릴 차치하게 될 것.

ASCII 코드로 충분히 표현이 가능하기 때문에 각 문자당 1바이트로 충분한데, 모든 문자가 4바이트를 차지하기 때문에 사실상 문자마다 3바이트씩 빈 공간으로 낭비되고 있다. 이런 문제를 해결하기 위해 나온 유명한 방식이 UTF-8이다.

그렇다면 UTF-8은 유니코드를 어떤 방식으로 인코딩할까?

| 바이트 수 | 바이트1  | 바이트2  | 바이트3  | 바이트4  |
| --------- | -------- | -------- | -------- | -------- |
| 1         | 0xxxxxxx |          |          |          |
| 2         | 110xxxxx | 10xxxxxx |          |          |
| 3         | 1110xxxx | 10xxxxxx | 10xxxxxx |          |
| 4         | 1110xxx  | 10xxxxxx | 10xxxxxx | 10xxxxxx |



시작 비트를 살펴보면 문자의 전체 바이트를 결정할 수 있다.

- 첫 바이트의 맨 앞 비트를 확인해서 0인 경우 1바이트 문자, 10인 경우 특정 문자의 중간 바이트, 110인 경우 2바이트, 1110인 경우 3바이트, 11110인 경우 4바이트, 이와 같은 방식으로 문자 바이트의 길이를 인식할 수 있다.

유니코드 값에 따라 가변적으로 바이트를 결정하여 불필요한 공간낭비를 절약할 수 있다는 점. 값이 128이하라면 1바이트로 표현한다. ASCII문자는 128개이며, 이 문자들의 유니코드 값은 동일하므로, 영문, 숫자를 포함한 기존ASCII 문자는 모두 그대로 1바이트에 표현이 가능하다.


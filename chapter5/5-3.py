### 패키지
# 모듈의 집합

import sys
sys.path.append('C:/python')

import game.sound.echo
game.sound.echo.echo_test()

from game.sound.echo import echo_test
echo_test()

print(game.VERSION)

# 모든 것을 불러오는 법
from game.sound import *
echo_test()
# 이걸 가능하게 하려면 sound 디렉터리의 init파일에 __all__변수를 설정하고 모듈을 정의해주어야 한다
# __all__이 의미하는 것은 sound 디렉터리에서 *를 사용하여 import할 경우, 이곳에 정의된 echo 모듈만 import된다는 의미이다.

## 접근자
# .. 부모 디렉터리
# . 현재 디렉터리